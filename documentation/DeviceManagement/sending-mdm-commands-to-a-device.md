# Sending MDM Commands to a Device

**Framework**: Device Management

Execute commands on a device and receive responses that contain the results of each operation.

#### Overview

Once a device installs the MDM enrollment profile, the MDM server can send commands to it. The MDM server sends a push notification to the device to initiate communication, and the device responds and establishes a secure connection with it. Then the server can send commands to the device, which the device executes and reports results back to the server. Wait for the response from a device with a matching `UUID` for a command, to verify that the device executed it. This value corresponds to the contents of the `User ID` parameter in the `Subject` field of the push-notification client certificate.

##### Initiate Polling for Mdm Commands

The MDM server sends a notification through the APNS gateway to the device, to make a device poll the MDM server for commands. Format the message that the server sends with the push notification as JSON, and only include the `PushMagic` string as the value of the `mdm` key; for example:

`{"mdm":"PushMagicValue"}`

In place of `PushMagicValue`, substitute the actual `PushMagic` string that the device sends to the MDM server in the `TokenUpdate` message. This is the complete message. Don’t include an `aps` key, which you only use for third-party app push notifications. It’s safe to send several push notifications to a device, because APNS coalesces multiple notifications and delivers only the last one.

##### Establish a Connection to the Mdm Server

In response to receiving a push notification from an MDM server, a device initiates communication by establishing a TLS connection to the MDM server URL. The device validates the server’s certificate, then uses its identity as the client certificate to authentication for the connection.

> **Note**:  MDM follows HTTP `3xx` redirections without user interaction. However, it doesn’t save the URL given by HTTP `301` (Moved Permanently) redirections. Each transaction begins at the URL the MDM payload specifies.

The device then sends a request-payload message in a plist-encoded dictionary to the MDM server using an HTTP PUT request. This message contains either an `Idle` status or the result of a previous operation.

A request payload message looks like this:

```other
PUT /your/url HTTP/1.1
Host: www.yourhostname.com
Content-Length: 1234
Content-Type: application/x-apple-aspen-mdm; charset=UTF-8

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0"> 
<dict>
    <key>UDID</key>
    <string>...</string>
    <key>CommandUUID</key>
    <string>9F09D114-BCFD-42AD-A974-371AA7D6256E</string>
    <key>Status</key>
    <string>Acknowledged</string> 
</dict>
</plist>
```

##### Send a Command to the Device

The server responds to the request-payload message from the device by sending a response-payload message back to the device enclosed in an HTTP reply. This message includes the next command for the device to execute in a plist-encoded dictionary that contains the following required keys:

| Key | Type | Content |
| --- | --- | --- |
| `Command` | Dictionary | The command dictionary. |
| `CommandUUID` | String | The unique identifier of the command. |

Include the `RequestType` key in the content of the `Command` dictionary, along with additional keys defined by each command. For example, here’s a request payload message:

```other
HTTP/1.1 200 OK
Content-Length: 1234
Content-Type: application/xml; charset=UTF-8

<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<!-- PEALISTv1: TextSize:0| -->
<plist version="1.0">
<dict>
    <key>CommandUUID</key>
    <string>9F09D114-BCFD-42AD-A974-371AA7D6256E</string>
    <key>Command</key>
    <dict>
        <key>RequestType</key>
        <string>...</string>
    </dict>
</dict>
</plist>
```

##### Execute the Command and Report Results

The device executes the command and sends its response in another HTTP PUT request to the MDM server. The response includes a plist-encoded dictionary that contains the following keys, and additional keys returned by the command:

| Key | Type | Content |
| --- | --- | --- |
| `CommandUUID` | String | The unique identifier of the command for this response. |
| `ErrorChain` | Array | If present, an array of dictionaries that describes any errors that occurred. The first item represents the top-level error. Subsequent items represent the underlying errors that led up to the top-level error. |
| `Status` | String | The status of the response, which is one of the following values: ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `Acknowledged`: The device processed the command successfully. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `Error`: An error occurred. See the `ErrorChain` for more details. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `CommandFormatError`: A protocol error occurred, which can result from a malformed command. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `Idle`: The device is idle; there’s no status. ![None](https://docs-assets.developer.apple.com/published/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `NotNow`: The device received the command, but couldn’t execute it. For more information, see [`Handling NotNow Status Responses`](handling-notnow-status-responses.md). |
| `UDID` | String | The unique identifier of the device. |

Each entry in the `ErrorChain` contains the following dictionary:

| Key | Type | Content |
| --- | --- | --- |
| `ErrorCode` | Integer | The error code. |
| `ErrorDomain` | String | The error domain. |
| `LocalizedDescription` | String | A description of the error in the device’s localized language. |
| `USEnglishDescription` | String | A description of the error in U.S. English. |

The `ErrorCode` and `ErrorDomain` keys contain internal codes that are useful for diagnostics. However, don’t rely on these values, because they may change between software releases.

If the device disconnects from the MDM server while processing a command, it caches the result of the command and reports the result when it reconnects.

##### Receive Results and Optionally Send Another Command

When the server receives a response from the device, it can either reply with the next command or end the connection by sending a `200` status (OK) with an empty response body.

If the connection breaks or the server returns a non `200` status while performing a command, the device caches the result of the command and re-attempts a connection to the server until the server returns a `2xx` status.

> **Note**:  An empty response body is zero bytes in length and doesn’t contain an empty property list.

##### Manage the Command Queue

Don’t consider a command accepted and executed by a device until the server receives the `Acknowledged` or `Error` status with the command `UUID` in the message. Until then, leave the last command on the queue.

It’s also possible for the device to send the same status twice. Examine the `CommandUUID` value in the deviceʼs status message to determine which command to which it applies.

## See Also

- [Handling NotNow Status Responses](handling-notnow-status-responses.md)
  Handle when a device won’t execute a command and instead returns a NotNow status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/sending-mdm-commands-to-a-device)*
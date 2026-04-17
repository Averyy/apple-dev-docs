# Request Mirroring

**Framework**: Device Management  
**Kind**: httpRequest

Prompt the user to share their screen using AirPlay Mirroring.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- macOS 10.10+

#### Discussion

Provide either the `DestinationName` or the `DestinationDeviceID`. If you provide both values, MDM uses `DestinationDeviceID`.

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device channel | iOS, macOS, Shared iPad |
| User channel | NA |
| Requires supervision | NA |
| Allowed in user enrollment | iOS, macOS |
| Required access right | NA |

##### Example Request and Response

**Request**:

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Command</key>
    <dict>
        <key>DestinationName</key>
        <string>Apple TV</string>
        <key>Password</key>
        <string>password</string>
        <key>RequestType</key>
        <string>RequestMirroring</string>
        <key>ScanTime</key>
        <integer>30</integer>
    </dict>
    <key>CommandUUID</key>
    <string>0001_RequestMirroring</string>
</dict>
</plist>
```

**Response**:

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CommandUUID</key>
    <string>0001_RequestMirroring</string>
    <key>MirroringResult</key>
    <string>Unknown</string>
    <key>Status</key>
    <string>Acknowledged</string>
    <key>UDID</key>
    <string>00008020-000915083C80012E</string>
</dict>
</plist>
```

## Topics

### Commands and responses
- [object RequestMirroringCommand](requestmirroringcommand.md)
  The command to prompt the user to share their screen using AirPlay Mirroring.
- [object RequestMirroringResponse](requestmirroringresponse.md)
  A response from the device after it processes the command to prompt the user to share their screen using AirPlay Mirroring.

## Endpoint

`PUT https://yourmdmhost.example.com/mdm#RequestMirroringCommand`

## Request Body

The request object the server returns for the Request Mirroring Command.

## See Also

- [Stop Mirroring](stop-mirroring-command.md)
  Stop mirroring the display to another device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/request-mirroring-command)*
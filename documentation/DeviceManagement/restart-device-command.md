# Restart Device

**Framework**: Device Management  
**Kind**: httpRequest

Remotely and immediately restart a device.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- macOS 10.13+
- tvOS 10.2+

#### Discussion

A passcode-locked iOS device doesn’t rejoin a Wi-Fi network after restarting, so it may not be able to communicate with the server.

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device channel | iOS, macOS, Shared iPad, tvOS |
| User channel | NA |
| Requires supervision | iOS, macOS, tvOS |
| Allowed in user enrollment | NA |
| Required access right | AllowPasscodeRemovalAndLock |

##### Example Request and Response

**Request**:

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Command</key>
    <dict>
        <key>RequestType</key>
        <string>RestartDevice</string>
    </dict>
    <key>CommandUUID</key>
    <string>0001_RestartDevice</string>
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
    <string>0001_RestartDevice</string>
    <key>Status</key>
    <string>Acknowledged</string>
    <key>UDID</key>
    <string>00008020-000915083C80012E</string>
</dict>
</plist>
```

## Topics

### Commands and responses
- [object RestartDeviceCommand](restartdevicecommand.md)
  The command to remotely and immediately restart a device.
- [object RestartDeviceResponse](restartdeviceresponse.md)
  A response from the device after it processes the command to remotely and immediately restart a device.

## Endpoint

`PUT https://yourmdmhost.example.com/mdm#RestartDeviceCommand`

## Request Body

The request object the server returns for the Restart Device Command.

## See Also

- [Erase Device](erase-device-command.md)
  Remotely and immediately erase a device.
- [Device Lock](device-lock-command.md)
  Remotely and immediately lock a device.
- [Shut Down Device](shut-down-device-command.md)
  Remotely and immediately shut down a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/restart-device-command)*
# Enable Remote Desktop

**Framework**: Device Management  
**Kind**: httpRequest

Enable Remote Desktop on a device.

**Availability**:
- macOS 10.14.4+
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

This command enables the following capabilities on the device:

- Remote Desktop with the All Users access
- The ability to receive remote events
- The Observe, Control, and Show being Observed options

All other options remain unchanged.

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device channel | macOS |
| User channel | NA |
| Requires supervision | macOS |
| Allowed in user enrollment | NA |
| Required access right |  |

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
        <string>EnableRemoteDesktop</string>
    </dict>
    <key>CommandUUID</key>
    <string>0001_EnableRemoteDesktop</string>
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
    <string>0001_EnableRemoteDesktop</string>
    <key>Status</key>
    <string>Acknowledged</string>
    <key>UDID</key>
    <string>E84CD517-CB37-52F7-988C-DB5137B604B8</string>
</dict>
</plist>
```

## Topics

### Commands and responses
- [object EnableRemoteDesktopCommand](enableremotedesktopcommand.md)
  The command to enable Remote Desktop on a device.
- [object EnableRemoteDesktopResponse](enableremotedesktopresponse.md)
  A response from the device after it processes the command to enable Remote Desktop on a device.

## Endpoint

`PUT https://yourmdmhost.example.com/mdm#EnableRemoteDesktopCommand`

## Request Body

The request object the server returns for the Enable Remote Desktop Command.

## See Also

- [Disable Remote Desktop](disable-remote-desktop-command.md)
  Disable Remote Desktop on a device.
- [Settings](settings-command.md)
  Configure settings on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/enable-remote-desktop-command)*
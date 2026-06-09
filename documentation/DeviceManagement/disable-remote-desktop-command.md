# Disable Remote Desktop

**Framework**: Device Management  
**Kind**: httpRequest

Disable Remote Desktop on a device.

**Availability**:
- macOS 10.14.4+

#### Discussion

This command disables Remote Desktop on the device, and prevents any further remote event processing. It removes any `PostEvent` Transparency Consent and Control (TCC) ability, unless the device already has an installed TCC configuration profile with that ability enabled.

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device channel | macOS |
| User channel | N/A |
| Requires supervision | macOS |
| Allowed in user enrollment | N/A |
| Required access right | N/A |

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
        <string>DisableRemoteDesktop</string>
    </dict>
    <key>CommandUUID</key>
    <string>0001_DisableRemoteDesktop</string>
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
    <string>0001_DisableRemoteDesktop</string>
    <key>Status</key>
    <string>Acknowledged</string>
    <key>UDID</key>
    <string>E84CD517-CB37-52F7-988C-DB5137B604B8</string>
</dict>
</plist>
```

## Topics

### Commands and responses
- [object DisableRemoteDesktopCommand](disableremotedesktopcommand.md)
  The command to disable Remote Desktop on a device.
- [object DisableRemoteDesktopResponse](disableremotedesktopresponse.md)
  A response from the device after it processes the command to disable Remote Desktop on a device.

## Endpoint

`PUT https://yourmdmhost.example.com/mdm`

## Request Body

The request object the server returns for the Disable Remote Desktop Command.

## See Also

- [Enable Remote Desktop](enable-remote-desktop-command.md)
  Enable Remote Desktop on a device.
- [Settings](settings-command.md)
  Configure settings on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/disable-remote-desktop-command)*
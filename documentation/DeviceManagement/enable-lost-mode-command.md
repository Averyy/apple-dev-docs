# Enable Lost Mode

**Framework**: Device Management  
**Kind**: httpRequest

Enable Lost Mode on a device, which provides a message and phone number on the Lock Screen.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+

#### Discussion

While in Lost Mode, a device responds to invalid commands with error code `12078`.

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device channel | iOS, Shared iPad |
| User channel | NA |
| Requires supervision | iOS |
| Allowed in user enrollment | NA |
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
        <key>Footnote</key>
        <string>Return to Acme, Inc.</string>
        <key>Message</key>
        <string>Lock Message</string>
        <key>PhoneNumber</key>
        <string>408-555-555</string>
        <key>RequestType</key>
        <string>EnableLostMode</string>
    </dict>
    <key>CommandUUID</key>
    <string>0001_EnableLostMode</string>
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
    <string>0001_EnableLostMode</string>
    <key>Status</key>
    <string>Acknowledged</string>
    <key>UDID</key>
    <string>00008020-000915083C80012E</string>
</dict>
</plist>
```

## Topics

### Commands and responses
- [object EnableLostModeCommand](enablelostmodecommand.md)
  The command to enable Lost Mode on a device, which provides a message and phone number on the Lock Screen.
- [object EnableLostModeResponse](enablelostmoderesponse.md)
  A response from the device after it processes the command to enable Lost Mode on a device, which provides a message and phone number on the Lock Screen.

## Endpoint

`PUT https://yourmdmhost.example.com/mdm`

## Request Body

The request object the server returns for the Enable Lost Mode Command.

## See Also

- [Device Location](device-location-command.md)
  Request the location of a device when in Lost Mode.
- [Play Lost Mode Sound](play-lost-mode-sound-command.md)
  Play the Lost Mode sound on a device that’s in Lost Mode.
- [Disable Lost Mode](disable-lost-mode-command.md)
  Take the device out of Lost Mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/enable-lost-mode-command)*
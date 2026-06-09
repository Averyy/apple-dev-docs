# Play Lost Mode Sound

**Framework**: Device Management  
**Kind**: httpRequest

Play the Lost Mode sound on a device that’s in Lost Mode.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 10.3+

#### Discussion

A device responds with error code:

- `12067`: If it isn’t in Lost mode.
- `12078`: If the command is invalid while in Lost Mode.

The sound plays until the server disables Lost Mode or the user disables the sound on the device.

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device channel | iOS, Shared iPad |
| User channel | N/A |
| Requires supervision | iOS |
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
        <string>PlayLostModeSound</string>
    </dict>
    <key>CommandUUID</key>
    <string>0001_PlayLostModeSound</string>
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
    <string>0001_PlayLostModeSound</string>
    <key>Status</key>
    <string>Acknowledged</string>
    <key>UDID</key>
    <string>00008020-000915083C80012E</string>
</dict>
</plist>
```

## Topics

### Commands and responses
- [object PlayLostModeSoundCommand](playlostmodesoundcommand.md)
  The command to play the Lost Mode sound on a device that’s in Lost Mode.
- [object PlayLostModeSoundResponse](playlostmodesoundresponse.md)
  A response from the device after it processes the command to play the Lost Mode sound on a device that’s in Lost Mode.

## Endpoint

`PUT https://yourmdmhost.example.com/mdm`

## Request Body

The request object the server returns for the Play Lost Mode Sound Command.

## See Also

- [Enable Lost Mode](enable-lost-mode-command.md)
  Enable Lost Mode on a device, which provides a message and phone number on the Lock Screen.
- [Device Location](device-location-command.md)
  Request the location of a device when in Lost Mode.
- [Disable Lost Mode](disable-lost-mode-command.md)
  Take the device out of Lost Mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/play-lost-mode-sound-command)*
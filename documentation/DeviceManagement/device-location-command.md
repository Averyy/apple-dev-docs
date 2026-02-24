# Device Location

**Framework**: Device Management  
**Kind**: httpRequest

Request the location of a device when in Lost Mode.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+

#### Discussion

A device responds with error codes:

- `12067`: If it isn’t in Lost mode.
- `12068`: If its location is unknown.
- `12078`: If the command is invalid while in Lost Mode.

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
        <key>RequestType</key>
        <string>DeviceLocation</string>
    </dict>
    <key>CommandUUID</key>
    <string>0001_DeviceLocation</string>
</dict>
</plist>
```

**Response**:

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Altitude</key>
    <real>-1.0</real>
    <key>CommandUUID</key>
    <string>0246_DeviceLocation</string>
    <key>Course</key>
    <real>-1.0</real>
    <key>HorizontalAccuracy</key>
    <real>3.677859038862057</real>
    <key>Latitude</key>
    <real>37.33385013244351</real>
    <key>Longitude</key>
    <real>-122.01079213269968</real>
    <key>Speed</key>
    <real>-1.0</real>
    <key>Status</key>
    <string>Acknowledged</string>
    <key>Timestamp</key>
    <string>2019-09-04T22:35:52Z</string>
    <key>UDID</key>
    <string>00008020-000915083C80012E</string>
    <key>VerticalAccuracy</key>
    <real>-1.0</real>
</dict>
</plist>
```

## Topics

### Commands and responses
- [object DeviceLocationCommand](devicelocationcommand.md)
  The command to request the location of a device when in Lost Mode.
- [object DeviceLocationResponse](devicelocationresponse.md)
  A response from the device after it processes the command to request the location of a device when in Lost Mode.

## Endpoint

`PUT https://yourmdmhost.example.com/mdm`

## Request Body

The request object the server returns for the Device Location Command.

## See Also

- [Enable Lost Mode](enable-lost-mode-command.md)
  Enable Lost Mode on a device, which provides a message and phone number on the Lock Screen.
- [Play Lost Mode Sound](play-lost-mode-sound-command.md)
  Play the Lost Mode sound on a device that’s in Lost Mode.
- [Disable Lost Mode](disable-lost-mode-command.md)
  Take the device out of Lost Mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/device-location-command)*
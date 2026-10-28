# Stop Mirroring

**Framework**: Device Management  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Stop mirroring the display to another device.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 7.0+
- macOS 10.10+

## Discussion

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

### Command availability

|  |  |
| --- | --- |
| Device channel | iOS, macOS, Shared iPad |
| User channel | N/A |
| Requires supervision | iOS, macOS |
| Allowed in user enrollment | N/A |
| Required access right | N/A |

### Example request and response

**Request**:

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Command</key>
    <dict>
        <key>RequestType</key>
        <string>StopMirroring</string>
    </dict>
    <key>CommandUUID</key>
    <string>0001_StopMirroring</string>
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
    <string>0001_StopMirroring</string>
    <key>Status</key>
    <string>Acknowledged</string>
    <key>UDID</key>
    <string>00008020-000915083C80012E</string>
</dict>
</plist>
```

## Topics

### Commands and responses
- [object StopMirroringCommand](./stopmirroringcommand.md)
  The command to stop mirroring the display to another device.
- [object StopMirroringResponse](./stopmirroringresponse.md)
  A response from the device after it processes the command to stop mirroring the display to another device.

## Endpoint

`PUT https://yourmdmhost.example.com/mdm`

## Request Body

**Content-Type**: `application/x-apple-aspen-mdm`  
**Type**: `StopMirroringCommand`

The request object the server returns for the Stop Mirroring Command.

## Responses

- `200` OK (`StopMirroringResponse`, `application/xml`): The response object the system returns for the Stop Mirroring Command.

## See Also

### AirPlay mirroring
- [Request Mirroring](./request-mirroring-command.md)
  Prompt the user to share their screen using AirPlay Mirroring.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/stop-mirroring-command)*
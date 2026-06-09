# Erase Device

**Framework**: Device Management  
**Kind**: httpRequest

Remotely and immediately erase a device.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 4.0+
- macOS 10.7+
- tvOS 10.2+
- visionOS 1.1+
- watchOS 10.0+

## Mentions

- [Returning a managed device to service](returning-a-managed-device-to-service.md)

#### Discussion

This command allows the server to immediately erase a device, even a locked device, without warning the user. The device sends a response to the server, but it doesn’t retry if it isn’t successful the first time.

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device channel | iOS, macOS, Shared iPad, tvOS, visionOS, watchOS |
| User channel | N/A |
| Requires supervision | macOS |
| Allowed in user enrollment | N/A |
| Required access right | AllowDeviceErase |

##### Example Request and Response

**Request**:

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Command</key>
    <dict>
        <key>DisallowProximitySetup</key>
        <false/>
        <key>PreserveDataPlan</key>
        <true/>
        <key>RequestType</key>
        <string>EraseDevice</string>
    </dict>
    <key>CommandUUID</key>
    <string>0001_EraseDevice</string>
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
    <string>0001_EraseDevice</string>
    <key>Status</key>
    <string>Acknowledged</string>
    <key>UDID</key>
    <string>00008020-000915083C80012E</string>
</dict>
</plist>
```

## Topics

### Commands and responses
- [object EraseDeviceCommand](erasedevicecommand.md)
  The command to remotely and immediately erase a device.
- [object EraseDeviceResponse](erasedeviceresponse.md)
  A response from the device after it processes the command to remotely and immediately erase a device.

## Endpoint

`PUT https://yourmdmhost.example.com/mdm`

## Request Body

The request object the server returns for the Erase Device Command.

## See Also

- [Device Lock](device-lock-command.md)
  Remotely and immediately lock a device.
- [Restart Device](restart-device-command.md)
  Remotely and immediately restart a device.
- [Shut Down Device](shut-down-device-command.md)
  Remotely and immediately shut down a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/erase-device-command)*
# Device Configured

**Framework**: Device Management  
**Kind**: httpRequest

Inform the device that it can allow the user to continue in Setup Assistant.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- macOS 10.11+
- tvOS 10.2+
- visionOS 2.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Mentions

- [Implementing Platform SSO for unattended device enrollment](implementing-platform-sso-for-unattended-device-enrollment.md)
- [Migrating managed devices](migrating-managed-devices.md)
- [Returning a managed device to service](returning-a-managed-device-to-service.md)

#### Discussion

This command only works on Device Enrollment Program (DEP) devices that have their cloud configuration set to await configuration.

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device channel | iOS, macOS, Shared iPad, tvOS, visionOS |
| User channel | NA |
| Requires supervision | iOS, macOS, tvOS, visionOS |
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
        <string>DeviceConfigured</string>
    </dict>
    <key>CommandUUID</key>
    <string>0001_DeviceConfigured</string>
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
    <string>0001_DeviceConfigured</string>
    <key>Status</key>
    <string>Acknowledged</string>
    <key>UDID</key>
    <string>00008020-000915083C80012E</string>
</dict>
</plist>
```

## Topics

### Commands and responses
- [object DeviceConfiguredCommand](deviceconfiguredcommand.md)
  The command to inform the device that it can allow the user to continue in Setup Assistant.
- [object DeviceConfiguredResponse](deviceconfiguredresponse.md)
  A response from the device after it processes the command to inform the device that it can allow the user to continue in Setup Assistant.

## Endpoint

`PUT https://yourmdmhost.example.com/mdm#DeviceConfiguredCommand`

## Request Body

The request object the server returns for the Device Configured Command.

## See Also

- [Device Information](device-information-command.md)
  Get detailed information about a device.
- [User Configured](user-configured-command.md)
  Inform the device that it can continue past Setup Assistant and finish login.
- [Restrictions](restrictions-command.md)
  Get a list of restrictions on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/device-configured-command)*
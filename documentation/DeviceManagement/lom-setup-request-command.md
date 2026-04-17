# LOM Setup Request

**Framework**: Device Management  
**Kind**: httpRequest

Get information from a device to set up lights-out management (LOM).

**Availability**:
- macOS 11.0+

#### Discussion

This command requires the `DeviceLockAndRemovePasscode` access right, [`LightsOutManagementLOM`](lightsoutmanagementlom.md) configuration and is available in macOS 11 and later on [`supported macOS devices`](https://developer.apple.comhttps://support.apple.com/guide/deployment/lights-out-management-payload-settings-dep580cf25bc/web).

##### Command Availability

|  |  |
| --- | --- |
| Device channel | macOS |
| User channel | NA |
| Requires supervision | macOS |
| Allowed in user enrollment | NA |
| Required access right | DeviceLockAndRemovePasscode |

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
        <string>LOMSetupRequest</string>
    </dict>
    <key>CommandUUID</key>
    <string>0001_LOMSetupRequest</string>
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
    <string>0001_LOMSetupRequest</string>
    <key>PrimaryIPv6AddressList</key>
    <array>
       <string>fe80::94f6:d6ff:fef3:c05b</string>
       <string>fe80::94f6:d6ff:fef3:c1a4</string>
    </array>
    <key>Status</key>
    <string>Acknowledged</string>
    <key>UDID</key>
    <string>84341F79-92F5-5EF7-9A6A-3A7374613227</string>
</dict>
</plist>
```

## Topics

### Commands and responses
- [object LOMSetupRequestCommand](lomsetuprequestcommand.md)
  The command to get information from a device to set up lights-out management (LOM).
- [object LOMSetupRequestResponse](lomsetuprequestresponse.md)
  A response from the device after it processes the command to get information from a device to set up lights-out management (LOM).

## Endpoint

`PUT https://yourmdmhost.example.com/mdm#LOMSetupRequestCommand`

## Request Body

The request object the server returns for the LOM Setup Request Command.

## See Also

- [LOM Device Request](lom-device-request-command.md)
  Send requests to a device using lights-out management (LOM).


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/lom-setup-request-command)*
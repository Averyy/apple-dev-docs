# LOM Device Request

**Framework**: Device Management  
**Kind**: httpRequest

Send requests to a device using lights-out management (LOM).

**Availability**:
- macOS 11.0+

#### Discussion

This command requires the `DeviceLockAndRemovePasscode` access right, [`LightsOutManagementLOM`](lightsoutmanagementlom.md) configuration and is available in macOS 11 and later on [`supported macOS devices`](https://developer.apple.comhttps://support.apple.com/guide/deployment/lights-out-management-payload-settings-dep580cf25bc/web).

`DeviceDNSName` is the `CommonName` in the Identity issued on the client certificate from [`LightsOutManagementLOM`](lightsoutmanagementlom.md). [`LOMSetupRequestResponse`](lomsetuprequestresponse.md) returns `PrimaryIPv6AddressList` and `SecondaryIPv6AddressList` after a successful deployment of Lights Out management configuration payload and subsequent [`LOMSetupRequestCommand`](lomsetuprequestcommand.md).

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
        <key>RequestList</key>
    <array>
        <dict>
            <key>DeviceDNSName</key>
            <string>lomdevice.com</string>
            <key>DeviceRequestType</key>
            <string>Reset</string>
            <key>DeviceRequestUUID</key>
            <string>0001</string>
            <key>PrimaryIPv6AddressList</key>
            <array>
                <string>fe80::94f6:d6ff:fef3:c05b</string>
                <string>fe80::94f6:d6ff:fef3:c1a4</string>
            </array>
            <key>SecondaryIPv6AddressList</key>
            <array/>
        </dict>
    </array>
    </dict>
    <key>CommandUUID</key>
    <string>0001_LOMDeviceRequest</string>
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
    <string>0001_LOMDeviceRequest</string>
    <key>ResponseData</key>
    <array>
        <dict>
            <key>DeviceRequestSucess</key>
            <true/>
            <key>DeviceRequestUUID</key>
            <string>0001</string>
        </dict>
    </array>
    <key>Status</key>
    <string>Acknowledged</string>
    <key>UDID</key>
    <string>37CECCAB-99C1-5ADF-8A9A-2AFA3B6387B5</string>
</dict>
</plist>
```

## Topics

### Commands and responses
- [object LOMDeviceRequestCommand](lomdevicerequestcommand.md)
  The command to send requests to a device using lights-out management (LOM).
- [object LOMDeviceRequestResponse](lomdevicerequestresponse.md)
  A response from the device after it processes the command to send requests to a device using lights-out management (LOM).

## Endpoint

`PUT https://yourmdmhost.example.com/mdm#LOMDeviceRequestCommand`

## Request Body

The request object the server returns for the LOM Device Request Command.

## See Also

- [LOM Setup Request](lom-setup-request-command.md)
  Get information from a device to set up lights-out management (LOM).


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/lom-device-request-command)*
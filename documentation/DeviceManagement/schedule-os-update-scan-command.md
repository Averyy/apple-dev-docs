# Schedule OS Update Scan

**Framework**: Device Management  
**Kind**: httpRequest

Schedule a background scan for operating-system updates on a device.

**Availability**:
- macOS 10.11+

#### Discussion

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device channel | macOS |
| User channel | NA |
| Requires supervision | macOS |
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
        <key>ForceUpdateScan</key>
        <false/>
        <key>RequestType</key>
        <string>ScheduleOSUpdateScan</string>
    </dict>
    <key>CommandUUID</key>
    <string>0001_ScheduleOSUpdateScan</string>
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
    <string>0316_ScheduleOSUpdateScan</string>
    <key>ScanInitiated</key>
    <true/>
    <key>ScanInititated</key>
    <true/>
    <key>Status</key>
    <string>Acknowledged</string>
    <key>UDID</key>
    <string>E84CD517-CB37-52F7-988C-DB5137B604B8</string>
</dict>
</plist>
```

## Topics

### Commands and responses
- [object ScheduleOSUpdateScanCommand](scheduleosupdatescancommand.md)
  The command to schedule a background scan for operating-system updates on a device.
- [object ScheduleOSUpdateScanResponse](scheduleosupdatescanresponse.md)
  A response from the device after it processes the command to schedule a background scan for operating-system updates on a device.

## Endpoint

`PUT https://yourmdmhost.example.com/mdm`

## Request Body

The request object the server returns for the Schedule OS Update Scan Command.

## See Also

- [Available OS Updates](available-os-updates-command.md)
  Get a list of available operating-system updates for a device.
- [Schedule OS Update](schedule-os-update-command.md)
  Schedule an update of the operating system on a device.
- [OS Update Status](os-update-status-command.md)
  Get the status of operating-system updates on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/schedule-os-update-scan-command)*
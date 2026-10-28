# Schedule OS Update Scan

**Framework**: Device Management  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Schedule a background scan for operating-system updates on a device. Removed: use the declarative management `com.apple.configuration.softwareupdate.enforcement.specific` configuration.

**Availability**:
- macOS 10.11+ - Deprecated in 26.0

> **Deprecated**: **Removed** Use the declarative management software update features instead.

## Discussion

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

### Command availability

|  |  |
| --- | --- |
| Device channel | macOS |
| User channel | N/A |
| Requires supervision | macOS |
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
- [object ScheduleOSUpdateScanCommand](./scheduleosupdatescancommand.md)
  The command to schedule a background scan for operating-system updates on a device. Removed: use the declarative management `com.apple.configuration.softwareupdate.enforcement.specific` configuration.
- [object ScheduleOSUpdateScanResponse](./scheduleosupdatescanresponse.md)
  A response from the device after it processes the command to schedule a background scan for operating-system updates on a device. Removed: use the declarative management `com.apple.configuration.softwareupdate.enforcement.specific` configuration.

## Endpoint

`PUT https://yourmdmhost.example.com/mdm`

## Request Body

**Content-Type**: `application/x-apple-aspen-mdm`  
**Type**: `ScheduleOSUpdateScanCommand`

The request object the server returns for the Schedule OS Update Scan Command.

## Responses

- `200` OK (`ScheduleOSUpdateScanResponse`, `application/xml`): The response object the system returns for the Schedule OS Update Scan Command.

## See Also

### Commands
- [Available OS Updates](./available-os-updates-command.md)
  Get a list of available operating-system updates for a device. Removed: use the declarative management `com.apple.configuration.softwareupdate.enforcement.specific` configuration.
- [OS Update Status](./os-update-status-command.md)
  Get the status of operating-system updates on a device. Removed: subscribe to the declarative management `softwareupdate.install-state` status item.
- [Schedule OS Update](./schedule-os-update-command.md)
  Schedule an update of the operating system on a device. Removed: use the declarative management `com.apple.configuration.softwareupdate.enforcement.specific` configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/schedule-os-update-scan-command)*
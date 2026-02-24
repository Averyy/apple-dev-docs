# Available OS Updates

**Framework**: Device Management  
**Kind**: httpRequest

Get a list of available operating-system updates for a device.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- macOS 10.11+
- tvOS 12.0+

#### Discussion

A device must have a total of `DownloadSize` + `InstallSize` bytes available to successfully install a software update. In macOS, execute the `ScheduleOSUpdateScan` command to update the results that this command returns. In iOS and tvOS, the list only contains the latest available updates.

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device channel | iOS, macOS, Shared iPad, tvOS |
| User channel | NA |
| Requires supervision | iOS, macOS, tvOS |
| Allowed in user enrollment | NA |
| Required access right | AllowAppInstallation |

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
        <string>AvailableOSUpdates</string>
    </dict>
    <key>CommandUUID</key>
    <string>0001_AvailableOSUpdates</string>
</dict>
</plist>
```

**Response**:

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>AvailableOSUpdates</key>
    <array>
        <dict>
            <key>AllowsInstallLater</key>
            <false/>
            <key>Build</key>
            <string>17A576</string>
            <key>DownloadSize</key>
            <integer>251607570</integer>
            <key>HumanReadableName</key>
            <string>iOS 13.0</string>
            <key>InstallSize</key>
            <integer>1809842176</integer>
            <key>IsCritical</key>
            <false/>
            <key>ProductKey</key>
            <string>iOSUpdate17A576</string>
            <key>ProductName</key>
            <string>iOS</string>
            <key>RestartRequired</key>
            <true/>
            <key>Version</key>
            <string>13.0</string>
        </dict>
    </array>
    <key>CommandUUID</key>
    <string>0001_AvailableOSUpdates</string>
    <key>Status</key>
    <string>Acknowledged</string>
    <key>UDID</key>
    <string>00008020-000915083C80012E</string>
</dict>
</plist>
```

## Topics

### Commands and responses
- [object AvailableOSUpdatesCommand](availableosupdatescommand.md)
  The command to get a list of available operating-system updates for a device.
- [object AvailableOSUpdatesResponse](availableosupdatesresponse.md)
  A response from the device after it processes the command to get a list of available operating-system updates for a device.

## Endpoint

`PUT https://yourmdmhost.example.com/mdm`

## Request Body

The request object the server returns for the Available OS Updates Command.

## See Also

- [Schedule OS Update Scan](schedule-os-update-scan-command.md)
  Schedule a background scan for operating-system updates on a device.
- [Schedule OS Update](schedule-os-update-command.md)
  Schedule an update of the operating system on a device.
- [OS Update Status](os-update-status-command.md)
  Get the status of operating-system updates on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/available-os-updates-command)*
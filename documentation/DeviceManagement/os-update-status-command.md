# OS Update Status

**Framework**: Device Management  
**Kind**: httpRequest

Get the status of operating-system updates on a device.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- macOS 10.11.5+
- tvOS 12.0+

#### Discussion

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
        <string>OSUpdateStatus</string>
    </dict>
    <key>CommandUUID</key>
    <string>0001_OSUpdateStatus</string>
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
    <string>0001_OSUpdateStatus</string>
    <key>OSUpdateStatus</key>
    <array>
        <dict>
            <key>DownloadPercentComplete</key>
            <real>0.5030184984207153</real>
            <key>IsDownloaded</key>
            <false/>
            <key>ProductKey</key>
            <string>iOSUpdate17A576</string>
            <key>Status</key>
            <string>Downloading</string>
        </dict>
    </array>
    <key>Status</key>
    <string>Acknowledged</string>
    <key>UDID</key>
    <string>00008020-000915083C80012E</string>
</dict>
</plist>
```

## Topics

### Commands and responses
- [object OSUpdateStatusCommand](osupdatestatuscommand.md)
  The command to get the status of operating-system updates on a device.
- [object OSUpdateStatusResponse](osupdatestatusresponse.md)
  A response from the device after it processes the command to get the status of operating-system updates on a device.

## Endpoint

`PUT https://yourmdmhost.example.com/mdm#OSUpdateStatusCommand`

## Request Body

The request object the server returns for the OS Update Status Command.

## See Also

- [Schedule OS Update Scan](schedule-os-update-scan-command.md)
  Schedule a background scan for operating-system updates on a device.
- [Available OS Updates](available-os-updates-command.md)
  Get a list of available operating-system updates for a device.
- [Schedule OS Update](schedule-os-update-command.md)
  Schedule an update of the operating system on a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/os-update-status-command)*
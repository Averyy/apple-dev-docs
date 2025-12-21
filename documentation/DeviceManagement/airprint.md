# AirPrint

**Framework**: Device Management  
**Kind**: dictionary

The payload that configures AirPrint printer discoverability in the user’s printer list.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- macOS 10.10+
- visionOS 2.0+

## Declaration

```swift
object AirPrint
```

#### Discussion

Specify `com.apple.airprint` as the payload type.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | iOS, macOS, Shared iPad, visionOS |
| User channel | macOS |
| Allow manual install | iOS, macOS, visionOS |
| Requires supervision | NA |
| Requires user-approved MDM | NA |
| Allowed in user enrollment | iOS, macOS, visionOS |
| Allow multiple payloads | iOS, macOS, Shared iPad, visionOS |

##### Profile Example

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadContent</key>
    <array>
        <dict>
            <key>AirPrint</key>
            <array>
                <dict>
                    <key>IPAddress</key>
                    <string>10.0.1.42</string>
                    <key>ResourcePath</key>
                    <string>/ipp/print</string>
                </dict>
            </array>
            <key>PayloadDescription</key>
            <string>Configures AirPrint settings</string>
            <key>PayloadDisplayName</key>
            <string>AirPrint</string>
            <key>PayloadIdentifier</key>
            <string>com.example.myairprintpayload</string>
            <key>PayloadType</key>
            <string>com.apple.airprint</string>
            <key>PayloadUUID</key>
            <string>01bd840a-42d2-4d7a-97d3-4580bc671ff9</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>AirPrint</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>159a5866-8323-4be1-84b1-fa4db5e04f0f</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## Topics

### Objects
- [object AirPrint.AirPrintItem](airprint/airprintitem.md)
  A dictionary of AirPrint printer details.

## See Also

- [object Printing](printing.md)
  The payload that configures printers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/airprint)*
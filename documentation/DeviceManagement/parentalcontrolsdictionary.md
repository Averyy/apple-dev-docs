# ParentalControlsDictionary

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure parental control dictionary restrictions.

**Availability**:
- macOS 10.7+

## Declaration

```swift
object ParentalControlsDictionary
```

#### Discussion

Specify `com.apple.Dictionary` as the payload type.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | macOS |
| User channel | macOS |
| Allow manual install | macOS |
| Requires supervision | NA |
| Requires user-approved MDM | NA |
| Allowed in user enrollment | NA |
| Allow multiple payloads | NA |

##### Profile Example

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadContent</key>
    <array>
        <dict>
            <key>parentalControl</key>
            <true/>
            <key>PayloadIdentifier</key>
            <string>com.example.mydictionarypayload</string>
            <key>PayloadType</key>
            <string>com.apple.Dictionary</string>
            <key>PayloadUUID</key>
            <string>0158853b-e3d5-41d6-b4d2-ada868a36042</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Parental Controls Dictionary</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>9b0ea70d-b1b1-4a96-81e7-3b33bfd563d5</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## See Also

- [object ParentalControlsApplicationRestrictions](parentalcontrolsapplicationrestrictions.md)
  The payload you use to configure parental controls for apps.
- [object ParentalControlsContentFilter](parentalcontrolscontentfilter.md)
  The payload you use to configure the parental control web content filters.
- [object ParentalControlsGameCenter](parentalcontrolsgamecenter.md)
  The payload you use to configure Game Center parental controls.
- [object ParentalControlsTimeLimits](parentalcontrolstimelimits.md)
  The payload you use to configure parental control time limits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/parentalcontrolsdictionary)*
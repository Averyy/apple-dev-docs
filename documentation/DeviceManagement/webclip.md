# WebClip

**Framework**: Device Management  
**Kind**: dictionary

The profile you use to configure web clips on the device.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- macOS 10.7+

## Declaration

```swift
object WebClip
```

#### Discussion

Specify `com.apple.webClip.managed` as the payload type.

Use this payload to add web clips to the Home screen of the user’s iOS device or to the Dock on a Mac. Web clips provide fast access to favorite webpages.

For iOS devices, if you prevent the user from removing the web clip, the only way to remove it is to remove the configuration profile that installed it. Also, for iOS devices it must have a display name and an icon URL for the payload to be valid.

A full-screen web clip on iOS devices opens the URL as a web app without a browser; there’s no URL, search bar, or bookmarks.

For Shared iPad devices, the system supports this payload on the user channel only.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | iOS |
| User channel | macOS, Shared iPad |
| Allow manual install | iOS, macOS |
| Requires supervision | NA |
| Requires user-approved MDM | NA |
| Allowed in user enrollment | iOS, macOS |
| Allow multiple payloads | iOS, macOS, Shared iPad |

##### Profile Example

```plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadContent</key>
    <array>
        <dict>
            <key>FullScreen</key>
            <true/>
            <key>IgnoreManifestScope</key>
            <false/>
            <key>IsRemovable</key>
            <true/>
            <key>Label</key>
            <string>Example</string>
            <key>Precomposed</key>
            <false/>
            <key>URL</key>
            <string>example.com</string>
            <key>PayloadIdentifier</key>
            <string>com.example.mywebclippayload</string>
            <key>PayloadType</key>
            <string>com.apple.webClip.managed</string>
            <key>PayloadUUID</key>
            <string>1d6d6912-708e-441a-9272-526ef05bbe3c</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Web Clip</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>289fc7fc-2870-479d-b30f-8d0592b7ef04</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## See Also

- [object WebContentFilter](webcontentfilter.md)
  The payload you use to configure web content filters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/webclip)*
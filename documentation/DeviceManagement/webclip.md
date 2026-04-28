# WebClip

**Framework**: Device Management  
**Kind**: dictionary

The profile that configures web clips on the device.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 4.0+
- macOS 10.7+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object WebClip
```

#### Discussion

Specify `com.apple.webClip.managed` as the payload type.

Use this payload to add web clips to the Home Screen of the user’s iOS device or to the Dock on a Mac. Web clips provide fast access to favorite webpages.

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

## Properties

- `FullScreen` (boolean): If `true`, the system launches the web clip as a full-screen web app.
- `Icon` (data): The PNG icon to show on the Home Screen. If not set, the system displays a white square. For best results, provide a square image that’s no larger than 400 x 400 pixels and less than 1 MB when uncompressed. The graphics file is automatically scaled and cropped to fit, if necessary, and converted to PNG format. Web clip icons are 144 x 144 pixels for iPad devices with a Retina display, and 114 x 114 pixels for iPhone devices. To prevent the device from adding a shine to the image, set `Precomposed` to `true`.
- `IgnoreManifestScope` (boolean): If `true`, a full screen web clip can navigate to an external web site without showing Safari UI. Otherwise, Safari UI appears when navigating away from the web clip’s URL. This key has no effect when `FullScreen` is `false`. Available in iOS 14 and later.
- `IsRemovable` (boolean): If `true`, the system enables removing the web clip.
- `Label` (string) *(required)*: The name of the web clip that the system displays on the Home Screen.
- `Precomposed` (boolean): If `true`, the system prevents SpringBoard from adding shine to the icon.
- `TargetApplicationBundleIdentifier` (string): The application bundle identifier of the application that opens the URL. To use this property, install the profile through MDM. Available in iOS 14 and later.
- `URL` (string) *(required)*: The URL of the web clip.

## See Also

- [object WebContentFilter](webcontentfilter.md)
  The payload that configures web content filters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/webclip)*
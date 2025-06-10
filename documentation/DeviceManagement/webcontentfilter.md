# WebContentFilter

**Framework**: Device Management  
**Kind**: dictionary

The payload you use to configure web content filters.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- macOS 10.15+
- visionOS 1.1+

## Declaration

```swift
object WebContentFilter
```

#### Discussion

Specify `com.apple.webcontent-filter` as the payload type.

The system matches URLs using string-based matching. A URL matches an allow list, deny list, or permitted list pattern if the exact characters of the pattern appear as a substring of the URL requested in the web browser. For example, if the system doesn’t allow `test.com/a`, it blocks `test.com/a`, `test.com/apple`, and `test.com/a/b`.

The system matches list entries that terminate with a `/` character explicitly; if the system blocks or allows `test.com/a/`, it blocks or allows `test.com/a` and `test.com/a/b`.

Matching discards a `www` subdomain prefix if present, so if the system doesn’t allow `www.test.com`, it also blocks `m.test.com`.

All filtering options are active simultaneously. The system only permits URLs and sites that pass all rules.

##### Profile Availability

|  |  |
| --- | --- |
| Device channel | iOS, macOS, Shared iPad, visionOS |
| User channel | NA |
| Allow manual install | iOS, macOS, visionOS |
| Requires supervision | NA |
| Requires user-approved MDM | NA |
| Allowed in user enrollment | iOS, visionOS |
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
            <key>AutoFilterEnabled</key>
            <true/>
            <key>DenylistURLs</key>
            <array>
                <string>https://notallowedname.company.com</string>
            </array>
            <key>FilterBrowsers</key>
            <true/>
            <key>FilterSockets</key>
            <true/>
            <key>FilterType</key>
            <string>BuiltIn</string>
            <key>PermittedURLs</key>
            <array>
                <string>https://example.company.com</string>
            </array>
            <key>PayloadIdentifier</key>
            <string>com.example.mywebcontentfilterpayload</string>
            <key>PayloadType</key>
            <string>com.apple.webcontent-filter</string>
            <key>PayloadUUID</key>
            <string>fb5d598f-0a96-4b77-9702-9edfc3417601</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Web Content Filter</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>b510e0c6-dc81-4b62-88d0-6a3ef82925e7</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## Topics

### Objects
- [object WebContentFilter.AllowListBookmarksItem](webcontentfilter/allowlistbookmarksitem.md)
  The bookmark in the allow list of the web content filter.
- [object WebContentFilter.URLFilterParameters](webcontentfilter/urlfilterparameters-data.dictionary.md)
  A dictionary containing URL filter parameters.
- [object WebContentFilter.VendorConfig](webcontentfilter/vendorconfig-data.dictionary.md)
  A custom dictionary for the filtering service plug-in.
- [object WebContentFilter.WhitelistedBookmarksItem](webcontentfilter/whitelistedbookmarksitem.md)
  The bookmark in the allow list of the web content filter.

## See Also

- [object WebClip](webclip.md)
  The profile you use to configure web clips on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/webcontentfilter)*
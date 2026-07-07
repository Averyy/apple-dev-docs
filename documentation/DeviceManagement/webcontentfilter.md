# WebContentFilter

**Framework**: Device Management  
**Kind**: dictionary

The payload that configures web content filters.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 7.0+
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
| User channel | N/A |
| Allow manual install | iOS, macOS, visionOS |
| Requires supervision | N/A |
| Requires user-approved MDM | N/A |
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
                <string>https://notallowed.example.com</string>
            </array>
            <key>FilterBrowsers</key>
            <true/>
            <key>FilterSockets</key>
            <true/>
            <key>FilterType</key>
            <string>BuiltIn</string>
            <key>PermittedURLs</key>
            <array>
                <string>https://allowed.example.com</string>
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

## Properties

- `AllowListBookmarks` ([WebContentFilter.AllowListBookmarksItem]): An array of dictionaries that define the pages that the user can bookmark or visit. Use when `FilterType` is `BuiltIn`. Available: iOS 14.5+ | iPadOS 14.5+ | visionOS 1.1+
- `AutoFilterEnabled` (boolean): If `true`, the system enables automatic filtering. Use when `FilterType` is `BuiltIn`. Available: iOS 7+ | iPadOS 7+ | visionOS 1.1+
- `BlacklistedURLs` ([string]): Use `DenyListURLs` instead. Available: iOS 7+ | iPadOS 7+
Deprecated: iOS 14.5+ | iPadOS 14.5+
- `ContentFilterUUID` (string): A globally unique identifier for this content filter configuration. The content filter processes network traffic for managed apps with the same `ContentFilterUUID` in their app attributes. Use when `FilterType` is `Plugin`.This key must be present for unsupervised devices and user enrollment. Available: iOS 16+ | iPadOS 16+ | visionOS 1.1+
- `DenyListURLs` ([string]): An array of URLs that are inaccessible. Use when `FilterType` is `BuiltIn`. Limit the number of these URLs to no more than 500. Available: iOS 14.5+ | iPadOS 14.5+ | visionOS 1.1+
- `FilterBrowsers` (boolean): If `true`, the system enables filtering WebKit traffic. Use when `FilterType` is `Plugin`. > **Note**:  At least one of `FilterBrowsers` or `FilterSockets` needs to be `true`. Available: iOS 7+ | iPadOS 7+ | visionOS 1.1+
- `FilterDataProviderBundleIdentifier` (string): The bundle identifier string of the filter data provider system extension. This string identifies the filter data provider when the filter starts running. Required if `FilterSockets` is `true`.
- `FilterDataProviderDesignatedRequirement` (string): The designated requirement string that the system embeds in the code signature of the filter data provider system extension. This string identifies the filter data provider when the filter starts running. Required if `FilterSockets` is `true`. Available: macOS 10.15+
- `FilterGrade` (string): The system uses this value to derive the relative order of content filters. Filters with a grade of `firewall` see network traffic before filters with a grade of `inspector`. However, the system doesn’t define the order of filters within a grade. Available: macOS 10.15+
- `FilterPacketProviderBundleIdentifier` (string): The bundle identifier string of the filter packet provider system extension. This string identifies the filter packet provider when the filter starts running. Required if `FilterPackets` is `true`. Available: macOS 10.15+
- `FilterPacketProviderDesignatedRequirement` (string): The designated requirement string that the system embeds in the code signature of the filter packet provider system extension. This string identifies the filter packet provider when the filter starts running. Required if `FilterPackets` is `true`. Available: macOS 10.15+
- `FilterPackets` (boolean): If `true` and `FilterType` is `Plugin`, the system enables filtering network packets. Use when `FilterType` is `Plugin`. > **Note**:  At least one of `FilterPackets` or `FilterSockets` needs to be `true`. Available: macOS 10.15+
- `FilterSockets` (boolean): If `true`, enables the filtering of socket traffic. Use when `FilterType` is `Plugin`. > **Note**:  At least one of `FilterBrowsers` or `FilterSockets` needs to be `true`.
- `FilterType` (string): The type of filter, built-in or plug-in. In macOS, the system only supports the plug-in value. Available: iOS 8+ | iPadOS 8+ | macOS 10.15+ | visionOS 1.1+
- `FilterURLs` (boolean): If `true`, the system filters URL requests. Use when `FilterType` is `Plugin`. Available: iOS 26+ | iPadOS 26+ | macOS 26+
- `HideDenyListURLs` (boolean): If `true`, the device hides the `DenyListURLs` item in the profiles that display in Settings > General > VPN & Device Management. Available: iOS 18+ | iPadOS 18+ | visionOS 2+
- `Organization` (string): The organization string to pass to the third-party plug-in. Use when `FilterType` is `Plugin`.
- `Password` (string): The password for the service. Use when `FilterType` is `Plugin`.
- `PayloadCertificateUUID` (string): The UUID of the certificate payload within the same profile that the system uses to authenticate the user. Use when `FilterType` is `Plugin`.
- `PermittedURLs` ([string]): An array or URLs that are accessible whether or not the automatic filter allows access. Use when `FilterType` is `BuiltIn`. Requires that `AutoFilterEnabled` is `true`. Available: iOS 7+ | iPadOS 7+ | visionOS 1.1+
- `PluginBundleID` (string): The bundle ID of the plug-in that provides filtering service. Required when `FilterType` is `Plugin`. Otherwise, it ignores this value. Consult your filtering solution vendor to determine what to specify for this value. Required when `FilterType` is `Plugin`.
- `SafariHistoryRetentionEnabled` (boolean): If `true`, this payload enforces a policy which requires retention of browsing history. This causes Safari to disable clearing of browsing history, and prevents the use of private browsing mode because that mode doesn’t keep browsing history. Available: iOS 26+ | iPadOS 26+ | macOS 26+ | visionOS 26+
- `ServerAddress` (string): The server address, which may be the IP address, hostname, or URL. Use when `FilterType` is `Plugin`.
- `URLFilterParameters` (WebContentFilter.URLFilterParameters): A dictionary containing URL filter parameters. Required when `FilterURLs` is `true`. Available: iOS 26+ | iPadOS 26+ | macOS 26+
- `UserDefinedName` (string): The display name for this filtering configuration. Required when `FilterType` is `Plugin`.
- `UserName` (string): The user name for the service. Use when `FilterType` is `Plugin`.
- `VendorConfig` (WebContentFilter.VendorConfig): The custom dictionary that the filtering service plug-in needs. Use when `FilterType` is `Plugin`.
- `WhitelistedBookmarks` ([WebContentFilter.WhitelistedBookmarksItem]): Use `AllowListBookmarks` instead. Available: iOS 7+ | iPadOS 7+
Deprecated: iOS 14.5+ | iPadOS 14.5+

## See Also

- [object WebClip](webclip.md)
  The profile that configures web clips on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/webcontentfilter)*
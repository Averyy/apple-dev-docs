# ParentalControlsContentFilter

**Framework**: Device Management  
**Kind**: dictionary

The payload that configures the parental control web content filters.

**Availability**:
- macOS 10.7+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object ParentalControlsContentFilter
```

#### Discussion

Specify `com.apple.familycontrols.contentfilter` as the payload type.

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
            <key>filterAllowList</key>
            <array>
                <string>http://www.example.com</string>
            </array>
            <key>filterDenyList</key>
            <array>
                <string>http://www.example2.com</string>
            </array>
            <key>siteAllowList</key>
            <array>
                <dict>
                    <key>address</key>
                    <string>http://www.example3.com</string>
                    <key>bookmarkPath</key>
                    <string>/</string>
                    <key>pageTitle</key>
                    <string>example3</string>
                </dict>
            </array>
            <key>restrictWeb</key>
            <true/>
            <key>useContentFilter</key>
            <true/>
            <key>allowListEnabled</key>
            <true/>
            <key>PayloadIdentifier</key>
            <string>com.example.mycontentfilterpayload</string>
            <key>PayloadType</key>
            <string>com.apple.familycontrols.contentfilter</string>
            <key>PayloadUUID</key>
            <string>342c6863-6e3c-4e00-893e-f76757ae41c7</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDisplayName</key>
    <string>Parental Controls Content Filter</string>
    <key>PayloadIdentifier</key>
    <string>com.example.myprofile</string>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>764e94bc-ab75-456f-ac47-3a1062e70ffb</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

## Topics

### Objects
- [object ParentalControlsContentFilter.SiteAllowListItem](parentalcontrolscontentfilter/siteallowlistitem.md)
  A dictionary defining a site for the allow list.
- [object ParentalControlsContentFilter.SiteWhitelistItem](parentalcontrolscontentfilter/sitewhitelistitem.md)
  A dictionary defining a site for the allow list.

## Properties

- `allowListEnabled` (boolean): If `true`, enables web content filters.
- `filterAllowList` ([string]): The array of URLs that defines an allow list. When `restrictWeb` and `useContentFilter` are enabled, only URLs in the allow list are available to the user.
- `filterBlacklist` ([string]): Use `filterDenyList` instead.
- `filterDenyList` ([string]): The array of URLs that defines a deny list. When `restrictWeb` and `useContentFilter` are enabled, no URLs in the deny list are available to the user.
- `filterWhitelist` ([string]): Use `filterAllowList` instead.
- `restrictWeb` (boolean) *(required)*: If `true`, enables web content filters.
- `siteAllowList` ([ParentalControlsContentFilter.SiteAllowListItem]): An array of sites that defines an allow list. If specified, this defines additional allowed sites besides those in the automated allow list and deny list, including disallowed adult sites. This key is required if `allowListEnabled` is `true`.
- `siteWhitelist` ([ParentalControlsContentFilter.SiteWhitelistItem]): Use `siteAllowList` instead.
- `useContentFilter` (boolean): If `true`, filters content automatically.
- `whitelistEnabled` (boolean): Use `allowListEnabled` instead.

## See Also

- [object ParentalControlsApplicationRestrictions](parentalcontrolsapplicationrestrictions.md)
  The payload that configures parental controls for apps.
- [object ParentalControlsDictionary](parentalcontrolsdictionary.md)
  The payload that configures parental control dictionary restrictions.
- [object ParentalControlsGameCenter](parentalcontrolsgamecenter.md)
  The payload that configures Game Center parental controls.
- [object ParentalControlsTimeLimits](parentalcontrolstimelimits.md)
  The payload that configures parental control time limits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/parentalcontrolscontentfilter)*
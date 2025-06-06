# WebContentSettings

**Framework**: ManagedSettings  
**Kind**: struct

An object that configures which websites a user can access.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
struct WebContentSettings
```

## Topics

### Filtering Web Domains
- [var blockedByFilter: WebContentSettings.FilterPolicy?](webcontentsettings/blockedbyfilter-swift.property.md)
  The current policy for filtering websites.
- [static let blockedByFilter: SettingMetadata<WebContentSettings.FilterPolicy>](webcontentsettings/blockedbyfilter-swift.type.property.md)
  A description of the setting that controls which websites a user can access.
- [WebContentSettings.FilterPolicy](webcontentsettings/filterpolicy.md)
  The policies available for filtering web content based on specific web domains.

## Relationships

### Conforms To
- [ManagedSettingsGroup](managedsettingsgroup.md)

## See Also

- [var safari: SafariSettings](managedsettingsstore/safari.md)
  Settings that affect Safari’s search results and cookie policies.
- [struct SafariSettings](safarisettings.md)
  Constraints on Safari’s AutoFill and cookie behaviors.
- [var webContent: WebContentSettings](managedsettingsstore/webcontent.md)
  Settings that affect web content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/webcontentsettings)*
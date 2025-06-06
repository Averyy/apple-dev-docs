# SafariSettings

**Framework**: ManagedSettings  
**Kind**: struct

Constraints on Safari’s AutoFill and cookie behaviors.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
struct SafariSettings
```

#### Overview

Use `SafariSettings` to manage Safari settings for cookies and AutoFill. You can prevent AutoFill and specify the websites from which Safari accepts cookies.

## Topics

### Specifying a Cookie Policy
- [var cookiePolicy: SafariSettings.CookiePolicy?](safarisettings/cookiepolicy-swift.property.md)
  Defines the conditions under which Safari accepts cookies.
- [static let cookiePolicy: SettingMetadata<SafariSettings.CookiePolicy>](safarisettings/cookiepolicy-swift.type.property.md)
  The metadata for the setting that configures Safari’s policy for cookies.
- [SafariSettings.CookiePolicy](safarisettings/cookiepolicy-swift.enum.md)
  The conditions under which Safari accepts cookies.
### Denying AutoFill
- [var denyAutoFill: Bool?](safarisettings/denyautofill-swift.property.md)
  A Boolean value that indicates whether Safari’s AutoFill feature is active.
- [static let denyAutoFill: SettingMetadata<Bool>](safarisettings/denyautofill-swift.type.property.md)
  The metadata associated with the setting that deactivates Safari’s AutoFill feature.

## Relationships

### Conforms To
- [ManagedSettingsGroup](managedsettingsgroup.md)

## See Also

- [var safari: SafariSettings](managedsettingsstore/safari.md)
  Settings that affect Safari’s search results and cookie policies.
- [var webContent: WebContentSettings](managedsettingsstore/webcontent.md)
  Settings that affect web content.
- [struct WebContentSettings](webcontentsettings.md)
  An object that configures which websites a user can access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/safarisettings)*
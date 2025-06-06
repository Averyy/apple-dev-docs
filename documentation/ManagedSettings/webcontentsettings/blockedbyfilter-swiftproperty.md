# blockedByFilter

**Framework**: ManagedSettings  
**Kind**: property

The current policy for filtering websites.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
var blockedByFilter: WebContentSettings.FilterPolicy? { get set }
```

#### Discussion

Setting any filter policy besides `.none` will disable Safari private browsing. The value is `nil` unless you specify a policy. Your app can block up to 50 web domains and specify up to 50 web domains exceptions at once.

## See Also

- [static let blockedByFilter: SettingMetadata<WebContentSettings.FilterPolicy>](webcontentsettings/blockedbyfilter-swift.type.property.md)
  A description of the setting that controls which websites a user can access.
- [WebContentSettings.FilterPolicy](webcontentsettings/filterpolicy.md)
  The policies available for filtering web content based on specific web domains.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/webcontentsettings/blockedbyfilter-swift.property)*
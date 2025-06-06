# blockedByFilter

**Framework**: ManagedSettings  
**Kind**: property

A description of the setting that controls which websites a user can access.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
static let blockedByFilter: SettingMetadata<WebContentSettings.FilterPolicy>
```

#### Discussion

The default value is [`WebContentSettings.FilterPolicy.none`](webcontentsettings/filterpolicy/none.md), which indicates that the system doesn’t block any websites.

## See Also

- [var blockedByFilter: WebContentSettings.FilterPolicy?](webcontentsettings/blockedbyfilter-swift.property.md)
  The current policy for filtering websites.
- [WebContentSettings.FilterPolicy](webcontentsettings/filterpolicy.md)
  The policies available for filtering web content based on specific web domains.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/webcontentsettings/blockedbyfilter-swift.type.property)*
# blockedByFilter

**Framework**: Managed Settings  
**Kind**: property  
**Role**: Type Property

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

The default value is [`WebContentSettings.FilterPolicy.none`](./filterpolicy/none.md), which indicates that the system doesn’t block any websites.

## See Also

### Filtering web domains
- [var blockedByFilter: WebContentSettings.FilterPolicy?](./blockedbyfilter-swift.property.md)
  The current policy for filtering websites.
- [WebContentSettings.FilterPolicy](./filterpolicy.md)
  The policies available for filtering web content based on specific web domains.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/webcontentsettings/blockedbyfilter-swift.type.property)*
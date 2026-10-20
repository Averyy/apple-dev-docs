# WebContentSettings.FilterPolicy

**Framework**: Managed Settings  
**Kind**: enum  
**Role**: Enumeration

The policies available for filtering web content based on specific web domains.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
enum FilterPolicy
```

## Topics

### Providing filters and exceptions
- [WebContentSettings.FilterPolicy.all(except:)](./filterpolicy/all%28except%29.md)
  The system blocks all websites except the ones you specify.
- [case auto(Set<WebDomain>, except: Set<WebDomain>)](./filterpolicy/auto%28_,except%29.md)
  The system blocks adult content.
- [WebContentSettings.FilterPolicy.none](./filterpolicy/none.md)
  The policy doesn’t affect any domains.
- [WebContentSettings.FilterPolicy.specific(_:)](./filterpolicy/specific%28_%29.md)
  The policy blocks the specified domains.
### Comparing policies
- [static func == (WebContentSettings.FilterPolicy, WebContentSettings.FilterPolicy) -> Bool](./filterpolicy/eqeq%28_,_%29.md)
  Returns a Boolean value that indicates whether two values are equal.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)

## See Also

### Filtering web domains
- [var blockedByFilter: WebContentSettings.FilterPolicy?](./blockedbyfilter-swift.property.md)
  The current policy for filtering websites.
- [static let blockedByFilter: SettingMetadata<WebContentSettings.FilterPolicy>](./blockedbyfilter-swift.type.property.md)
  A description of the setting that controls which websites a user can access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/webcontentsettings/filterpolicy)*
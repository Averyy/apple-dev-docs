# WebContentSettings.FilterPolicy

**Framework**: ManagedSettings  
**Kind**: enum

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

### Providing Filters and Exceptions
- [WebContentSettings.FilterPolicy.all(except:)](webcontentsettings/filterpolicy/all(except:).md)
  The system blocks all websites except the ones you specify.
- [case auto(Set<WebDomain>, except: Set<WebDomain>)](webcontentsettings/filterpolicy/auto(_:except:).md)
  The system blocks adult content.
- [WebContentSettings.FilterPolicy.none](webcontentsettings/filterpolicy/none.md)
  The policy doesn’t affect any domains.
- [WebContentSettings.FilterPolicy.specific(_:)](webcontentsettings/filterpolicy/specific(_:).md)
  The policy blocks the specified domains.
### Comparing Policies
- [static func == (WebContentSettings.FilterPolicy, WebContentSettings.FilterPolicy) -> Bool](webcontentsettings/filterpolicy/==(_:_:).md)
  Returns a Boolean value that indicates whether two values are equal.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)

## See Also

- [var blockedByFilter: WebContentSettings.FilterPolicy?](webcontentsettings/blockedbyfilter-swift.property.md)
  The current policy for filtering websites.
- [static let blockedByFilter: SettingMetadata<WebContentSettings.FilterPolicy>](webcontentsettings/blockedbyfilter-swift.type.property.md)
  A description of the setting that controls which websites a user can access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedsettings/webcontentsettings/filterpolicy)*
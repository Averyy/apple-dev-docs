# CSUserQuery.UserInteractionKind

**Framework**: Core Spotlight  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate how someone engaged with search-related content.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
enum UserInteractionKind
```

```c
enum CSUserInteraction : NSInteger;
```

## Topics

### Getting the interaction types
- [static var `default`: CSUserQuery.UserInteractionKind](./userinteractionkind/default.md)
- [CSUserQuery.UserInteractionKind.select](./userinteractionkind/select.md)
- [CSUserQuery.UserInteractionKind.focus](./userinteractionkind/focus.md)
### Creating an interaction kind
- [init?(rawValue: Int)](./userinteractionkind/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Improving the quality of ranked results
- [func userEngaged(CSUserQuery.Item, visibleItems: [CSUserQuery.Item], interaction: CSUserQuery.UserInteractionKind)](./userengaged%28_,visibleitems,interaction%29.md)
  Notifies the system that someone engaged with a specific search result in your app’s interface.
- [func userEngaged(CSUserQuery.Suggestion, visibleSuggestions: [CSUserQuery.Suggestion], interaction: CSUserQuery.UserInteractionKind)](./userengaged%28_,visiblesuggestions,interaction%29.md)
  Notifies the system that someone engaged with a specific text completion in your app’s interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/csuserquery/userinteractionkind)*
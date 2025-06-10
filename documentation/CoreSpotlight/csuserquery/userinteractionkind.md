# CSUserQuery.UserInteractionKind

**Framework**: Core Spotlight  
**Kind**: enum

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

## Topics

### Getting the interaction types
- [static var `default`: CSUserQuery.UserInteractionKind](csuserquery/userinteractionkind/default.md)
- [CSUserQuery.UserInteractionKind.select](csuserquery/userinteractionkind/select.md)
- [CSUserQuery.UserInteractionKind.focus](csuserquery/userinteractionkind/focus.md)
### Creating an interaction kind
- [init?(rawValue: Int)](csuserquery/userinteractionkind/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func userEngaged(CSUserQuery.Item, visibleItems: [CSUserQuery.Item], interaction: CSUserQuery.UserInteractionKind)](csuserquery/userengaged(_:visibleitems:interaction:).md)
  Notifies the system that someone engaged with a specific search result in your app’s interface.
- [func userEngaged(CSUserQuery.Suggestion, visibleSuggestions: [CSUserQuery.Suggestion], interaction: CSUserQuery.UserInteractionKind)](csuserquery/userengaged(_:visiblesuggestions:interaction:).md)
  Notifies the system that someone engaged with a specific text completion in your app’s interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/csuserquery/userinteractionkind)*
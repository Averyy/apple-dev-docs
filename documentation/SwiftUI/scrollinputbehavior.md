# ScrollInputBehavior

**Framework**: SwiftUI  
**Kind**: struct

A type that defines whether input should scroll a view.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct ScrollInputBehavior
```

## Topics

### Type Properties
- [static let automatic: ScrollInputBehavior](scrollinputbehavior/automatic.md)
  Indicates that the system should determine whether the associated input scrolls a view.
- [static let disabled: ScrollInputBehavior](scrollinputbehavior/disabled.md)
  Indicates that the associated input should not scroll a view.
- [static let enabled: ScrollInputBehavior](scrollinputbehavior/enabled.md)
  Indicates that the associated input should scroll a view.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func scrollInputBehavior(ScrollInputBehavior, for: ScrollInputKind) -> some View](view/scrollinputbehavior(_:for:).md)
  Enables or disables scrolling in scrollable views when using particular inputs.
- [struct ScrollInputKind](scrollinputkind.md)
  Inputs used to scroll views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scrollinputbehavior)*
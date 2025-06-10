# ScrollInputKind

**Framework**: SwiftUI  
**Kind**: struct

Inputs used to scroll views.

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
struct ScrollInputKind
```

## Topics

### Type Properties
- [static let handGestureShortcut: ScrollInputKind](scrollinputkind/handgestureshortcut.md)
  A finger or wrist movement that the user can perform in order to scroll a view.
- [static let look: ScrollInputKind](scrollinputkind/look.md)
  On visionOS, by looking at the edge of a scroll view the content can automatically scroll. The axes will be determined automatically.
### Type Methods
- [static func look(axes: Axis.Set) -> ScrollInputKind](scrollinputkind/look(axes:).md)
  On visionOS, by looking at the edge of a scroll view the content can automatically scroll. This contructor method takes a set of the scrollable axes.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func scrollInputBehavior(ScrollInputBehavior, for: ScrollInputKind) -> some View](view/scrollinputbehavior(_:for:).md)
  Enables or disables scrolling in scrollable views when using particular inputs.
- [struct ScrollInputBehavior](scrollinputbehavior.md)
  A type that defines whether input should scroll a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scrollinputkind)*
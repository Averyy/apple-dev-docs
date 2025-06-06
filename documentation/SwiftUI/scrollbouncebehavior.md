# ScrollBounceBehavior

**Framework**: SwiftUI  
**Kind**: struct

The ways that a scrollable view can bounce when it reaches the end of its content.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- tvOS 16.4+
- visionOS 1.0+
- watchOS 9.4+

## Declaration

```swift
struct ScrollBounceBehavior
```

#### Overview

Use the [`scrollBounceBehavior(_:axes:)`](view/scrollbouncebehavior(_:axes:).md) view modifier to set a value of this type for a scrollable view, like a [`ScrollView`](scrollview.md) or a [`List`](list.md). The value configures the bounce behavior when people scroll to the end of the view’s content.

You can configure each scrollable axis to use a different bounce mode.

## Topics

### Bounce behaviors
- [static var automatic: ScrollBounceBehavior](scrollbouncebehavior/automatic.md)
  The automatic behavior.
- [static var always: ScrollBounceBehavior](scrollbouncebehavior/always.md)
  The scrollable view always bounces.
- [static var basedOnSize: ScrollBounceBehavior](scrollbouncebehavior/basedonsize.md)
  The scrollable view bounces when its content is large enough to require scrolling.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [func scrollBounceBehavior(ScrollBounceBehavior, axes: Axis.Set) -> some View](view/scrollbouncebehavior(_:axes:).md)
  Configures the bounce behavior of scrollable views along the specified axis.
- [var horizontalScrollBounceBehavior: ScrollBounceBehavior](environmentvalues/horizontalscrollbouncebehavior.md)
  The scroll bounce mode for the horizontal axis of scrollable views.
- [var verticalScrollBounceBehavior: ScrollBounceBehavior](environmentvalues/verticalscrollbouncebehavior.md)
  The scroll bounce mode for the vertical axis of scrollable views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scrollbouncebehavior)*
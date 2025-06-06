# verticalScrollBounceBehavior

**Framework**: SwiftUI  
**Kind**: property

The scroll bounce mode for the vertical axis of scrollable views.

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
var verticalScrollBounceBehavior: ScrollBounceBehavior { get set }
```

#### Discussion

Use the [`scrollBounceBehavior(_:axes:)`](view/scrollbouncebehavior(_:axes:).md) view modifier to set this value in the [`Environment`](environment.md).

## See Also

- [func scrollBounceBehavior(ScrollBounceBehavior, axes: Axis.Set) -> some View](view/scrollbouncebehavior(_:axes:).md)
  Configures the bounce behavior of scrollable views along the specified axis.
- [var horizontalScrollBounceBehavior: ScrollBounceBehavior](environmentvalues/horizontalscrollbouncebehavior.md)
  The scroll bounce mode for the horizontal axis of scrollable views.
- [struct ScrollBounceBehavior](scrollbouncebehavior.md)
  The ways that a scrollable view can bounce when it reaches the end of its content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/verticalscrollbouncebehavior)*
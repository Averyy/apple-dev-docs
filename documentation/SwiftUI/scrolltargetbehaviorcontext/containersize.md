# containerSize

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

The size of the container of the scrollable view.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
var containerSize: CGSize { get }
```

#### Discussion

This is the size of the bounds of the scroll view subtracting any insets applied to the scroll view (like the safe area).

## See Also

### Getting the scroll target behavior context
- [var axes: Axis.Set](./axes.md)
  The axes in which the scrollable view is scrollable.
- [var contentSize: CGSize](./contentsize.md)
  The size of the content of the scrollable view.
- [var originalTarget: ScrollTarget](./originaltarget.md)
  The original target when the scroll gesture began.
- [var velocity: CGVector](./velocity.md)
  The current velocity of the scrollable view’s scroll gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scrolltargetbehaviorcontext/containersize)*
# BEScrollViewScrollUpdate

**Framework**: BrowserEngineKit  
**Kind**: class

An object that describes a change in a scroll view’s scroll state.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
@MainActor
class BEScrollViewScrollUpdate
```

#### Overview

When a person scrolls a [`BEScrollView`](bescrollview.md), the system calls the view’s delegate’s [`scrollView(_:handle:completion:)`](bescrollviewdelegate/scrollview(_:handle:completion:).md) method with an instance of this class as the `handle` parameter. Your app can continue to receive `BEScrollViewScrollUpdate` objects after the person completes their scroll gesture, as the scroll decelerates.

> ❗ **Important**:  `BEScrollViewScrollUpdate` isn’t thread-safe, and the system reuses the same object for multiple scroll updates. Retrieve all information you need from a scroll update immediately on the main queue before any further processing.

## Topics

### Retrieving scroll state information
- [var timestamp: TimeInterval](bescrollviewscrollupdate/timestamp.md)
  The time at which a scroll update occurs.
- [var phase: BEScrollViewScrollUpdate.Phase](bescrollviewscrollupdate/phase-swift.property.md)
  A value that indicates the scroll update’s position in the scrolling life cycle.
- [BEScrollViewScrollUpdate.Phase](bescrollviewscrollupdate/phase-swift.enum.md)
  Phases in the scroll gesture life cycle.
### Transforming coordinates
- [func location(in: UIView?) -> CGPoint](bescrollviewscrollupdate/location(in:).md)
  Returns the location of the scroll update in the coordinate system of the given view.
- [func translation(in: UIView?) -> CGPoint](bescrollviewscrollupdate/translation(in:).md)
  Returns the scroll displacement in the coordinate system of the view that the update represents.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class BEScrollView](bescrollview.md)
  A scroll view that works with its delegate to handle nesting and customize scroll interactions.
- [protocol BEScrollViewDelegate](bescrollviewdelegate.md)
  A protocol for scroll view delegates to handle scroll updates and DOM nesting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bescrollviewscrollupdate)*
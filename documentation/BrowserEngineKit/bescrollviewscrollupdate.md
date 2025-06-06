# BEScrollViewScrollUpdate

**Framework**: BrowserEngineKit  
**Kind**: class

An object that represents a change in a scroll view’s scroll state.

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

When a person scrolls a [`BEScrollView`](bescrollview.md), the view’s delegate receives the [`scrollView(_:handle:completion:)`](bescrollviewdelegate/scrollview(_:handle:completion:).md) method. The `handle` parameter is an instance of `BEScrollViewScrollUpdate` that describes the scroll activity.

Your app can continue to receive `BEScrollViewScrollUpdate` objects after the person completes their scroll gesture, as the scrolling decelerates.

> ❗ **Important**:  `BEScrollViewScrollUpdate` isn’t thread-safe, and the system uses the same object for multiple scroll updates. When you receive a scroll update, immediately get the information you need on the main queue before any other processing.

 `BEScrollViewScrollUpdate` isn’t thread-safe, and the system uses the same object for multiple scroll updates. When you receive a scroll update, immediately get the information you need on the main queue before any other processing.

## Topics

### Retrieving scroll state information
- [var timestamp: TimeInterval](bescrollviewscrollupdate/timestamp.md)
  The time at which the scroll update occurred.
- [var phase: BEScrollViewScrollUpdate.Phase](bescrollviewscrollupdate/phase-swift.property.md)
  The point in the scrolling lifecycle represented by the scroll update.
- [BEScrollViewScrollUpdate.Phase](bescrollviewscrollupdate/phase-swift.enum.md)
  The phase of a scroll update in a scroll gesture’s lifecycle.
### Transforming coordinates
- [func location(in: UIView?) -> CGPoint](bescrollviewscrollupdate/location(in:).md)
  Returns the coordinates of the scroll update in the given view’s bounds.
- [func translation(in: UIView?) -> CGPoint](bescrollviewscrollupdate/translation(in:).md)
  Returns the amount of scrolling in the scroll update in the given view’s coordinates.

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
  A scroll view that works with its delegate to handle nesting, and customize scroll interactions.
- [protocol BEScrollViewDelegate](bescrollviewdelegate.md)
  The protocol that browser scroll view delegates conform to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bescrollviewscrollupdate)*
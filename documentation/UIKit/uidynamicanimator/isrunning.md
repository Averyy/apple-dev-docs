# isRunning

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Returns true if the dynamic animator is running.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var isRunning: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isRunning) BOOL running;
```

## Discussion

The views associated with an animator’s behaviors can change position or change transform only when the animator is running. For optimization purposes, iOS can pause and then restart an animator. Use this method if you need to check whether or not your views are currently subject to changes in position or transform.

## See Also

### Accessing a dynamic animator’s state
- [var elapsedTime: TimeInterval](./elapsedtime.md)
  Returns the time interval since the dynamic animator started running.
- [var behaviors: [UIDynamicBehavior]](./behaviors.md)
  The dynamic behaviors managed by a dynamic animator.
- [var referenceView: UIView?](./referenceview.md)
  The view that a dynamic animator was initialized with.
- [func updateItem(usingCurrentState: any UIDynamicItem)](./updateitem%28usingcurrentstate%29.md)
  Asks a dynamic animator to read the current state of a dynamic item, replacing the animator’s internal representation of the item’s state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidynamicanimator/isrunning)*
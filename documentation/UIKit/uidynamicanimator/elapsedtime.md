# elapsedTime

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

Returns the time interval since the dynamic animator started running.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var elapsedTime: TimeInterval { get }
```

```objc
@property (nonatomic, readonly) NSTimeInterval elapsedTime;
```

#### Return Value

The elapsed time since the dynamic animator started running.

## See Also

### Accessing a dynamic animator’s state
- [var isRunning: Bool](./isrunning.md)
  Returns true if the dynamic animator is running.
- [var behaviors: [UIDynamicBehavior]](./behaviors.md)
  The dynamic behaviors managed by a dynamic animator.
- [var referenceView: UIView?](./referenceview.md)
  The view that a dynamic animator was initialized with.
- [func updateItem(usingCurrentState: any UIDynamicItem)](./updateitem%28usingcurrentstate%29.md)
  Asks a dynamic animator to read the current state of a dynamic item, replacing the animator’s internal representation of the item’s state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidynamicanimator/elapsedtime)*
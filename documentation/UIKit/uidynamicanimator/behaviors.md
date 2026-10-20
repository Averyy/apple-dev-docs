# behaviors

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The dynamic behaviors managed by a dynamic animator.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var behaviors: [UIDynamicBehavior] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<__kindof UIDynamicBehavior *> * behaviors;
```

## See Also

### Accessing a dynamic animator’s state
- [var elapsedTime: TimeInterval](./elapsedtime.md)
  Returns the time interval since the dynamic animator started running.
- [var isRunning: Bool](./isrunning.md)
  Returns true if the dynamic animator is running.
- [var referenceView: UIView?](./referenceview.md)
  The view that a dynamic animator was initialized with.
- [func updateItem(usingCurrentState: any UIDynamicItem)](./updateitem%28usingcurrentstate%29.md)
  Asks a dynamic animator to read the current state of a dynamic item, replacing the animator’s internal representation of the item’s state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidynamicanimator/behaviors)*
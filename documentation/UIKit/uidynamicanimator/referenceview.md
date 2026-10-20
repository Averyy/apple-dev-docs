# referenceView

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The view that a dynamic animator was initialized with.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var referenceView: UIView? { get }
```

```objc
@property (nonatomic, readonly, nullable) UIView * referenceView;
```

#### Discussion

This property has a value only for a dynamic animator initialized using the [`init(referenceView:)`](./init%28referenceview%29.md) method.

## See Also

### Accessing a dynamic animator’s state
- [var elapsedTime: TimeInterval](./elapsedtime.md)
  Returns the time interval since the dynamic animator started running.
- [var isRunning: Bool](./isrunning.md)
  Returns true if the dynamic animator is running.
- [var behaviors: [UIDynamicBehavior]](./behaviors.md)
  The dynamic behaviors managed by a dynamic animator.
- [func updateItem(usingCurrentState: any UIDynamicItem)](./updateitem%28usingcurrentstate%29.md)
  Asks a dynamic animator to read the current state of a dynamic item, replacing the animator’s internal representation of the item’s state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidynamicanimator/referenceview)*
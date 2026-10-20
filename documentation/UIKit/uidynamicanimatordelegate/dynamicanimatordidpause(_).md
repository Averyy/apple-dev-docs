# dynamicAnimatorDidPause(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Called when a dynamic animator pauses the animations for its behaviors’ associated dynamic items.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
optional func dynamicAnimatorDidPause(_ animator: UIDynamicAnimator)
```

```objc
- (void) dynamicAnimatorDidPause:(UIDynamicAnimator *) animator;
```

## Parameters

- `animator`: The dynamic animator that paused its animation.

## See Also

### Responding to animation pausing and resumption
- [func dynamicAnimatorWillResume(UIDynamicAnimator)](./dynamicanimatorwillresume%28_%29.md)
  Called when a dynamic animator is about to resume the animations for its behaviors’ associated dynamic items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidynamicanimatordelegate/dynamicanimatordidpause(_:))*
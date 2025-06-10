# dynamicAnimatorWillResume(_:)

**Framework**: UIKit  
**Kind**: method

Called when a dynamic animator is about to resume the animations for its behaviors’ associated dynamic items.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func dynamicAnimatorWillResume(_ animator: UIDynamicAnimator)
```

## Parameters

- `animator`: The dynamic animator that is about to resume animation.

## See Also

- [func dynamicAnimatorDidPause(UIDynamicAnimator)](uidynamicanimatordelegate/dynamicanimatordidpause(_:).md)
  Called when a dynamic animator pauses the animations for its behaviors’ associated dynamic items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidynamicanimatordelegate/dynamicanimatorwillresume(_:))*
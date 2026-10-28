# isRemovedOnCompletion

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

Determines if the animation is removed from the target layer’s animations upon completion.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var isRemovedOnCompletion: Bool { get set }
```

```objc
@property (getter=isRemovedOnCompletion) BOOL removedOnCompletion;
```

## Discussion

When [`true`](../../Swift/true.md), the animation is removed from the target layer’s animations once its active duration has passed. Defaults to [`true`](../../Swift/true.md).

## See Also

### Animation Attributes
- [var timingFunction: CAMediaTimingFunction?](./timingfunction.md)
  An optional timing function defining the pacing of the animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caanimation/isremovedoncompletion)*
# isRemovedOnCompletion

**Framework**: Core Animation  
**Kind**: property

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

#### Discussion

When [`true`](https://developer.apple.com/documentation/swift/true), the animation is removed from the target layer’s animations once its active duration has passed. Defaults to [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [var timingFunction: CAMediaTimingFunction?](caanimation/timingfunction.md)
  An optional timing function defining the pacing of the animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caanimation/isremovedoncompletion)*
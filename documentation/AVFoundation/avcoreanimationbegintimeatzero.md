# AVCoreAnimationBeginTimeAtZero

**Framework**: AVFoundation  
**Kind**: var

A value that sets an animation begin time to `0`.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
let AVCoreAnimationBeginTimeAtZero: CFTimeInterval
```

#### Discussion

The constant is a small, non-zero, positive value which prevents CoreAnimation from replacing `0.0` with [`CACurrentMediaTime()`](https://developer.apple.com/documentation/QuartzCore/CACurrentMediaTime()).


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcoreanimationbegintimeatzero)*
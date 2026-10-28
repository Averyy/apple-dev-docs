# timingFunction

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

An optional timing function defining the pacing of the animation.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var timingFunction: CAMediaTimingFunction? { get set }
```

```objc
@property (strong, nullable) CAMediaTimingFunction * timingFunction;
```

## Discussion

Defaults to `nil`, indicating linear pacing.

## See Also

### Animation Attributes
- [var isRemovedOnCompletion: Bool](./isremovedoncompletion.md)
  Determines if the animation is removed from the target layer’s animations upon completion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caanimation/timingfunction)*
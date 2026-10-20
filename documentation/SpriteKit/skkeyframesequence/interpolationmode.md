# interpolationMode

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

The mode used to determine how values for times between the keyframes are calculated.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
var interpolationMode: SKInterpolationMode { get set }
```

```objc
@property (nonatomic) SKInterpolationMode interpolationMode;
```

## Mentions

- [Using Keyframe Sequence to effect Custom Interpolation](../using-keyframe-sequence-to-effect-custom-interpolation.md)

#### Discussion

The possible values are defined in [`SKInterpolationMode`](../skinterpolationmode.md). The default value is [`SKInterpolationMode.linear`](../skinterpolationmode/linear.md).

## See Also

### Interpolation Modifiers
- [var repeatMode: SKRepeatMode](./repeatmode.md)
  The mode used to determine how the keyframe sequence repeats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skkeyframesequence/interpolationmode)*
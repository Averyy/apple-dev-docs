# sample(atTime:)

**Framework**: SpriteKit  
**Kind**: method

Calculates the sample at a particular time.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func sample(atTime time: CGFloat) -> Any?
```

## Mentions

- [Using Keyframe Sequence to effect Custom Interpolation](using-keyframe-sequence-to-effect-custom-interpolation.md)

#### Return Value

An object that contains the interpolated sample. The class of this object matches the class of the values stored in the keyframe sequence — either an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) or an `SKColor`.

## Parameters

- `time`: The time value to sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skkeyframesequence/sample(attime:))*
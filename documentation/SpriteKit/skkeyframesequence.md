# SKKeyframeSequence

**Framework**: SpriteKit  
**Kind**: class  
**Role**: Class

An object that performs interpolation between values specified at different times (keyframes).

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
class SKKeyframeSequence
```

```objc
@interface SKKeyframeSequence : NSObject
```

## Mentions

- [Using Keyframe Sequence to effect Custom Interpolation](./using-keyframe-sequence-to-effect-custom-interpolation.md)
- [Animating Particle Properties Across Disparate Values](./animating-particle-properties-across-disparate-values.md)

## Overview

The primary use for an [`SKKeyframeSequence`](./skkeyframesequence.md) object is to animate properties on particles emitted by an [`SKEmitterNode`](./skemitternode.md) object, but it can also be used for your general interpolation needs across a discrete set of inputs.

When a keyframe sequence is used with an emitter node, particles determine their values by sampling the keyframe sequence. The sequence replaces the normal simulation performed by the emitter node.

## Topics

### First Steps
- [Using Keyframe Sequence to effect Custom Interpolation](./using-keyframe-sequence-to-effect-custom-interpolation.md)
  See a few examples of what keyframe sequence can do.
- [init(keyframeValues: [Any], times: [NSNumber])](./skkeyframesequence/init%28keyframevalues,times%29.md)
  Initializes a keyframe sequence with an initial set of values and times.
- [convenience init(capacity: Int)](./skkeyframesequence/init%28capacity%29.md)
  Initializes a new keyframe sequence.
- [init?(coder: NSCoder)](./skkeyframesequence/init%28coder%29.md)
### Sequence Building
- [func addKeyframeValue(Any, time: CGFloat)](./skkeyframesequence/addkeyframevalue%28_,time%29.md)
  Adds a keyframe to the sequence.
- [func removeKeyframe(at: Int)](./skkeyframesequence/removekeyframe%28at%29.md)
  Removes a keyframe from the sequence.
- [func removeLastKeyframe()](./skkeyframesequence/removelastkeyframe%28%29.md)
  Removes the last value in the sequence.
- [func setKeyframeTime(CGFloat, for: Int)](./skkeyframesequence/setkeyframetime%28_,for%29.md)
  Changes the time for a specific keyframe.
- [func setKeyframeValue(Any, for: Int)](./skkeyframesequence/setkeyframevalue%28_,for%29.md)
  Changes the value for a specific keyframe.
- [func setKeyframeValue(Any, time: CGFloat, for: Int)](./skkeyframesequence/setkeyframevalue%28_,time,for%29.md)
  Replaces a keyframe in the sequence with a new keyframe.
### Sequence Running
- [func sample(atTime: CGFloat) -> Any?](./skkeyframesequence/sample%28attime%29.md)
  Calculates the sample at a particular time.
### Sequence Information
- [func count() -> Int](./skkeyframesequence/count%28%29.md)
  The number of keyframes in the sequence.
- [func getKeyframeTime(for: Int) -> CGFloat](./skkeyframesequence/getkeyframetime%28for%29.md)
  Gets the time for a keyframe in the sequence.
- [func getKeyframeValue(for: Int) -> Any](./skkeyframesequence/getkeyframevalue%28for%29.md)
  Gets the value for a keyframe in the sequence.
### Interpolation Modifiers
- [var interpolationMode: SKInterpolationMode](./skkeyframesequence/interpolationmode.md)
  The mode used to determine how values for times between the keyframes are calculated.
- [var repeatMode: SKRepeatMode](./skkeyframesequence/repeatmode.md)
  The mode used to determine how the keyframe sequence repeats.
### Constants
- [enum SKInterpolationMode](./skinterpolationmode.md)
  The modes used to interpolate between keyframes in the sequence.
- [enum SKRepeatMode](./skrepeatmode.md)
  The modes used to determine how the sequence repeats.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Mathematical Tools
- [class SKRange](./skrange.md)
  A definition of a range of floating-point values.
- [class SKRegion](./skregion.md)
  The definition of an arbitrary area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skkeyframesequence)*
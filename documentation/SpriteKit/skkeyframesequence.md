# SKKeyframeSequence

**Framework**: SpriteKit  
**Kind**: class

An object that performs interpolation between values specified at different times (keyframes).

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
class SKKeyframeSequence
```

## Mentions

- [Using Keyframe Sequence to effect Custom Interpolation](using-keyframe-sequence-to-effect-custom-interpolation.md)
- [Animating Particle Properties Across Disparate Values](animating-particle-properties-across-disparate-values.md)

#### Overview

The primary use for an [`SKKeyframeSequence`](skkeyframesequence.md) object is to animate properties on particles emitted by an [`SKEmitterNode`](skemitternode.md) object, but it can also be used for your general interpolation needs across a discrete set of inputs.

When a keyframe sequence is used with an emitter node, particles determine their values by sampling the keyframe sequence. The sequence replaces the normal simulation performed by the emitter node.

## Topics

### First Steps
- [Using Keyframe Sequence to effect Custom Interpolation](using-keyframe-sequence-to-effect-custom-interpolation.md)
  See a few examples of what keyframe sequence can do.
- [init(keyframeValues: [Any], times: [NSNumber])](skkeyframesequence/init(keyframevalues:times:).md)
  Initializes a keyframe sequence with an initial set of values and times.
- [convenience init(capacity: Int)](skkeyframesequence/init(capacity:).md)
  Initializes a new keyframe sequence.
- [init?(coder: NSCoder)](skkeyframesequence/init(coder:).md)
### Sequence Building
- [func addKeyframeValue(Any, time: CGFloat)](skkeyframesequence/addkeyframevalue(_:time:).md)
  Adds a keyframe to the sequence.
- [func removeKeyframe(at: Int)](skkeyframesequence/removekeyframe(at:).md)
  Removes a keyframe from the sequence.
- [func removeLastKeyframe()](skkeyframesequence/removelastkeyframe.md)
  Removes the last value in the sequence.
- [func setKeyframeTime(CGFloat, for: Int)](skkeyframesequence/setkeyframetime(_:for:).md)
  Changes the time for a specific keyframe.
- [func setKeyframeValue(Any, for: Int)](skkeyframesequence/setkeyframevalue(_:for:).md)
  Changes the value for a specific keyframe.
- [func setKeyframeValue(Any, time: CGFloat, for: Int)](skkeyframesequence/setkeyframevalue(_:time:for:).md)
  Replaces a keyframe in the sequence with a new keyframe.
### Sequence Running
- [func sample(atTime: CGFloat) -> Any?](skkeyframesequence/sample(attime:).md)
  Calculates the sample at a particular time.
### Sequence Information
- [func count() -> Int](skkeyframesequence/count.md)
  The number of keyframes in the sequence.
- [func getKeyframeTime(for: Int) -> CGFloat](skkeyframesequence/getkeyframetime(for:).md)
  Gets the time for a keyframe in the sequence.
- [func getKeyframeValue(for: Int) -> Any](skkeyframesequence/getkeyframevalue(for:).md)
  Gets the value for a keyframe in the sequence.
### Interpolation Modifiers
- [var interpolationMode: SKInterpolationMode](skkeyframesequence/interpolationmode.md)
  The mode used to determine how values for times between the keyframes are calculated.
- [var repeatMode: SKRepeatMode](skkeyframesequence/repeatmode.md)
  The mode used to determine how the keyframe sequence repeats.
### Constants
- [enum SKInterpolationMode](skinterpolationmode.md)
  The modes used to interpolate between keyframes in the sequence.
- [enum SKRepeatMode](skrepeatmode.md)
  The modes used to determine how the sequence repeats.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class SKRange](skrange.md)
  A definition of a range of floating-point values.
- [class SKRegion](skregion.md)
  The definition of an arbitrary area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skkeyframesequence)*
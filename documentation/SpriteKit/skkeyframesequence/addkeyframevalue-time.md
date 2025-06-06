# addKeyframeValue(_:time:)

**Framework**: SpriteKit  
**Kind**: method

Adds a keyframe to the sequence.

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
func addKeyframeValue(_ value: Any, time: CGFloat)
```

#### Discussion

The new keyframe is appended to the end of the array.

## Parameters

- `value`: An object that defines the value to add. It must have the same class as other value objects stored in the sequence.
- `time`: The corresponding time.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skkeyframesequence/addkeyframevalue(_:time:))*
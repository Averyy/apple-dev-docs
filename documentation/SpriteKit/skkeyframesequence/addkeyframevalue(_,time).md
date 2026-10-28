# addKeyframeValue(_:time:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Instance Method

Adds a keyframe to the sequence.

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
func addKeyframeValue(_ value: Any, time: CGFloat)
```

```objc
- (void) addKeyframeValue:(id) value time:(CGFloat) time;
```

## Discussion

The new keyframe is appended to the end of the array.

## Parameters

- `value`: An object that defines the value to add. It must have the same class as other value objects stored in the sequence.
- `time`: The corresponding time.

## See Also

### Sequence Building
- [func removeKeyframe(at: Int)](./removekeyframe%28at%29.md)
  Removes a keyframe from the sequence.
- [func removeLastKeyframe()](./removelastkeyframe%28%29.md)
  Removes the last value in the sequence.
- [func setKeyframeTime(CGFloat, for: Int)](./setkeyframetime%28_,for%29.md)
  Changes the time for a specific keyframe.
- [func setKeyframeValue(Any, for: Int)](./setkeyframevalue%28_,for%29.md)
  Changes the value for a specific keyframe.
- [func setKeyframeValue(Any, time: CGFloat, for: Int)](./setkeyframevalue%28_,time,for%29.md)
  Replaces a keyframe in the sequence with a new keyframe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skkeyframesequence/addkeyframevalue(_:time:))*
# setKeyframeValue(_:for:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Instance Method

Changes the value for a specific keyframe.

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
func setKeyframeValue(_ value: Any, for index: Int)
```

```objc
- (void) setKeyframeValue:(id) value forIndex:(NSUInteger) index;
```

## Parameters

- `value`: The new value for the keyframe.
- `index`: The index of the keyframe to change.

## See Also

### Sequence Building
- [func addKeyframeValue(Any, time: CGFloat)](./addkeyframevalue%28_,time%29.md)
  Adds a keyframe to the sequence.
- [func removeKeyframe(at: Int)](./removekeyframe%28at%29.md)
  Removes a keyframe from the sequence.
- [func removeLastKeyframe()](./removelastkeyframe%28%29.md)
  Removes the last value in the sequence.
- [func setKeyframeTime(CGFloat, for: Int)](./setkeyframetime%28_,for%29.md)
  Changes the time for a specific keyframe.
- [func setKeyframeValue(Any, time: CGFloat, for: Int)](./setkeyframevalue%28_,time,for%29.md)
  Replaces a keyframe in the sequence with a new keyframe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skkeyframesequence/setkeyframevalue(_:for:))*
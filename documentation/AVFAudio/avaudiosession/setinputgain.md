# setInputGain(_:)

**Framework**: AVFAudio  
**Kind**: method

Changes the input gain to the specified value.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func setInputGain(_ gain: Float) throws
```

#### Discussion

Before calling this method, check the value in the [`isInputGainSettable`](avaudiosession/isinputgainsettable.md) property to make sure the input gain level is settable for the current inputs.

## Parameters

- `gain`: The new gain value, which must be in the range   to  , where   represents the lowest gain setting and   represents the highest gain setting.

## See Also

- [var inputGain: Float](avaudiosession/inputgain.md)
  The gain applied to inputs associated with the session.
- [var isInputGainSettable: Bool](avaudiosession/isinputgainsettable.md)
  A Boolean value that indicates whether you can set the input gain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/setinputgain(_:))*
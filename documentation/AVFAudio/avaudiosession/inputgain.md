# inputGain

**Framework**: AVFAudio  
**Kind**: property

The gain applied to inputs associated with the session.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var inputGain: Float { get }
```

#### Discussion

This property returns a floating point value ranging from `0.0` to `1.0`, where `0.0` represents the lowest gain setting, and `1.0` represents the highest gain setting.

You can observe changes to the value of this property by using key-value observing. For more information, see [`Using Key-Value Observing in Swift`](https://developer.apple.com/documentation/Swift/using-key-value-observing-in-swift).

## See Also

- [var isInputGainSettable: Bool](avaudiosession/isinputgainsettable.md)
  A Boolean value that indicates whether you can set the input gain.
- [func setInputGain(Float) throws](avaudiosession/setinputgain(_:).md)
  Changes the input gain to the specified value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/inputgain)*
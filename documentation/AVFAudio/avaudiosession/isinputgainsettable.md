# isInputGainSettable

**Framework**: AVFAudio  
**Kind**: property

A Boolean value that indicates whether you can set the input gain.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var isInputGainSettable: Bool { get }
```

#### Return Value

Returns [`true`](https://developer.apple.com/documentation/swift/true) if the device allows input gain to be changed, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

Not all devices support variable gain; check this property before attempting to set the input gain.

## See Also

- [var inputGain: Float](avaudiosession/inputgain.md)
  The gain applied to inputs associated with the session.
- [func setInputGain(Float) throws](avaudiosession/setinputgain(_:).md)
  Changes the input gain to the specified value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/isinputgainsettable)*
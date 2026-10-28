# isInputGainSettable

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly, getter=isInputGainSettable) BOOL inputGainSettable;
```

## Return Value

Returns [`true`](../../Swift/true.md) if the device allows input gain to be changed, otherwise [`false`](../../Swift/false.md).

## Discussion

Not all devices support variable gain; check this property before attempting to set the input gain.

## See Also

### Setting input gain
- [var inputGain: Float](./inputgain.md)
  The gain applied to inputs associated with the session.
- [func setInputGain(Float) throws](./setinputgain%28_%29.md)
  Changes the input gain to the specified value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/isinputgainsettable)*
# preferredInputNumberOfChannels

**Framework**: AVFAudio  
**Kind**: property

The preferred number of input channels for the current route.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var preferredInputNumberOfChannels: Int { get }
```

#### Discussion

The value of this property indicates the number of channels selected using the [`setPreferredInputNumberOfChannels(_:)`](avaudiosession/setpreferredinputnumberofchannels(_:).md) method.

To determine the actual number of input channels, query the [`inputNumberOfChannels`](avaudiosession/inputnumberofchannels.md) property.

## See Also

- [func setPreferredInputNumberOfChannels(Int) throws](avaudiosession/setpreferredinputnumberofchannels(_:).md)
  Sets the preferred number of input channels for the current route.
- [var inputNumberOfChannels: Int](avaudiosession/inputnumberofchannels.md)
  The number of audio input channels for the current route.
- [var maximumInputNumberOfChannels: Int](avaudiosession/maximuminputnumberofchannels.md)
  The maximum number of input channels available for the current audio route.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/preferredinputnumberofchannels)*
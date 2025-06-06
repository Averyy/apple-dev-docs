# inputNumberOfChannels

**Framework**: AVFAudio  
**Kind**: property

The number of audio input channels for the current route.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var inputNumberOfChannels: Int { get }
```

#### Discussion

You can observe changes to the value of this property by using key-value observing. For more information, see [`Using Key-Value Observing in Swift`](https://developer.apple.com/documentation/Swift/using-key-value-observing-in-swift).

## See Also

- [var preferredInputNumberOfChannels: Int](avaudiosession/preferredinputnumberofchannels.md)
  The preferred number of input channels for the current route.
- [func setPreferredInputNumberOfChannels(Int) throws](avaudiosession/setpreferredinputnumberofchannels(_:).md)
  Sets the preferred number of input channels for the current route.
- [var maximumInputNumberOfChannels: Int](avaudiosession/maximuminputnumberofchannels.md)
  The maximum number of input channels available for the current audio route.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/inputnumberofchannels)*
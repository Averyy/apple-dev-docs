# outputNumberOfChannels

**Framework**: AVFAudio  
**Kind**: property

The number of audio output channels.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var outputNumberOfChannels: Int { get }
```

#### Discussion

You can observe changes to the value of this property using key-value observice. For more information, see [`Using Key-Value Observing in Swift`](https://developer.apple.com/documentation/Swift/using-key-value-observing-in-swift).

## See Also

- [var preferredOutputNumberOfChannels: Int](avaudiosession/preferredoutputnumberofchannels.md)
  The preferred number of output channels for the current route.
- [func setPreferredOutputNumberOfChannels(Int) throws](avaudiosession/setpreferredoutputnumberofchannels(_:).md)
  Sets the preferred number of output channels for the current route.
- [var maximumOutputNumberOfChannels: Int](avaudiosession/maximumoutputnumberofchannels.md)
  The maximum number of output channels available for the current audio route.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/outputnumberofchannels)*
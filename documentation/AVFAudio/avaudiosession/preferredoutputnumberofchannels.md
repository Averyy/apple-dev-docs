# preferredOutputNumberOfChannels

**Framework**: AVFAudio  
**Kind**: property

The preferred number of output channels for the current route.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var preferredOutputNumberOfChannels: Int { get }
```

#### Discussion

The value of this property indicates the preferred number of output channels selected using the [`setPreferredOutputNumberOfChannels(_:)`](avaudiosession/setpreferredoutputnumberofchannels(_:).md) method.

To determine the actual number of channels, query the [`outputNumberOfChannels`](avaudiosession/outputnumberofchannels.md) property.

## See Also

- [func setPreferredOutputNumberOfChannels(Int) throws](avaudiosession/setpreferredoutputnumberofchannels(_:).md)
  Sets the preferred number of output channels for the current route.
- [var outputNumberOfChannels: Int](avaudiosession/outputnumberofchannels.md)
  The number of audio output channels.
- [var maximumOutputNumberOfChannels: Int](avaudiosession/maximumoutputnumberofchannels.md)
  The maximum number of output channels available for the current audio route.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/preferredoutputnumberofchannels)*
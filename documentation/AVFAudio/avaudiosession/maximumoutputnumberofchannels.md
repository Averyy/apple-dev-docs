# maximumOutputNumberOfChannels

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

The maximum number of output channels available for the current audio route.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var maximumOutputNumberOfChannels: Int { get }
```

```objc
@property (readonly) NSInteger maximumOutputNumberOfChannels;
```

## See Also

### Setting the number of output channels
- [var preferredOutputNumberOfChannels: Int](./preferredoutputnumberofchannels.md)
  The preferred number of output channels for the current route.
- [func setPreferredOutputNumberOfChannels(Int) throws](./setpreferredoutputnumberofchannels%28_%29.md)
  Sets the preferred number of output channels for the current route.
- [var outputNumberOfChannels: Int](./outputnumberofchannels.md)
  The number of audio output channels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/maximumoutputnumberofchannels)*
# preferredOutputNumberOfChannels

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly) NSInteger preferredOutputNumberOfChannels;
```

## Discussion

The value of this property indicates the preferred number of output channels selected using the [`setPreferredOutputNumberOfChannels(_:)`](./setpreferredoutputnumberofchannels%28_%29.md) method.

To determine the actual number of channels, query the [`outputNumberOfChannels`](./outputnumberofchannels.md) property.

## See Also

### Setting the number of output channels
- [func setPreferredOutputNumberOfChannels(Int) throws](./setpreferredoutputnumberofchannels%28_%29.md)
  Sets the preferred number of output channels for the current route.
- [var outputNumberOfChannels: Int](./outputnumberofchannels.md)
  The number of audio output channels.
- [var maximumOutputNumberOfChannels: Int](./maximumoutputnumberofchannels.md)
  The maximum number of output channels available for the current audio route.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/preferredoutputnumberofchannels)*
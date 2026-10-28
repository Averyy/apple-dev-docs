# preferredInputNumberOfChannels

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly) NSInteger preferredInputNumberOfChannels;
```

## Discussion

The value of this property indicates the number of channels selected using the [`setPreferredInputNumberOfChannels(_:)`](./setpreferredinputnumberofchannels%28_%29.md) method.

To determine the actual number of input channels, query the [`inputNumberOfChannels`](./inputnumberofchannels.md) property.

## See Also

### Setting the number of input channels
- [func setPreferredInputNumberOfChannels(Int) throws](./setpreferredinputnumberofchannels%28_%29.md)
  Sets the preferred number of input channels for the current route.
- [var inputNumberOfChannels: Int](./inputnumberofchannels.md)
  The number of audio input channels for the current route.
- [var maximumInputNumberOfChannels: Int](./maximuminputnumberofchannels.md)
  The maximum number of input channels available for the current audio route.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/preferredinputnumberofchannels)*
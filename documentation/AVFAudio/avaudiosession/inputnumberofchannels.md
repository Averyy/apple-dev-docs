# inputNumberOfChannels

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly) NSInteger inputNumberOfChannels;
```

## Discussion

You can observe changes to the value of this property by using key-value observing. For more information, see [Using Key-Value Observing in Swift](../../Swift/using-key-value-observing-in-swift.md).

## See Also

### Setting the number of input channels
- [var preferredInputNumberOfChannels: Int](./preferredinputnumberofchannels.md)
  The preferred number of input channels for the current route.
- [func setPreferredInputNumberOfChannels(Int) throws](./setpreferredinputnumberofchannels%28_%29.md)
  Sets the preferred number of input channels for the current route.
- [var maximumInputNumberOfChannels: Int](./maximuminputnumberofchannels.md)
  The maximum number of input channels available for the current audio route.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/inputnumberofchannels)*
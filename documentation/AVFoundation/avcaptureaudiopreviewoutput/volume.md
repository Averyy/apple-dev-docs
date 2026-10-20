# volume

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The output volume of the audio preview.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var volume: Float { get set }
```

```objc
@property (nonatomic) float volume;
```

#### Discussion

A value of `1.0` indicates maximum volume, and a value of `0.0` mutes the audio preview.

## See Also

### Configuring the output
- [var outputDeviceUniqueID: String?](./outputdeviceuniqueid.md)
  The unique identifier of the Core Audio output device to use for audio preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureaudiopreviewoutput/volume)*
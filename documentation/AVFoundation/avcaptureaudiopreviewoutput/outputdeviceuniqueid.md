# outputDeviceUniqueID

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The unique identifier of the Core Audio output device to use for audio preview.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var outputDeviceUniqueID: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * outputDeviceUniqueID;
```

## Discussion

Set the value to the unique identifier of the audio output device, or `nil` to use default system output.

## See Also

### Configuring the output
- [var volume: Float](./volume.md)
  The output volume of the audio preview.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureaudiopreviewoutput/outputdeviceuniqueid)*
# highQualityRecording

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

Describes whether this port supports Bluetooth high-quality recording.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
var highQualityRecording: AVAudioSessionCapability { get }
```

```objc
@property (nonatomic, strong, readonly, nonnull) AVAudioSessionCapability * highQualityRecording;
```

#### Discussion

Please see [`bluetoothHighQualityRecording`](../avaudiosession/categoryoptions-swift.struct/bluetoothhighqualityrecording.md) for details.

## See Also

### Inspecting the port extension
- [var farFieldCapture: AVAudioSessionCapability](./farfieldcapture.md)
  Describes whether this port supports far-field input capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosessionportextensionbluetoothmicrophone/highqualityrecording)*
# mode

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

The current audio session’s mode.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var mode: AVAudioSession.Mode { get }
```

```objc
@property (readonly) AVAudioSessionMode mode;
```

## Discussion

The audio session mode, together with the audio session category, indicates to the system how you intend to use audio in your app. You can use a mode to configure the audio system for specific use cases such as video recording, voice or video chat, or audio analysis.

[`AVAudioSession.Mode`](./mode-swift.struct.md) discusses the values available for this property. The default value is [`default`](./mode-swift.struct/default.md).

## See Also

### Inspecting mode configuration
- [var availableModes: [AVAudioSession.Mode]](./availablemodes.md)
  The audio session modes available on the device.
- [AVAudioSession.Mode](./mode-swift.struct.md)
  Audio session mode identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/mode-swift.property)*
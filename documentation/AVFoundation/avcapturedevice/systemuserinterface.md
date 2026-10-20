# AVCaptureDevice.SystemUserInterface

**Framework**: AVFoundation  
**Kind**: enum  
**Role**: Enumeration

Constants that describe the capture device configuration user interfaces.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+

## Declaration

```swift
enum SystemUserInterface
```

```c
enum AVCaptureSystemUserInterface : NSInteger;
```

## Topics

### User interfaces
- [AVCaptureDevice.SystemUserInterface.videoEffects](./systemuserinterface/videoeffects.md)
  The system user interface for changing the state of video effects.
- [AVCaptureDevice.SystemUserInterface.microphoneModes](./systemuserinterface/microphonemodes.md)
  The system user interface for selecting microphone modes.
### Initializers
- [init?(rawValue: Int)](./systemuserinterface/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Presenting the configuration user interface
- [class func showSystemUserInterface(AVCaptureDevice.SystemUserInterface)](./showsystemuserinterface%28_%29.md)
  Displays the system’s user interface to configure video effects or microphone modes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/systemuserinterface)*
# preferredExtension

**Framework**: ReplayKit  
**Kind**: property  
**Role**: Instance Property

A bundle identifier of a broadcast extension.

**Availability**:
- iOS 12.0+ - Deprecated in 27.0
- iPadOS 12.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use ScreenCaptureKit SCContentSharingPicker instead

## Declaration

```swift
var preferredExtension: String? { get set }
```

```objc
@property (nonatomic, strong, nullable) NSString * preferredExtension;
```

## Discussion

Set this property to the bundle identifier of a broadcast extension to show only that broadcast provider in the broadcast picker. Set the property to `nil`, which is the default value, to show all broadcast providers available on the device.

## See Also

### Configuring the Broadcast Picker
- [var showsMicrophoneButton: Bool](./showsmicrophonebutton.md)
  A Boolean value that indicates whether the microphone button is visible in the broadcast picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpsystembroadcastpickerview/preferredextension)*
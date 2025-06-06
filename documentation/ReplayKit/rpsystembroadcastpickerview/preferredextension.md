# preferredExtension

**Framework**: ReplayKit  
**Kind**: property

A bundle identifier of a broadcast extension.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var preferredExtension: String? { get set }
```

#### Discussion

Set this property to the bundle identifier of a broadcast extension to show only that broadcast provider in the broadcast picker. Set the property to `nil`, which is the default value, to show all broadcast providers available on the device.

## See Also

- [var showsMicrophoneButton: Bool](rpsystembroadcastpickerview/showsmicrophonebutton.md)
  A Boolean value that indicates whether the microphone button is visible in the broadcast picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpsystembroadcastpickerview/preferredextension)*
# preferredBroadcastOptions

**Framework**: Group Activities  
**Kind**: property

Preferences for how to present audio and video on the main communication channel.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var preferredBroadcastOptions: BroadcastOptions
```

#### Discussion

Use this property to request special handling of the audio and video on the FaceTime call. For example, you might request video mirroring to simplify activities that involve left-right movement. The system respects your preferences when possible, but may override those preferences if system- or user-specific settings are present. The default value of this property is an empty set.

## See Also

- [var supportsContinuationOnTV: Bool](groupactivitymetadata/supportscontinuationontv.md)
  A Boolean value that indicates whether your app supports activity continuation on an Apple TV.
- [struct BroadcastOptions](broadcastoptions.md)
  Options for how to broadcast media on the shared communications channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupactivitymetadata/preferredbroadcastoptions)*
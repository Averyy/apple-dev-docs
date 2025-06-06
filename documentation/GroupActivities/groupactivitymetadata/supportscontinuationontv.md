# supportsContinuationOnTV

**Framework**: Group Activities  
**Kind**: property

A Boolean value that indicates whether your app supports activity continuation on an Apple TV.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var supportsContinuationOnTV: Bool
```

#### Discussion

The default value of this property is `false`. Set it to `true` to allow participants to continue the activity on Apple TV.

## See Also

- [var preferredBroadcastOptions: BroadcastOptions](groupactivitymetadata/preferredbroadcastoptions.md)
  Preferences for how to present audio and video on the main communication channel.
- [struct BroadcastOptions](broadcastoptions.md)
  Options for how to broadcast media on the shared communications channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupactivitymetadata/supportscontinuationontv)*
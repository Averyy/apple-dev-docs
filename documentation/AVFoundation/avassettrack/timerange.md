# timeRange

**Framework**: AVFoundation  
**Kind**: property

The time range of the track within the overall timeline of the asset.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
var timeRange: CMTimeRange { get }
```

#### Discussion

If the start of the time range is greater than [`zero`](https://developer.apple.com/documentation/CoreMedia/CMTime/zero), the track doesn’t initially have media data to present. This condition may occur when the media delays an audio track to align the start of audio with a specific video frame. You can test for this as the example below shows:


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassettrack/timerange)*
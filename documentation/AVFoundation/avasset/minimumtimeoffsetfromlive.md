# minimumTimeOffsetFromLive

**Framework**: AVFoundation  
**Kind**: property

A time value that indicates how closely playback follows the latest live stream content.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
var minimumTimeOffsetFromLive: CMTime { get }
```

#### Discussion

This property value is only valid when working with live streaming content. For non-live assets, this property value is [`invalid`](https://developer.apple.com/documentation/CoreMedia/CMTime/invalid).


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasset/minimumtimeoffsetfromlive)*
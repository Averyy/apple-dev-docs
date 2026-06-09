# fetchAccessLog(completionHandler:)

**Framework**: AVFoundation  
**Kind**: method

Asynchronously retrieves the access log without blocking the calling thread.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
var accessLog: AVPlayerItemAccessLog? { get async }
```

#### Discussion

An AVPlayerItemAccessLog provides methods to retrieve the network access log in a format suitable for serialization. If nil is returned then there is no logging information currently available for this AVPlayerItem. An AVPlayerItemNewAccessLogEntryNotification will be posted when new logging information becomes available. However, accessLog might already return a non-nil value even before the first notification is posted.

## Parameters

- `completionHandler`: A block that is called with the access log. May be called with nil if no logging information is available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/fetchaccesslog(completionhandler:))*
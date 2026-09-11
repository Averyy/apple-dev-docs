# fetchErrorLog(completionHandler:)

**Framework**: AVFoundation  
**Kind**: method

Asynchronously retrieves the error log without blocking the calling thread.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
nonisolated
var errorLog: AVPlayerItemErrorLog? { get async }
```

#### Discussion

An AVPlayerItemErrorLog provides methods to retrieve the error log in a format suitable for serialization. If nil is returned then there is no logging information currently available for this AVPlayerItem.

## Parameters

- `completionHandler`: A block that is called with the error log. May be called with nil if no logging information is available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/fetcherrorlog(completionhandler:))*
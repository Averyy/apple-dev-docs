# removeReceiver(_:at:)

**Framework**: AVFoundation  
**Kind**: method

Removes a receiver and its renderer from the synchronizer.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func removeReceiver(_ receiver: sending AVSampleBufferVideoRenderer.Receiver, at time: CMTime) async -> Bool
```

## Parameters

- `receiver`: The receiver to be removed.
- `time`: The time on the timebase’s timeline at which the renderer should be removed. If the time is in the past, the renderer is immediately removed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferrendersynchronizer/removereceiver(_:at:)-3yxub)*
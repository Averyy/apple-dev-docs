# stopRealtimeSampleDelivery(session:)

**Framework**: Media Device  
**Kind**: method  
**Required**: Yes

Called when the extension should stop realtime sample delivery.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
@MainActor
func stopRealtimeSampleDelivery(session: MediaOutputSession)
```

## Mentions

- [Creating a media device extension](creating-a-media-device-extension.md)

## Parameters

- `session`: The session to stop delivering samples for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediadevice/realtimesamplehandling/stoprealtimesampledelivery(session:))*
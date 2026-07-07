# seek(to:tolerance:)

**Framework**: AVKit  
**Kind**: method  
**Required**: Yes

Requests a seek to the specified position.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
@MainActor
func seek(to position: CMTime, tolerance: CMTime)
```

## Parameters

- `position`: The position to seek to.
- `tolerance`: How close to `position` the actual seek must land. Pass `CMTime.zero` for exact frame-accurate seeking or `CMTime.positiveInfinity` for fast approximate seeking.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplaybackuserinterfacetimecontrollable-50vcy/seek(to:tolerance:))*
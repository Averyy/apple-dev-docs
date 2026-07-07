# init(position:hostTime:rate:)

**Framework**: AVKit  
**Kind**: init

Creates a new playback position snapshot.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
init(position: CMTime, hostTime: CMTime, rate: Float)
```

#### Return Value

A new playback position snapshot.

## Parameters

- `position`: The playback position at `hostTime`.
- `hostTime`: The mach host time at which `position` was accurate.
- `rate`: The rate of position advancement at the time of the snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplaybackuserinterfaceplaybackposition/init(position:hosttime:rate:))*
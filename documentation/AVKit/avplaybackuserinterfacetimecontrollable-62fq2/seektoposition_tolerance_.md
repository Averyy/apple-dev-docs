# seekToPosition:tolerance:

**Framework**: AVKit  
**Kind**: method  
**Role**: Instance Method

Requests a seek to the specified position.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```objc
- (void) seekToPosition:(CMTime) position tolerance:(CMTime) tolerance;
```

## Parameters

- `position`: The position to seek to.
- `tolerance`: How close to `position` the actual seek must land. Pass `kCMTimeZero` for exact frame-accurate seeking or `kCMTimePositiveInfinity` for fast approximate seeking.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplaybackuserinterfacetimecontrollable-62fq2/seektoposition:tolerance:)*
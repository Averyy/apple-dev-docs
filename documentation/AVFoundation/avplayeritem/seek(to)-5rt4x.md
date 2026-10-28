# seek(to:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Sets the current playback time to the time specified by the date object.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

> **Deprecated**: Use [`seek(to:completionHandler:)`](./seek%28to,completionhandler%29-1dibq.md) instead.

## Declaration

```swift
nonisolated
func seek(to date: Date) async -> Bool
```

## Return Value

[`true`](../../Swift/true.md) if the playhead was moved to `date`, otherwise [`false`](../../Swift/false.md).

## Discussion

For playback content that is associated with a range of dates, this method moves the playhead to point within that range. This method will fail (return [`false`](../../Swift/false.md)) if `date` is outside the range or if the content is not associated with a range of dates.

## Parameters

- `date`: The time to which to seek.

## See Also

### Related Documentation
- [func seek(to: CMTime, toleranceBefore: CMTime, toleranceAfter: CMTime, completionHandler: ((Bool) -> Void)?)](./seek%28to,tolerancebefore,toleranceafter,completionhandler%29.md)
  Sets the current playback time within a specified time bound and invokes the specified block when the seek operation completes or is interrupted.
- [func seek(to: CMTime, completionHandler: ((Bool) -> Void)?)](./seek%28to,completionhandler%29-91gnw.md)
  Sets the current playback time to the specified time.
### Seeking through media
- [func seek(to: CMTime)](./seek%28to%29-1dpto.md)
  Sets the current playback time to the specified time.
- [func seek(to: CMTime, toleranceBefore: CMTime, toleranceAfter: CMTime)](./seek%28to,tolerancebefore,toleranceafter%29.md)
  Sets the current playback time within a specified time bound.
- [func seek(to: Date) -> Bool](./seek%28to%29-3s9d8.md)
  Sets the current playback time to the time specified by the date object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/seek(to:)-5rt4x)*
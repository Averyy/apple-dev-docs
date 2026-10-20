# seek(to:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Sets the current playback time to the time specified by the date object.

**Availability**:
- iOS 4.0+ - Deprecated in 11.0
- iPadOS 4.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.7+ - Deprecated in 10.13
- tvOS 9.0+ - Deprecated in 11.0

> **Deprecated**: Use [`seek(to:completionHandler:)`](./seek%28to,completionhandler%29-1dibq.md) instead.

## Declaration

```swift
@MainActor
func seek(to date: Date) -> Bool
```

```objc
- (BOOL) seekToDate:(NSDate *) date;
```

#### Return Value

[`true`](../../Swift/true.md) if the playhead was moved to `date`, otherwise [`false`](../../Swift/false.md).

#### Discussion

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
- [func seek(to: Date) async -> Bool](./seek%28to%29-5rt4x.md)
  Sets the current playback time to the time specified by the date object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/seek(to:)-3s9d8)*
# seek(to:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Requests that the player seek to a specified date.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
nonisolated
func seek(to date: Date)
```

```objc
- (void) seekToDate:(NSDate *) date;
```

## Discussion

The time to which the player seeks may differ from the specified `date` for efficiency. For sample accurate seeking see [`seek(to:toleranceBefore:toleranceAfter:)`](./seek%28to,tolerancebefore,toleranceafter%29.md).

## Parameters

- `date`: The time to which to seek.

## See Also

### Seeking through media
- [func seek(to: CMTime)](./seek%28to%29-87h2r.md)
  Requests that the player seek to a specified time.
- [func seek(to: CMTime, completionHandler: (Bool) -> Void)](./seek%28to,completionhandler%29-75bls.md)
  Requests that the player seek to a specified time, and to notify you when the seek is complete.
- [func seek(to: CMTime, toleranceBefore: CMTime, toleranceAfter: CMTime)](./seek%28to,tolerancebefore,toleranceafter%29.md)
  Requests that the player seek to a specified time with the amount of accuracy specified by the time tolerance values.
- [func seek(to: CMTime, toleranceBefore: CMTime, toleranceAfter: CMTime, completionHandler: (Bool) -> Void)](./seek%28to,tolerancebefore,toleranceafter,completionhandler%29.md)
  Requests that the player seek to a specified time with the amount of accuracy specified by the time tolerance values, and to notify you when the seek is complete.
- [func seek(to: Date, completionHandler: (Bool) -> Void)](./seek%28to,completionhandler%29-wr1l.md)
  Requests that the player seek to a specified date, and to notify you when the seek is complete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/seek(to:)-9h9qr)*
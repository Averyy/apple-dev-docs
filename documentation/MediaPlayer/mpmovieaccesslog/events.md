# events

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

The events in the movie access log.

**Availability**:
- iOS 3.2+ - Deprecated in 9.0
- iPadOS 3.2+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use AVPlayerViewController in AVKit

## Declaration

```swift
var events: [Any]! { get }
```

```objc
@property (nonatomic, readonly) NSArray * events;
```

## Discussion

An ordered collection of [`MPMovieAccessLogEvent`](../mpmovieaccesslogevent.md) instances that represent the chronological sequence of events in the movie access log.

## See Also

### Movie access log properties
- [var extendedLogData: Data!](./extendedlogdata.md)
  A textual version of the web server access log for the associated movie player.
- [var extendedLogDataStringEncoding: UInt](./extendedlogdatastringencoding.md)
  The string encoding for the [`extendedLogData`](./extendedlogdata.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmovieaccesslog/events)*
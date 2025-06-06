# events

**Framework**: Media Player  
**Kind**: property

The events in the movie access log.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+

## Declaration

```swift
var events: [Any]! { get }
```

#### Discussion

An ordered collection of [`MPMovieAccessLogEvent`](mpmovieaccesslogevent.md) instances that represent the chronological sequence of events in the movie access log.

## See Also

- [var extendedLogData: Data!](mpmovieaccesslog/extendedlogdata.md)
  A textual version of the web server access log for the associated movie player.
- [var extendedLogDataStringEncoding: UInt](mpmovieaccesslog/extendedlogdatastringencoding.md)
  The string encoding for the [`extendedLogData`](mpmovieaccesslog/extendedlogdata.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmovieaccesslog/events)*
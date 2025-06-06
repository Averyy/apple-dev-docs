# events

**Framework**: Media Player  
**Kind**: property

The events in the movie error log.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+

## Declaration

```swift
var events: [Any]! { get }
```

#### Discussion

An ordered collection of [`MPMovieErrorLogEvent`](mpmovieerrorlogevent.md) instances that represent the chronological sequence of events in the movie error log.

## See Also

- [var extendedLogData: Data!](mpmovieerrorlog/extendedlogdata.md)
  A textual version of the web server error log.
- [var extendedLogDataStringEncoding: UInt](mpmovieerrorlog/extendedlogdatastringencoding.md)
  The string encoding for the extended log data property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmovieerrorlog/events)*
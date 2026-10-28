# events

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

The events in the movie error log.

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

An ordered collection of [`MPMovieErrorLogEvent`](../mpmovieerrorlogevent.md) instances that represent the chronological sequence of events in the movie error log.

## See Also

### Movie error log properties
- [var extendedLogData: Data!](./extendedlogdata.md)
  A textual version of the web server error log.
- [var extendedLogDataStringEncoding: UInt](./extendedlogdatastringencoding.md)
  The string encoding for the extended log data property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmovieerrorlog/events)*
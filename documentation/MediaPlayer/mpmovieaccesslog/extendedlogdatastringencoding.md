# extendedLogDataStringEncoding

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

The string encoding for the [`extendedLogData`](./extendedlogdata.md) property.

**Availability**:
- iOS 3.2+ - Deprecated in 9.0
- iPadOS 3.2+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use AVPlayerViewController in AVKit

## Declaration

```swift
var extendedLogDataStringEncoding: UInt { get }
```

```objc
@property (nonatomic, readonly) NSStringEncoding extendedLogDataStringEncoding;
```

#### Discussion

For possible string encodings, see String_Encodings.

## See Also

### Movie access log properties
- [var extendedLogData: Data!](./extendedlogdata.md)
  A textual version of the web server access log for the associated movie player.
- [var events: [Any]!](./events.md)
  The events in the movie access log.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmovieaccesslog/extendedlogdatastringencoding)*
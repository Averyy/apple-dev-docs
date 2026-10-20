# extendedLogData

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

A textual version of the web server error log.

**Availability**:
- iOS 3.2+ - Deprecated in 9.0
- iPadOS 3.2+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use AVPlayerViewController in AVKit

## Declaration

```swift
var extendedLogData: Data! { get }
```

```objc
@property (nonatomic, readonly) NSData * extendedLogData;
```

#### Discussion

The web server error log in a textual format that conforms to the W3C Extended Log File Format for web server log files.

## See Also

### Movie error log properties
- [var extendedLogDataStringEncoding: UInt](./extendedlogdatastringencoding.md)
  The string encoding for the extended log data property.
- [var events: [Any]!](./events.md)
  The events in the movie error log.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmovieerrorlog/extendedlogdata)*
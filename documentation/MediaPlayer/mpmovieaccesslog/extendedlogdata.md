# extendedLogData

**Framework**: Media Player  
**Kind**: property

A textual version of the web server access log for the associated movie player.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+

## Declaration

```swift
var extendedLogData: Data! { get }
```

#### Discussion

The web server access log in a textual format that conforms to the W3C Extended Log File Format for web server log files. For more information, see [`http://www.w3.org/pub/WWW/TR/WD-logfile.html`](https://developer.apple.comhttp://www.w3.org/pub/WWW/TR/WD-logfile.html).

## See Also

- [var extendedLogDataStringEncoding: UInt](mpmovieaccesslog/extendedlogdatastringencoding.md)
  The string encoding for the [`extendedLogData`](mpmovieaccesslog/extendedlogdata.md) property.
- [var events: [Any]!](mpmovieaccesslog/events.md)
  The events in the movie access log.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmovieaccesslog/extendedlogdata)*
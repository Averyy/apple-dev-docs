# extendedLogData()

**Framework**: AVFoundation  
**Kind**: method

Returns a serialized representation of the error log in the Extended Log File Format.

**Availability**:
- iOS 4.3+
- iPadOS 4.3+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func extendedLogData() -> Data?
```

#### Return Value

A serialized representation of the error log in the Extended Log File Format.

#### Discussion

This method converts the web server error log into a textual format that conforms to the W3C Extended Log File Format for web server log files. For more information, see [`http://www.w3.org/pub/WWW/TR/WD-logfile.html`](https://developer.apple.comhttp://www.w3.org/pub/WWW/TR/WD-logfile.html).

You can generate a string suitable for console output using:

```objc
[[NSString alloc] initWithData:[myLog extendedLogData] encoding:[myLog extendedLogDataStringEncoding]]
```

## See Also

- [var events: [AVPlayerItemErrorLogEvent]](avplayeritemerrorlog/events.md)
  A chronologically ordered array of player item error log event objects.
- [var extendedLogDataStringEncoding: UInt](avplayeritemerrorlog/extendedlogdatastringencoding.md)
  The string encoding of the extended log data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemerrorlog/extendedlogdata())*
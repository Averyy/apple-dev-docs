# AVPlayerItemErrorLogEvent

**Framework**: AVFoundation  
**Kind**: class

A single item in a player item’s error log.

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
class AVPlayerItemErrorLogEvent
```

#### Overview

This object provides properties for accessing the data fields of each log event. Each event is a single entry in an [`AVPlayerItem`](avplayeritem.md) object’s error log.

These properties aren’t observable. For more information about key-value observing, see [`Using Key-Value Observing in Swift`](https://developer.apple.com/documentation/Swift/using-key-value-observing-in-swift).

## Topics

### Getting information about the event
- [var date: Date?](avplayeritemerrorlogevent/date.md)
  The date and time when the error occurred.
- [var uri: String?](avplayeritemerrorlogevent/uri.md)
  The URI of the playback item that had an error.
- [var serverAddress: String?](avplayeritemerrorlogevent/serveraddress.md)
  The IP address of the server that was the source of the error.
- [var playbackSessionID: String?](avplayeritemerrorlogevent/playbacksessionid.md)
  A GUID that identifies the playback session that had an error.
- [var errorStatusCode: Int](avplayeritemerrorlogevent/errorstatuscode.md)
  A unique error code identifier.
- [var errorDomain: String](avplayeritemerrorlogevent/errordomain.md)
  The domain of the error.
- [var errorComment: String?](avplayeritemerrorlogevent/errorcomment.md)
  A description of the error encountered.
- [var allHTTPResponseHeaderFields: [String : String]?](avplayeritemerrorlogevent/allhttpresponseheaderfields.md)
  The HTTP header fields the server returns.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func accessLog() -> AVPlayerItemAccessLog?](avplayeritem/accesslog.md)
  Returns an object that represents a snapshot of the network access log.
- [class AVPlayerItemAccessLog](avplayeritemaccesslog.md)
  An object used to retrieve the access log associated with a player item.
- [class AVPlayerItemAccessLogEvent](avplayeritemaccesslogevent.md)
  A single entry in a player item’s access log.
- [func errorLog() -> AVPlayerItemErrorLog?](avplayeritem/errorlog.md)
  Returns an object that represents a snapshot of the error log.
- [class AVPlayerItemErrorLog](avplayeritemerrorlog.md)
  The error log associated with a player item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemerrorlogevent)*
# date

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

The date and time when the error occurred.

**Availability**:
- iOS 3.2+ - Deprecated in 9.0
- iPadOS 3.2+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use AVPlayerViewController in AVKit

## Declaration

```swift
var date: Date! { get }
```

```objc
@property (nonatomic, readonly) NSDate * date;
```

## See Also

### Movie error log event properties
- [var uri: String!](./uri.md)
  The URI of the item playing when the error occurred.
- [var serverAddress: String!](./serveraddress.md)
  The IP address of the web server that was the source of the error.
- [var playbackSessionID: String!](./playbacksessionid.md)
  A globally unique identifier (GUID) for the playback session.
- [var errorStatusCode: Int](./errorstatuscode.md)
  A unique error code identifier.
- [var errorDomain: String!](./errordomain.md)
  The network domain of the error.
- [var errorComment: String!](./errorcomment.md)
  A description of the error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmovieerrorlogevent/date)*
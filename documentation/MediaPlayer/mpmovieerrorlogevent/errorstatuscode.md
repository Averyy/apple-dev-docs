# errorStatusCode

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

A unique error code identifier.

**Availability**:
- iOS 3.2+ - Deprecated in 9.0
- iPadOS 3.2+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use AVPlayerViewController in AVKit

## Declaration

```swift
var errorStatusCode: Int { get }
```

```objc
@property (nonatomic, readonly) NSInteger errorStatusCode;
```

## Discussion

If the error is unknown, the value of this property is negative.

## See Also

### Movie error log event properties
- [var date: Date!](./date.md)
  The date and time when the error occurred.
- [var uri: String!](./uri.md)
  The URI of the item playing when the error occurred.
- [var serverAddress: String!](./serveraddress.md)
  The IP address of the web server that was the source of the error.
- [var playbackSessionID: String!](./playbacksessionid.md)
  A globally unique identifier (GUID) for the playback session.
- [var errorDomain: String!](./errordomain.md)
  The network domain of the error.
- [var errorComment: String!](./errorcomment.md)
  A description of the error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmovieerrorlogevent/errorstatuscode)*
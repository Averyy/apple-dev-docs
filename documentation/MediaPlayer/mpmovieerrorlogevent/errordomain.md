# errorDomain

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

The network domain of the error.

**Availability**:
- iOS 3.2+ - Deprecated in 9.0
- iPadOS 3.2+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use AVPlayerViewController in AVKit

## Declaration

```swift
var errorDomain: String! { get }
```

```objc
@property (nonatomic, readonly) NSString * errorDomain;
```

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
- [var errorStatusCode: Int](./errorstatuscode.md)
  A unique error code identifier.
- [var errorComment: String!](./errorcomment.md)
  A description of the error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmovieerrorlogevent/errordomain)*
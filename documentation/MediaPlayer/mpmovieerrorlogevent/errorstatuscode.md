# errorStatusCode

**Framework**: Media Player  
**Kind**: property

A unique error code identifier.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+

## Declaration

```swift
var errorStatusCode: Int { get }
```

#### Discussion

If the error is unknown, the value of this property is negative.

## See Also

- [var date: Date!](mpmovieerrorlogevent/date.md)
  The date and time when the error occurred.
- [var uri: String!](mpmovieerrorlogevent/uri.md)
  The URI of the item playing when the error occurred.
- [var serverAddress: String!](mpmovieerrorlogevent/serveraddress.md)
  The IP address of the web server that was the source of the error.
- [var playbackSessionID: String!](mpmovieerrorlogevent/playbacksessionid.md)
  A globally unique identifier (GUID) for the playback session.
- [var errorDomain: String!](mpmovieerrorlogevent/errordomain.md)
  The network domain of the error.
- [var errorComment: String!](mpmovieerrorlogevent/errorcomment.md)
  A description of the error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpmovieerrorlogevent/errorstatuscode)*
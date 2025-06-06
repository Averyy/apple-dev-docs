# uri

**Framework**: AVFoundation  
**Kind**: property

The URI of the playback item that had an error.

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
var uri: String? { get }
```

#### Discussion

The property corresponds to “uri”.

The value of this property may be `nil` if the URI is unknown.

## See Also

- [var date: Date?](avplayeritemerrorlogevent/date.md)
  The date and time when the error occurred.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemerrorlogevent/uri)*
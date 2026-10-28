# errorStatusCode

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A unique error code identifier.

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
var errorStatusCode: Int { get }
```

```objc
@property (nonatomic, readonly) NSInteger errorStatusCode;
```

## Discussion

The property corresponds to “status”.

## See Also

### Getting information about the event
- [var date: Date?](./date.md)
  The date and time when the error occurred.
- [var uri: String?](./uri.md)
  The URI of the playback item that had an error.
- [var serverAddress: String?](./serveraddress.md)
  The IP address of the server that was the source of the error.
- [var playbackSessionID: String?](./playbacksessionid.md)
  A GUID that identifies the playback session that had an error.
- [var errorDomain: String](./errordomain.md)
  The domain of the error.
- [var errorComment: String?](./errorcomment.md)
  A description of the error encountered.
- [var allHTTPResponseHeaderFields: [String : String]?](./allhttpresponseheaderfields.md)
  The HTTP header fields the server returns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemerrorlogevent/errorstatuscode)*
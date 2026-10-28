# errorDomain

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The domain of the error.

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
var errorDomain: String { get }
```

```objc
@property (nonatomic, readonly) NSString * errorDomain;
```

## Discussion

The property corresponds to “domain”.

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
- [var errorStatusCode: Int](./errorstatuscode.md)
  A unique error code identifier.
- [var errorComment: String?](./errorcomment.md)
  A description of the error encountered.
- [var allHTTPResponseHeaderFields: [String : String]?](./allhttpresponseheaderfields.md)
  The HTTP header fields the server returns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemerrorlogevent/errordomain)*
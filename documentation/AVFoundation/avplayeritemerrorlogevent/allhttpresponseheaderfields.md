# allHTTPResponseHeaderFields

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The HTTP header fields the server returns.

**Availability**:
- iOS 17.5+
- iPadOS 17.5+
- Mac Catalyst 17.5+
- macOS 14.5+
- tvOS 17.5+
- visionOS 1.2+
- watchOS 10.5+

## Declaration

```swift
var allHTTPResponseHeaderFields: [String : String]? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSDictionary<NSString *,NSString *> * allHTTPResponseHeaderFields;
```

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
- [var errorDomain: String](./errordomain.md)
  The domain of the error.
- [var errorComment: String?](./errorcomment.md)
  A description of the error encountered.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemerrorlogevent/allhttpresponseheaderfields)*
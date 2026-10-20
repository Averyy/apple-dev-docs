# uri

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The URI of the playback item.

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

```objc
@property (nonatomic, readonly, nullable) NSString * URI;
```

#### Discussion

The property corresponds to “uri”.

The value of this property is `nil` if the URI is unknown.

This property is not compatible with key-value observing.

## See Also

### Getting server-related log events
- [var serverAddress: String?](./serveraddress.md)
  The IP address of the server that was the source of the last delivered media segment.
- [var numberOfServerAddressChanges: Int](./numberofserveraddresschanges.md)
  A count of changes to the server address over the last uninterrupted period of playback.
- [var mediaRequestsWWAN: Int](./mediarequestswwan.md)
  The number of network read requests over a WWAN.
- [var transferDuration: TimeInterval](./transferduration.md)
  The accumulated duration, in seconds, of active network transfer of bytes.
- [var numberOfBytesTransferred: Int64](./numberofbytestransferred.md)
  The accumulated number of bytes transferred by the item.
- [var numberOfMediaRequests: Int](./numberofmediarequests.md)
  The number of media read requests from the server to this client.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/uri)*
# numberOfBytesTransferred

**Framework**: AVFoundation  
**Kind**: property

The accumulated number of bytes transferred by the item.

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
var numberOfBytesTransferred: Int64 { get }
```

#### Discussion

The property corresponds to “bytes”.

The value of this property is negative if unknown.

This property is not compatible with key-value observing.

## See Also

- [var uri: String?](avplayeritemaccesslogevent/uri.md)
  The URI of the playback item.
- [var serverAddress: String?](avplayeritemaccesslogevent/serveraddress.md)
  The IP address of the server that was the source of the last delivered media segment.
- [var numberOfServerAddressChanges: Int](avplayeritemaccesslogevent/numberofserveraddresschanges.md)
  A count of changes to the server address over the last uninterrupted period of playback.
- [var mediaRequestsWWAN: Int](avplayeritemaccesslogevent/mediarequestswwan.md)
  The number of network read requests over a WWAN.
- [var transferDuration: TimeInterval](avplayeritemaccesslogevent/transferduration.md)
  The accumulated duration, in seconds, of active network transfer of bytes.
- [var numberOfMediaRequests: Int](avplayeritemaccesslogevent/numberofmediarequests.md)
  The number of media read requests from the server to this client.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritemaccesslogevent/numberofbytestransferred)*
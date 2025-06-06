# countOfBytesClientExpectsToReceive

**Framework**: Foundation  
**Kind**: property

A best-guess upper bound on the number of bytes the client expects to receive.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var countOfBytesClientExpectsToReceive: Int64 { get set }
```

## Mentions

- [Downloading files in the background](downloading-files-in-the-background.md)

#### Discussion

The value set for this property should account for the size of both HTTP response headers and the response body. If no value is specified, the system uses [`NSURLSessionTransferSizeUnknown`](nsurlsessiontransfersizeunknown.md) instead. This property is used by the system to optimize the scheduling of URL session tasks. Developers are strongly encouraged to provide an approximate upper bound, or an exact byte count, if possible, rather than accept the default.

## See Also

- [var countOfBytesClientExpectsToSend: Int64](urlsessiontask/countofbytesclientexpectstosend.md)
  A best-guess upper bound on the number of bytes the client expects to send.
- [let NSURLSessionTransferSizeUnknown: Int64](nsurlsessiontransfersizeunknown.md)
  The total size of the transfer cannot be determined.
- [var earliestBeginDate: Date?](urlsessiontask/earliestbegindate.md)
  The earliest date at which the network load should begin.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessiontask/countofbytesclientexpectstoreceive)*
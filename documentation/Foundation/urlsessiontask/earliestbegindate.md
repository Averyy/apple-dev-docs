# earliestBeginDate

**Framework**: Foundation  
**Kind**: property

The earliest date at which the network load should begin.

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
var earliestBeginDate: Date? { get set }
```

## Mentions

- [Downloading files in the background](downloading-files-in-the-background.md)

#### Discussion

For tasks created from background [`URLSession`](urlsession.md) instances, this property indicates that the network load should not begin any earlier than this date. Setting this property does not guarantee that the load will begin at the specified date, but only that it will not begin sooner. If not specified, no start delay is used.

This property has no effect for tasks created from nonbackground sessions.

## See Also

- [var countOfBytesClientExpectsToReceive: Int64](urlsessiontask/countofbytesclientexpectstoreceive.md)
  A best-guess upper bound on the number of bytes the client expects to receive.
- [var countOfBytesClientExpectsToSend: Int64](urlsessiontask/countofbytesclientexpectstosend.md)
  A best-guess upper bound on the number of bytes the client expects to send.
- [let NSURLSessionTransferSizeUnknown: Int64](nsurlsessiontransfersizeunknown.md)
  The total size of the transfer cannot be determined.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessiontask/earliestbegindate)*
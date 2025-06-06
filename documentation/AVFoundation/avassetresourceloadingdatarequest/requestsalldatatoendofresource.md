# requestsAllDataToEndOfResource

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates the entire remaining length of the resource from the offest to the end of the resource is being requested.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var requestsAllDataToEndOfResource: Bool { get }
```

#### Discussion

When this property is true, you should disregard the value of requestedLength and incrementally provide as much data, starting from the requested offset, as the resource contains. Continue until all available data was successfully loaded, the request was cancelled, or an error occurs.

## See Also

- [func respond(with: Data)](avassetresourceloadingdatarequest/respond(with:).md)
  Provides data to the loading request.
- [var requestedLength: Int](avassetresourceloadingdatarequest/requestedlength.md)
  The length, in bytes, of the data requested.
- [var requestedOffset: Int64](avassetresourceloadingdatarequest/requestedoffset.md)
  The position within the resource of the first byte requested.
- [var currentOffset: Int64](avassetresourceloadingdatarequest/currentoffset.md)
  The position within the resource of the next byte.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingdatarequest/requestsalldatatoendofresource)*
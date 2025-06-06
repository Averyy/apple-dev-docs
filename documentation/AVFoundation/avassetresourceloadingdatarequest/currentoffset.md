# currentOffset

**Framework**: AVFoundation  
**Kind**: property

The position within the resource of the next byte.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var currentOffset: Int64 { get }
```

#### Discussion

When incrementally loading data you should begin loading at this offset, returning the data by invoking the [`respond(with:)`](avassetresourceloadingdatarequest/respond(with:).md) method. Bytes previous to this value have already been provided.

## See Also

- [func respond(with: Data)](avassetresourceloadingdatarequest/respond(with:).md)
  Provides data to the loading request.
- [var requestedLength: Int](avassetresourceloadingdatarequest/requestedlength.md)
  The length, in bytes, of the data requested.
- [var requestedOffset: Int64](avassetresourceloadingdatarequest/requestedoffset.md)
  The position within the resource of the first byte requested.
- [var requestsAllDataToEndOfResource: Bool](avassetresourceloadingdatarequest/requestsalldatatoendofresource.md)
  A Boolean value that indicates the entire remaining length of the resource from the offest to the end of the resource is being requested.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingdatarequest/currentoffset)*
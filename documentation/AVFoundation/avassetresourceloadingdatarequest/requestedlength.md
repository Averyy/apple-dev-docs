# requestedLength

**Framework**: AVFoundation  
**Kind**: property

The length, in bytes, of the data requested.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var requestedLength: Int { get }
```

#### Discussion

If the content length of the resource is unknown, the sum of the [`requestedLength`](avassetresourceloadingdatarequest/requestedlength.md) and [`requestedOffset`](avassetresourceloadingdatarequest/requestedoffset.md) properties may be greater than the actual content length. When this situation occurs, an application must attempt to provide as much of the requested data beginning at the [`requestedOffset`](avassetresourceloadingdatarequest/requestedoffset.md) property as the resource contains. The application must then invoke either the [`AVAssetResourceLoadingRequest`](avassetresourceloadingrequest.md) instance’s [`finishLoading()`](avassetresourceloadingrequest/finishloading().md) method upon success, or the [`finishLoading(with:)`](avassetresourceloadingrequest/finishloading(with:).md) method if an error is encountered during the loading.

## See Also

- [func respond(with: Data)](avassetresourceloadingdatarequest/respond(with:).md)
  Provides data to the loading request.
- [var requestedOffset: Int64](avassetresourceloadingdatarequest/requestedoffset.md)
  The position within the resource of the first byte requested.
- [var currentOffset: Int64](avassetresourceloadingdatarequest/currentoffset.md)
  The position within the resource of the next byte.
- [var requestsAllDataToEndOfResource: Bool](avassetresourceloadingdatarequest/requestsalldatatoendofresource.md)
  A Boolean value that indicates the entire remaining length of the resource from the offest to the end of the resource is being requested.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingdatarequest/requestedlength)*
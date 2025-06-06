# respond(with:)

**Framework**: AVFoundation  
**Kind**: method

Provides data to the loading request.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func respond(with data: Data)
```

#### Discussion

This method may be invoked multiple times on the same instance of `AVAssetResourceLoadingDataRequest` to provide the full range of requested data incrementally. Upon each invocation, the value of the [`currentOffset`](avassetresourceloadingdatarequest/currentoffset.md) property is updated to match the amount of data provided.

## Parameters

- `data`: An instance of NSData containing some or all of the requested bytes.

## See Also

- [var requestedLength: Int](avassetresourceloadingdatarequest/requestedlength.md)
  The length, in bytes, of the data requested.
- [var requestedOffset: Int64](avassetresourceloadingdatarequest/requestedoffset.md)
  The position within the resource of the first byte requested.
- [var currentOffset: Int64](avassetresourceloadingdatarequest/currentoffset.md)
  The position within the resource of the next byte.
- [var requestsAllDataToEndOfResource: Bool](avassetresourceloadingdatarequest/requestsalldatatoendofresource.md)
  A Boolean value that indicates the entire remaining length of the resource from the offest to the end of the resource is being requested.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingdatarequest/respond(with:))*
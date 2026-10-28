# requestedOffset

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The position within the resource of the first byte requested.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var requestedOffset: Int64 { get }
```

```objc
@property (nonatomic, readonly) long long requestedOffset;
```

## Discussion

When all of the requested bytes that can be provided have been loaded—including the possible [`contentInformationRequest`](../avassetresourceloadingrequest/contentinformationrequest.md) data in the [`AVAssetResourceLoadingRequest`](../avassetresourceloadingrequest.md) instance that contains the receiver—the delegate should respond by invoking [`finishLoading()`](../avassetresourceloadingrequest/finishloading%28%29.md).

If the `requestedOffset` value is beyond the content length of the resource, the [`AVAssetResourceLoadingRequest`](../avassetresourceloadingrequest.md) instance is sent a [`finishLoading()`](../avassetresourceloadingrequest/finishloading%28%29.md) message without any prior invocations of [`respond(with:)`](./respond%28with%29.md).

## See Also

### Providing data to a request
- [func respond(with: Data)](./respond%28with%29.md)
  Provides data to the loading request.
- [var requestedLength: Int](./requestedlength.md)
  The length, in bytes, of the data requested.
- [var currentOffset: Int64](./currentoffset.md)
  The position within the resource of the next byte.
- [var requestsAllDataToEndOfResource: Bool](./requestsalldatatoendofresource.md)
  A Boolean value that indicates the entire remaining length of the resource from the offest to the end of the resource is being requested.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingdatarequest/requestedoffset)*
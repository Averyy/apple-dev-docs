# AVAssetResourceLoadingDataRequest

**Framework**: AVFoundation  
**Kind**: class

An object for requesting data from a resource that an asset resource-loading request references.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class AVAssetResourceLoadingDataRequest
```

#### Overview

The [`AVAssetResourceLoaderDelegate`](avassetresourceloaderdelegate.md) uses the `AVAssetResourceLoadingDataRequest` class to do the actual data reading, and its methods will be invoked, as necessary, to acquire data for the [`AVAssetResourceLoadingRequest`](avassetresourceloadingrequest.md) instance.

When the resource loading delegate, which implements the [`AVAssetResourceLoaderDelegate`](avassetresourceloaderdelegate.md) protocol, receives an instance of [`AVAssetResourceLoadingRequest`](avassetresourceloadingrequest.md) as the second parameter of the delegate’s [`resourceLoader(_:shouldWaitForLoadingOfRequestedResource:)`](avassetresourceloaderdelegate/resourceloader(_:shouldwaitforloadingofrequestedresource:).md) method, it has the option of accepting responsibility for loading the referenced resource. If it accepts that responsibility, by returning [`true`](https://developer.apple.com/documentation/swift/true), it must check whether the [`dataRequest`](avassetresourceloadingrequest/datarequest.md) property of the [`AVAssetResourceLoadingRequest`](avassetresourceloadingrequest.md) instance is not `nil`. If it is not `nil`, the resource loading delegate is informed of the range of bytes within the resource that are required by the underlying media system. In response, the data is provided by one or more invocations of [`respond(with:)`](avassetresourceloadingdatarequest/respond(with:).md) as required to provide the requested data. The data can be provided in increments determined by the resource loading delegate according to convenience or efficiency.

When the [`AVAssetResourceLoadingRequest`](avassetresourceloadingrequest.md) method [`finishLoading()`](avassetresourceloadingrequest/finishloading().md) is invoked, the data request is considered fully satisfied. If the entire range of bytes requested has not yet been provided, the underlying media system assumes that the resource’s length is limited to the provided content.

## Topics

### Providing Data to a Request
- [func respond(with: Data)](avassetresourceloadingdatarequest/respond(with:).md)
  Provides data to the loading request.
- [var requestedLength: Int](avassetresourceloadingdatarequest/requestedlength.md)
  The length, in bytes, of the data requested.
- [var requestedOffset: Int64](avassetresourceloadingdatarequest/requestedoffset.md)
  The position within the resource of the first byte requested.
- [var currentOffset: Int64](avassetresourceloadingdatarequest/currentoffset.md)
  The position within the resource of the next byte.
- [var requestsAllDataToEndOfResource: Bool](avassetresourceloadingdatarequest/requestsalldatatoendofresource.md)
  A Boolean value that indicates the entire remaining length of the resource from the offest to the end of the resource is being requested.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class AVAssetResourceLoader](avassetresourceloader.md)
  An object that mediates resource requests from a URL asset.
- [protocol AVAssetResourceLoaderDelegate](avassetresourceloaderdelegate.md)
  Methods you can implement to handle resource-loading requests coming from a URL asset.
- [class AVAssetResourceLoadingRequest](avassetresourceloadingrequest.md)
  An object that encapsulates information about a resource request from a resource loader object.
- [class AVAssetResourceRenewalRequest](avassetresourcerenewalrequest.md)
  An object that encapsulates information about a resource request from a resource loader to renew a previously issued request.
- [class AVAssetResourceLoadingRequestor](avassetresourceloadingrequestor.md)
  An object that contains information about the originator of a resource-loading request.
- [class AVAssetResourceLoadingContentInformationRequest](avassetresourceloadingcontentinformationrequest.md)
  A query for retrieving essential information about a resource that an asset resource-loading request references.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingdatarequest)*
# AVAssetResourceLoadingContentInformationRequest

**Framework**: AVFoundation  
**Kind**: class

A query for retrieving essential information about a resource that an asset resource-loading request references.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class AVAssetResourceLoadingContentInformationRequest
```

#### Overview

When a resource loading delegate, which must implement the [`AVAssetResourceLoaderDelegate`](avassetresourceloaderdelegate.md) protocol, receives an instance of [`AVAssetResourceLoadingRequest`](avassetresourceloadingrequest.md) when the [`resourceLoader(_:shouldWaitForLoadingOfRequestedResource:)`](avassetresourceloaderdelegate/resourceloader(_:shouldwaitforloadingofrequestedresource:).md) is invoked and accepts responsibility for loading the resource, it must check whether the [`contentInformationRequest`](avassetresourceloadingrequest/contentinformationrequest.md) property of the [`AVAssetResourceLoadingRequest`](avassetresourceloadingrequest.md) is not `nil`. Whenever the value is not `nil`, the request includes a query for the information that `AVAssetResourceLoadingContentInformationRequest` encapsulates. In response to such queries, the resource loading delegate should set the values of the content information request’s properties appropriately before invoking the [`AVAssetResourceLoadingRequest`](avassetresourceloadingrequest.md) method [`finishLoading()`](avassetresourceloadingrequest/finishloading().md).

When [`finishLoading()`](avassetresourceloadingrequest/finishloading().md) is invoked, the values of the properties of its [`contentInformationRequest`](avassetresourceloadingrequest/contentinformationrequest.md) property will, in part, determine how the requested resource is processed. For example, if the requested resource’s URL is the URL of an [`AVURLAsset`](avurlasset.md) and [`contentType`](avassetresourceloadingcontentinformationrequest/contenttype.md) is set by the resource loading delegate to a value that the underlying media system doesn’t recognize as a supported media file type, operations on the `AVURLAsset`, such as playback, are likely to fail.

## Topics

### Configuring content information
- [var allowedContentTypes: [String]?](avassetresourceloadingcontentinformationrequest/allowedcontenttypes.md)
  The types of data that are accepted as a valid response for the requested resource.
- [var contentType: String?](avassetresourceloadingcontentinformationrequest/contenttype.md)
  The UTI that specifies the type of data contained by the requested resource.
- [var contentLength: Int64](avassetresourceloadingcontentinformationrequest/contentlength.md)
  The length, in bytes, of the requested resource.
- [var isByteRangeAccessSupported: Bool](avassetresourceloadingcontentinformationrequest/isbyterangeaccesssupported.md)
  A Boolean value that indicates whether random access to arbitrary ranges of bytes of the resource is supported.
- [var renewalDate: Date?](avassetresourceloadingcontentinformationrequest/renewaldate.md)
  The date at which a new resource loading request will be issued for resources that expire, if the media system still requires it.
- [var isEntireLengthAvailableOnDemand: Bool](avassetresourceloadingcontentinformationrequest/isentirelengthavailableondemand.md)
  A Boolean value that indicates whether asset data loading can expect data immediately.

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
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [class AVAssetResourceLoadingDataRequest](avassetresourceloadingdatarequest.md)
  An object for requesting data from a resource that an asset resource-loading request references.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingcontentinformationrequest)*
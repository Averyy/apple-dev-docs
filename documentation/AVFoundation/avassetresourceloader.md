# AVAssetResourceLoader

**Framework**: AVFoundation  
**Kind**: class

An object that mediates resource requests from a URL asset.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class AVAssetResourceLoader
```

#### Overview

You do not create resource loader objects yourself. Instead, you retrieve a resource loader from the [`resourceLoader`](avurlasset/resourceloader.md) property of an [`AVURLAsset`](avurlasset.md) object and use it to assign your custom delegate object.

The delegate you associate with this object must adopt the [`AVAssetResourceLoaderDelegate`](avassetresourceloaderdelegate.md) protocol. For more information, see [`AVAssetResourceLoaderDelegate`](avassetresourceloaderdelegate.md).

## Topics

### Accessing the Delegate
- [func setDelegate((any AVAssetResourceLoaderDelegate)?, queue: dispatch_queue_t?)](avassetresourceloader/setdelegate(_:queue:).md)
  Sets the delegate and dispatch queue to use with the resource loader.
- [var delegate: (any AVAssetResourceLoaderDelegate)?](avassetresourceloader/delegate.md)
  The delegate object to use when handling resource requests.
- [protocol AVAssetResourceLoaderDelegate](avassetresourceloaderdelegate.md)
  Methods you can implement to handle resource-loading requests coming from a URL asset.
- [var delegateQueue: dispatch_queue_t?](avassetresourceloader/delegatequeue.md)
  The dispatch queue to use when handling resource requests.
### Loading Content Keys
- [var preloadsEligibleContentKeys: Bool](avassetresourceloader/preloadseligiblecontentkeys.md)
  A Boolean value that indicates whether content keys will be loaded as quickly as possible.
### Supporting Common Media Client Data
- [var sendsCommonMediaClientDataAsHTTPHeaders: Bool](avassetresourceloader/sendscommonmediaclientdataashttpheaders.md)
  A Boolean value that indicates whether to enable attaching Common Media Client Data as HTTP request headers.

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
- [class AVAssetResourceLoadingContentInformationRequest](avassetresourceloadingcontentinformationrequest.md)
  A query for retrieving essential information about a resource that an asset resource-loading request references.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetresourceloader)*
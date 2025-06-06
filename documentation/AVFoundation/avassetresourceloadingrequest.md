# AVAssetResourceLoadingRequest

**Framework**: AVFoundation  
**Kind**: class

An object that encapsulates information about a resource request from a resource loader object.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class AVAssetResourceLoadingRequest
```

#### Overview

When an [`AVURLAsset`](avurlasset.md) object needs help loading a resource, it asks its [`AVAssetResourceLoader`](avassetresourceloader.md) object to assist. The resource loader encapsulates the request information by creating an instance of this object, which it then hands to its delegate object for processing. The delegate uses the information in this object to perform the request and report on the success or failure of the operation.

## Topics

### Accessing the Request Data
- [var request: URLRequest](avassetresourceloadingrequest/request.md)
  The URL request object for the resource.
- [var requestor: AVAssetResourceLoadingRequestor](avassetresourceloadingrequest/requestor.md)
  The asset resource requestor that made the request.
- [var contentInformationRequest: AVAssetResourceLoadingContentInformationRequest?](avassetresourceloadingrequest/contentinformationrequest.md)
  The information for a requested resource.
- [var dataRequest: AVAssetResourceLoadingDataRequest?](avassetresourceloadingrequest/datarequest.md)
  The range of requested resource data.
- [var redirect: URLRequest?](avassetresourceloadingrequest/redirect.md)
  An URL request instance if the loading request was redirected.
- [func streamingContentKeyRequestData(forApp: Data, contentIdentifier: Data, options: [String : Any]?) throws -> Data](avassetresourceloadingrequest/streamingcontentkeyrequestdata(forapp:contentidentifier:options:).md)
  Obtains key request data for a specific combination of application and content.
- [func persistentContentKey(fromKeyVendorResponse: Data, options: [String : Any]?) throws -> Data](avassetresourceloadingrequest/persistentcontentkey(fromkeyvendorresponse:options:).md)
  Obtains a persistable content key from a context.
- [let AVAssetResourceLoadingRequestStreamingContentKeyRequestRequiresPersistentKey: String](avassetresourceloadingrequeststreamingcontentkeyrequestrequirespersistentkey.md)
  Specifies whether the content key request requires a persistable key to be returned from the key vendor.
### Reporting the Result of the Request
- [var response: URLResponse?](avassetresourceloadingrequest/response.md)
  The URL response for the loading request.
- [func finishLoading()](avassetresourceloadingrequest/finishloading.md)
  Causes the receiver to treat the processing of the request as complete.
- [var isCancelled: Bool](avassetresourceloadingrequest/iscancelled.md)
  A Boolean value that indicates whether the request has been cancelled.
- [func finishLoading(with: (any Error)?)](avassetresourceloadingrequest/finishloading(with:).md)
  Causes the receiver to handle the failure to load a resource for which a resource loader’s delegate took responsibility.
- [var isFinished: Bool](avassetresourceloadingrequest/isfinished.md)
  A Boolean value that indicates whether loading of the resource has finished.
- [func finishLoading(with: URLResponse?, data: Data?, redirect: URLRequest?)](avassetresourceloadingrequest/finishloading(with:data:redirect:).md)
  Causes the receiver to finish loading a resource for which a resource loader’s delegate took responsibility .

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [AVAssetResourceRenewalRequest](avassetresourcerenewalrequest.md)
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
- [class AVAssetResourceRenewalRequest](avassetresourcerenewalrequest.md)
  An object that encapsulates information about a resource request from a resource loader to renew a previously issued request.
- [class AVAssetResourceLoadingRequestor](avassetresourceloadingrequestor.md)
  An object that contains information about the originator of a resource-loading request.
- [class AVAssetResourceLoadingDataRequest](avassetresourceloadingdatarequest.md)
  An object for requesting data from a resource that an asset resource-loading request references.
- [class AVAssetResourceLoadingContentInformationRequest](avassetresourceloadingcontentinformationrequest.md)
  A query for retrieving essential information about a resource that an asset resource-loading request references.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetresourceloadingrequest)*
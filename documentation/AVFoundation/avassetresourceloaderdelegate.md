# AVAssetResourceLoaderDelegate

**Framework**: AVFoundation  
**Kind**: protocol  
**Role**: Protocol

Methods you can implement to handle resource-loading requests coming from a URL asset.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
protocol AVAssetResourceLoaderDelegate : NSObjectProtocol
```

```objc
@protocol AVAssetResourceLoaderDelegate <NSObject>
```

## Overview

A class should adopt this protocol when associated with the asset’s resource loader—that is, an instance of the [`AVAssetResourceLoader`](./avassetresourceloader.md) class. The resource loader works with your delegate to process the request.

## Topics

### Processing resource requests
- [func resourceLoader(AVAssetResourceLoader, shouldWaitForLoadingOfRequestedResource: AVAssetResourceLoadingRequest) -> Bool](./avassetresourceloaderdelegate/resourceloader%28_,shouldwaitforloadingofrequestedresource%29.md)
  Asks the delegate if it wants to load the requested resource.
- [func resourceLoader(AVAssetResourceLoader, shouldWaitForRenewalOfRequestedResource: AVAssetResourceRenewalRequest) -> Bool](./avassetresourceloaderdelegate/resourceloader%28_,shouldwaitforrenewalofrequestedresource%29.md)
  Tells the delegate when assistance is required of the application to renew a resource.
- [func resourceLoader(AVAssetResourceLoader, didCancel: AVAssetResourceLoadingRequest)](./avassetresourceloaderdelegate/resourceloader%28_,didcancel%29-3nl51.md)
  Informs the delegate that a prior loading request has been cancelled.
### Processing authentication challenges
- [func resourceLoader(AVAssetResourceLoader, shouldWaitForResponseTo: URLAuthenticationChallenge) -> Bool](./avassetresourceloaderdelegate/resourceloader%28_,shouldwaitforresponseto%29.md)
  Tells the delegate that assistance is required of the application to respond to an authentication challenge.
- [func resourceLoader(AVAssetResourceLoader, didCancel: URLAuthenticationChallenge)](./avassetresourceloaderdelegate/resourceloader%28_,didcancel%29-1wqin.md)
  Informs the delegate that a prior authentication challenge has been cancelled.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Resource loading
- [class AVAssetResourceLoader](./avassetresourceloader.md)
  An object that mediates resource requests from a URL asset.
- [class AVAssetResourceLoadingRequest](./avassetresourceloadingrequest.md)
  An object that encapsulates information about a resource request from a resource loader object.
- [class AVAssetResourceRenewalRequest](./avassetresourcerenewalrequest.md)
  An object that encapsulates information about a resource request from a resource loader to renew a previously issued request.
- [class AVAssetResourceLoadingRequestor](./avassetresourceloadingrequestor.md)
  An object that contains information about the originator of a resource-loading request.
- [class AVAssetResourceLoadingDataRequest](./avassetresourceloadingdatarequest.md)
  An object for requesting data from a resource that an asset resource-loading request references.
- [class AVAssetResourceLoadingContentInformationRequest](./avassetresourceloadingcontentinformationrequest.md)
  A query for retrieving essential information about a resource that an asset resource-loading request references.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetresourceloaderdelegate)*
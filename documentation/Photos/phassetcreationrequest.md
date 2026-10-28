# PHAssetCreationRequest

**Framework**: Photos  
**Kind**: class  
**Role**: Class

A request to create a new Photos asset from underlying data resources, for use in a photo library change block.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class PHAssetCreationRequest
```

```objc
@interface PHAssetCreationRequest : PHAssetChangeRequest
```

## Mentions

- [Delivering an Enhanced Privacy Experience in Your Photos App](../PhotoKit/delivering-an-enhanced-privacy-experience-in-your-photos-app.md)

## Overview

A [`PHAssetCreationRequest`](./phassetcreationrequest.md) object, used within a photo library change block, constructs a new photo or video asset from data resources, and adds it to the Photos library. This class works in terms of the raw data resources that together form an asset, so you can use it together with the [`PHAssetResource`](./phassetresource.md) class to perform a complete copy (or backup and restore) of an asset’s underlying resources. To instead simply create a new asset from an image object, image file, or video file, see the superclass [`PHAssetChangeRequest`](./phassetchangerequest.md).

To create a new asset from data resources, first start a change block using the shared [`PHPhotoLibrary`](./phphotolibrary.md) method [`performChanges(_:completionHandler:)`](./phphotolibrary/performchanges%28_,completionhandler%29.md) or [`performChangesAndWait(_:)`](./phphotolibrary/performchangesandwait%28_%29.md). Then, within the change block:

1. Within the change block, create a new asset creation request with the [`forAsset()`](./phassetcreationrequest/forasset%28%29.md) method.
2. Add image, video, or data resources using [`addResource(with:data:options:)`](./phassetcreationrequest/addresource%28with,data,options%29.md) or [`addResource(with:fileURL:options:)`](./phassetcreationrequest/addresource%28with,fileurl,options%29.md).
3. (Optional.) Set metadata for the new asset using methods and properties of the superclass [`PHAssetChangeRequest`](./phassetchangerequest.md).

After Photos runs the change block and calls your completion handler, the new asset is created in the Photos library.

If you instantiate or use this class outside a photo library change block, Photos throws an exception. For details on change blocks, see [`PHPhotoLibrary`](./phphotolibrary.md).

## Topics

### Requesting Asset Creation
- [class func forAsset() -> Self](./phassetcreationrequest/forasset%28%29.md)
  Creates a request for adding a new asset to the Photos library using asset resources.
### Preflighting a Request
- [class func supportsAssetResourceTypes([NSNumber]) -> Bool](./phassetcreationrequest/supportsassetresourcetypes%28_%29.md)
  Returns a Boolean value indicating whether Photos supports creating an asset with the specified combination of resource types.
### Providing Data Resources for the New Asset
- [func addResource(with: PHAssetResourceType, data: Data, options: PHAssetResourceCreationOptions?)](./phassetcreationrequest/addresource%28with,data,options%29.md)
  Adds a data resource to the asset being created, using the specified data.
- [func addResource(with: PHAssetResourceType, fileURL: URL, options: PHAssetResourceCreationOptions?)](./phassetcreationrequest/addresource%28with,fileurl,options%29.md)
  Adds a data resource to the asset being created, using the file at the specified URL.
### Instance Properties
- [var originalResourceChoice: PHAsset.OriginalResourceChoice](./phassetcreationrequest/originalresourcechoice.md)
  The original resource to use as the unadjusted base for rendering derivatives of the new asset.

## Relationships

### Inherits From
- [PHAssetChangeRequest](./phassetchangerequest.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Asset resource management
- [class PHAssetResource](./phassetresource.md)
  An underlying data resource associated with a photo, video, or Live Photo asset in the Photos library.
- [class PHAssetResourceCreationOptions](./phassetresourcecreationoptions.md)
  A set of options affecting the creation of a new Photos asset from underlying resources.
- [class PHAssetResourceManager](./phassetresourcemanager.md)
  A resource manager for the data storage underlying a Photos asset.
- [class PHAssetResourceRequestOptions](./phassetresourcerequestoptions.md)
  A set of options affecting the delivery of underlying asset data that you request from the asset-resource manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetcreationrequest)*
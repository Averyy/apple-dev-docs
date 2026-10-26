# PHAssetResourceManager

**Framework**: Photos  
**Kind**: class  
**Role**: Class

A resource manager for the data storage underlying a Photos asset.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class PHAssetResourceManager
```

```objc
@interface PHAssetResourceManager : NSObject
```

#### Overview

An asset can have multiple underlying data resources—for example, both original and edited versions—each of which is represented by a [`PHAssetResource`](./phassetresource.md) object. Unlike the [`PHImageManager`](./phimagemanager.md) class, which provides and caches the primary representations of assets as thumbnails, image objects, or video objects, the asset resource manager provides direct access to these underlying data resources.

## Topics

### Getting the Asset Resource Manager
- [class func `default`() -> PHAssetResourceManager](./phassetresourcemanager/default%28%29.md)
  Returns the shared asset resource manager object.
### Requesting Resources
- [func requestData(for: PHAssetResource, options: PHAssetResourceRequestOptions?, dataReceivedHandler: (Data) -> Void, completionHandler: ((any Error)?) -> Void) -> PHAssetResourceDataRequestID](./phassetresourcemanager/requestdata%28for,options,datareceivedhandler,completionhandler%29.md)
  Requests the underlying data for the specified asset resource, to be delivered asynchronously.
- [func cancelDataRequest(PHAssetResourceDataRequestID)](./phassetresourcemanager/canceldatarequest%28_%29.md)
  Cancels an asynchronous request.
- [func writeData(for: PHAssetResource, toFile: URL, options: PHAssetResourceRequestOptions?, completionHandler: ((any Error)?) -> Void)](./phassetresourcemanager/writedata%28for,tofile,options,completionhandler%29.md)
  Requests the underlying data for the specified asset resource, to be asynchronously written to a local file.
### Constants
- [typealias PHAssetResourceDataRequestID](./phassetresourcedatarequestid.md)
  A numeric identifier for an asynchronous asset resource loading request.
- [Resource Loading Request Identifiers](../PhotoKit/resource-loading-request-identifiers.md)
  Special values for the [`PHAssetResourceDataRequestID`](./phassetresourcedatarequestid.md) identifier that are returned by asynchronous requests.
### Instance Methods
- [func exportedAssetID(for: PHAssetResource) async throws -> CKAsset.ExportedAssetID](./phassetresourcemanager/exportedassetid%28for%29.md)
  Returns the exported asset ID for the specified asset resource.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Asset resource management
- [class PHAssetResource](./phassetresource.md)
  An underlying data resource associated with a photo, video, or Live Photo asset in the Photos library.
- [class PHAssetCreationRequest](./phassetcreationrequest.md)
  A request to create a new Photos asset from underlying data resources, for use in a photo library change block.
- [class PHAssetResourceCreationOptions](./phassetresourcecreationoptions.md)
  A set of options affecting the creation of a new Photos asset from underlying resources.
- [class PHAssetResourceRequestOptions](./phassetresourcerequestoptions.md)
  A set of options affecting the delivery of underlying asset data that you request from the asset-resource manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetresourcemanager)*
# PHAssetResourceRequestOptions

**Framework**: Photos  
**Kind**: class  
**Role**: Class

A set of options affecting the delivery of underlying asset data that you request from the asset-resource manager.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class PHAssetResourceRequestOptions
```

```objc
@interface PHAssetResourceRequestOptions : NSObject
```

## Overview

You use this class when requesting the underlying data for photo, video, and Live Photo asset resources from a [`PHAssetResourceManager`](./phassetresourcemanager.md) object.

## Topics

### Fetching Resource Data from iCloud
- [var isNetworkAccessAllowed: Bool](./phassetresourcerequestoptions/isnetworkaccessallowed.md)
  A Boolean value that specifies whether Photos can download the requested asset resource data from iCloud.
- [var progressHandler: PHAssetResourceProgressHandler?](./phassetresourcerequestoptions/progresshandler.md)
  A block that Photos calls periodically while downloading the asset resource data.
- [typealias PHAssetResourceProgressHandler](./phassetresourceprogresshandler.md)
  The signature for a block that Photos calls while downloading asset resource data from iCloud. Used by the [`progressHandler`](./phassetresourcerequestoptions/progresshandler.md) property.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Asset resource management
- [class PHAssetResource](./phassetresource.md)
  An underlying data resource associated with a photo, video, or Live Photo asset in the Photos library.
- [class PHAssetCreationRequest](./phassetcreationrequest.md)
  A request to create a new Photos asset from underlying data resources, for use in a photo library change block.
- [class PHAssetResourceCreationOptions](./phassetresourcecreationoptions.md)
  A set of options affecting the creation of a new Photos asset from underlying resources.
- [class PHAssetResourceManager](./phassetresourcemanager.md)
  A resource manager for the data storage underlying a Photos asset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetresourcerequestoptions)*
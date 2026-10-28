# PHAssetResourceCreationOptions

**Framework**: Photos  
**Kind**: class  
**Role**: Class

A set of options affecting the creation of a new Photos asset from underlying resources.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class PHAssetResourceCreationOptions
```

```objc
@interface PHAssetResourceCreationOptions : NSObject
```

## Overview

You use this class when creating an asset for addition to the Photos library with a [`PHAssetCreationRequest`](./phassetcreationrequest.md) object.

## Topics

### Describing a New Asset Resource
- [var originalFilename: String?](./phassetresourcecreationoptions/originalfilename.md)
  The filename for the asset resource being created.
- [var uniformTypeIdentifier: String?](./phassetresourcecreationoptions/uniformtypeidentifier.md)
  The uniform type identifier for the resource.
- [var contentType: UTType?](./phassetresourcecreationoptions/contenttype.md)
  The type of data being provided for this asset resource. If not specified, one will be inferred from the PHAssetResourceType or file URL extension (if provided).
### Managing Resource Files
- [var shouldMoveFile: Bool](./phassetresourcecreationoptions/shouldmovefile.md)
  A Boolean value that determines whether Photos moves or duplicates files when creating an asset resource.

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
- [class PHAssetResourceManager](./phassetresourcemanager.md)
  A resource manager for the data storage underlying a Photos asset.
- [class PHAssetResourceRequestOptions](./phassetresourcerequestoptions.md)
  A set of options affecting the delivery of underlying asset data that you request from the asset-resource manager.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phassetresourcecreationoptions)*
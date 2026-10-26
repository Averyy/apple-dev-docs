# PHChangeRequest

**Framework**: Photos  
**Kind**: class  
**Role**: Class

The abstract base class of the framework’s photo library change requests.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class PHChangeRequest
```

```objc
@interface PHChangeRequest : NSObject
```

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [PHAssetChangeRequest](./phassetchangerequest.md)
- [PHAssetCollectionChangeRequest](./phassetcollectionchangerequest.md)
- [PHAssetResourceUploadJobChangeRequest](./phassetresourceuploadjobchangerequest.md)
- [PHCollectionListChangeRequest](./phcollectionlistchangerequest.md)
- [PHProjectChangeRequest](./phprojectchangerequest.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Updating the Library
- [Requesting Changes to the Photo Library](../PhotoKit/requesting-changes-to-the-photo-library.md)
  Create, delete, or modify assets and collections in a photo library by making change requests.
- [func performChanges(() -> Void, completionHandler: ((Bool, (any Error)?) -> Void)?)](./phphotolibrary/performchanges%28_,completionhandler%29.md)
  Asynchronously runs a block that requests changes to the photo library.
- [func performChangesAndWait(() -> Void) throws](./phphotolibrary/performchangesandwait%28_%29.md)
  Synchronously runs a block that requests changes to be performed in the photo library.
- [class PHAssetChangeRequest](./phassetchangerequest.md)
  A request to create, delete, change metadata for, or edit the content of a Photos asset, for use in a photo library change block.
- [class PHAssetCollectionChangeRequest](./phassetcollectionchangerequest.md)
  A request to create, delete, or modify a Photos asset collection, for use in a photo library change block.
- [class PHCollectionListChangeRequest](./phcollectionlistchangerequest.md)
  A request to create, delete, or modify a Photos collection list, for use in a photo library change block.
- [class PHObjectPlaceholder](./phobjectplaceholder.md)
  A read-only proxy object that represents a Photos asset or collection to create.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phchangerequest)*
# NSFileProviderItemVersion

**Framework**: File Provider  
**Kind**: class

The version of the item’s content and its metadata.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class NSFileProviderItemVersion
```

#### Overview

Each item has a separate version object for its metadata and its content. As a result, the file provider can update an item’s metadata without uploading or downloading a new copy of its content.

## Topics

### Creating Version Instances
- [init(contentVersion: Data, metadataVersion: Data)](nsfileprovideritemversion/init(contentversion:metadataversion:).md)
  Creates a new version object.
### Accessing Version Data
- [class var beforeFirstSyncComponent: Data](nsfileprovideritemversion/beforefirstsynccomponent.md)
  A Boolean value indicating that this version predates the version returned by the file provider extension.
- [var contentVersion: Data](nsfileprovideritemversion/contentversion.md)
  An opaque object used to track versions of the item’s content.
- [var metadataVersion: Data](nsfileprovideritemversion/metadataversion.md)
  An opaque object used to track versions of the item’s metadata.

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

## See Also

- [struct NSFileProviderItemFields](nsfileprovideritemfields.md)
  Fields that specify which of the item’s properties have changed.
- [class NSFileProviderRequest](nsfileproviderrequest.md)
  An object that provides information about the application requesting data from the File Provider extension.
- [protocol NSFileProviderItemDecorating](nsfileprovideritemdecorating.md)
  Support for decorating items.
- [struct NSFileProviderItemDecorationIdentifier](nsfileprovideritemdecorationidentifier.md)
  A decoration identifier defined in the File Provider extension’s information property list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovideritemversion)*
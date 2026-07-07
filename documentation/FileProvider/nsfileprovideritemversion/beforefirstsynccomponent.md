# beforeFirstSyncComponent

**Framework**: File Provider  
**Kind**: property

A Boolean value indicating that this version predates the version returned by the file provider extension.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
class var beforeFirstSyncComponent: Data { get }
```

#### Discussion

The system uses this property to represent an item that doesn’t have a corresponding version provided by the file provider extension.

When creating an item by calling the [`createItem(basedOn:fields:contents:options:request:completionHandler:)`](nsfileproviderreplicatedextension/createitem(basedon:fields:contents:options:request:completionhandler:).md) method, if your file provider extension returns an item that doesn’t match the template, the system tries to apply the necessary changes before saving the item to disk. However, if the system detects conflicts with the version on disk, it sends the new item back to your file provider extension by calling either the [`modifyItem(_:baseVersion:changedFields:contents:options:request:completionHandler:)`](nsfileproviderreplicatedextension/modifyitem(_:baseversion:changedfields:contents:options:request:completionhandler:).md) of [`deleteItem(identifier:baseVersion:options:request:completionHandler:)`](nsfileproviderreplicatedextension/deleteitem(identifier:baseversion:options:request:completionhandler:).md) methods with a `baseVersion` property that represents the item passed to the [`createItem(basedOn:fields:contents:options:request:completionHandler:)`](nsfileproviderreplicatedextension/createitem(basedon:fields:contents:options:request:completionhandler:).md) method.

## See Also

- [var contentVersion: Data](nsfileprovideritemversion/contentversion.md)
  An opaque object used to track versions of the item’s content.
- [var metadataVersion: Data](nsfileprovideritemversion/metadataversion.md)
  An opaque object used to track versions of the item’s metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovideritemversion/beforefirstsynccomponent)*
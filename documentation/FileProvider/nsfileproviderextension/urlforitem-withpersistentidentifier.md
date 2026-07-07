# urlForItem(withPersistentIdentifier:)

**Framework**: File Provider  
**Kind**: method

Returns the URL for a given persistent identifier.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- visionOS 1.0+

## Declaration

```swift
func urlForItem(withPersistentIdentifier identifier: NSFileProviderItemIdentifier) -> URL?
```

#### Return Value

The URL of a shared document.

#### Discussion

Override this method to provide the URL for the document with the given identifier. This method must be the inverse of [`persistentIdentifierForItem(at:)`](nsfileproviderextension/persistentidentifierforitem(at:).md), mapping from the persistent identifier, back to the URL.

This URL must be inside the directory referred to by the [`NSFileProviderManager`](nsfileprovidermanager.md) object’s [`documentStorageURL`](nsfileprovidermanager/documentstorageurl.md) property.

## Parameters

- `identifier`: The persistent identifier for a shared document.

## See Also

- [func persistentIdentifierForItem(at: URL) -> NSFileProviderItemIdentifier?](nsfileproviderextension/persistentidentifierforitem(at:).md)
  Returns a unique identifier for the given URL.
- [func item(for: NSFileProviderItemIdentifier) throws -> NSFileProviderItem](nsfileproviderextension/item(for:).md)
  Returns a description of the item associated with the persistent identifier.
- [func enumerator(for: NSFileProviderItemIdentifier) throws -> any NSFileProviderEnumerator](nsfileproviderextension/enumerator(for:).md)
  Returns an enumerator for the specified item.
- [struct NSFileProviderItemIdentifier](nsfileprovideritemidentifier.md)
  A unique identifier for an item managed by the File Provider extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderextension/urlforitem(withpersistentidentifier:))*
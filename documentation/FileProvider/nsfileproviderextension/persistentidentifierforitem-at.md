# persistentIdentifierForItem(at:)

**Framework**: File Provider  
**Kind**: method

Returns a unique identifier for the given URL.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- visionOS 1.0+

## Declaration

```swift
func persistentIdentifierForItem(at url: URL) -> NSFileProviderItemIdentifier?
```

#### Return Value

A unique identifier for the item specified by the URL, or `nil` if the document is not in the File Provider’s shared container.

#### Discussion

Override this method to define a static mapping between URLs and their persistent identifiers. A document’s identifier should remain constant over time; it should not change when the document is edited, moved, or renamed.

For example, if you already have a unique key for the document in your cloud database, you can use that key as the document’s identifier.

Always return `nil` if the URL is not inside in the directory referred to by the [`NSFileProviderManager`](nsfileprovidermanager.md) object’s [`documentStorageURL`](nsfileprovidermanager/documentstorageurl.md) property.

## Parameters

- `url`: The URL of a shared document.

## See Also

- [func urlForItem(withPersistentIdentifier: NSFileProviderItemIdentifier) -> URL?](nsfileproviderextension/urlforitem(withpersistentidentifier:).md)
  Returns the URL for a given persistent identifier.
- [func item(for: NSFileProviderItemIdentifier) throws -> NSFileProviderItem](nsfileproviderextension/item(for:).md)
  Returns a description of the item associated with the persistent identifier.
- [func enumerator(for: NSFileProviderItemIdentifier) throws -> any NSFileProviderEnumerator](nsfileproviderextension/enumerator(for:).md)
  Returns an enumerator for the specified item.
- [struct NSFileProviderItemIdentifier](nsfileprovideritemidentifier.md)
  A unique identifier for an item managed by the File Provider extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderextension/persistentidentifierforitem(at:))*
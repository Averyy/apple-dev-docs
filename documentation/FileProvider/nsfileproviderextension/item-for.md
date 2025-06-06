# item(for:)

**Framework**: File Provider  
**Kind**: method

Returns a description of the item associated with the persistent identifier.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func item(for identifier: NSFileProviderItemIdentifier) throws -> NSFileProviderItem
```

#### Return Value

A custom object that describes the specified document or directory, or `nil` in Objective-C if an error occurs.

#### Discussion

Your File Provider extension must define a class that adopts the [`NSFileProviderItemProtocol`](nsfileprovideritemprotocol.md) interface. Instances of this class provides access to information about an item (a document or directory) that your File Provider manages and stores.

Your class should implement as many of the protocol’s optional methods as makes sense for the specified item. This lets the system provide as much information as possible to the user as they browse your File Provider.

Optionally, you can define different classes for different types of items—for example, different classes for documents and directories. These classes can define different subsets of the [`NSFileProviderItemProtocol`](nsfileprovideritemprotocol.md) interface’s optional methods. For example, the class representing a folder implements the [`childItemCount`](nsfileprovideritemprotocol/childitemcount.md) property, while the class representing a document does not.

Override this method to look up the item associated with the persistent identifier and return an instance of your custom [`NSFileProviderItemProtocol`](nsfileprovideritemprotocol.md) class for that item.

## Parameters

- `identifier`: The persistent identifier for a shared document.

## See Also

- [func persistentIdentifierForItem(at: URL) -> NSFileProviderItemIdentifier?](nsfileproviderextension/persistentidentifierforitem(at:).md)
  Returns a unique identifier for the given URL.
- [func urlForItem(withPersistentIdentifier: NSFileProviderItemIdentifier) -> URL?](nsfileproviderextension/urlforitem(withpersistentidentifier:).md)
  Returns the URL for a given persistent identifier.
- [func enumerator(for: NSFileProviderItemIdentifier) throws -> any NSFileProviderEnumerator](nsfileproviderextension/enumerator(for:).md)
  Returns an enumerator for the specified item.
- [struct NSFileProviderItemIdentifier](nsfileprovideritemidentifier.md)
  A unique identifier for an item managed by the File Provider extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderextension/item(for:))*
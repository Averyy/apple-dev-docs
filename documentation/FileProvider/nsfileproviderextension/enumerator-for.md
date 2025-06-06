# enumerator(for:)

**Framework**: File Provider  
**Kind**: method

Returns an enumerator for the specified item.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func enumerator(for containerItemIdentifier: NSFileProviderItemIdentifier) throws -> any NSFileProviderEnumerator
```

## Mentions

- [Defining Your File Provider’s Content](defining-your-file-provider-s-content.md)

#### Return Value

An enumerator for the specified document or folder, or `nil` in Objective-C if an error has occurred.

#### Discussion

Your File Provider extension must define one or more classes that adopt the [`NSFileProviderEnumerator`](nsfileproviderenumerator.md) protocol. Instances of these classes must be able to enumerate both the contents of the specified item and any changes to the content.

Override this method to return an instance of your custom [`NSFileProviderEnumerator`](nsfileproviderenumerator.md) class for the specified item (either a document or a folder). For more information, see [`Content and Change Tracking`](content-and-change-tracking.md).

## Parameters

- `containerItemIdentifier`: The persistent identifier for a document or folder.

## See Also

- [func persistentIdentifierForItem(at: URL) -> NSFileProviderItemIdentifier?](nsfileproviderextension/persistentidentifierforitem(at:).md)
  Returns a unique identifier for the given URL.
- [func urlForItem(withPersistentIdentifier: NSFileProviderItemIdentifier) -> URL?](nsfileproviderextension/urlforitem(withpersistentidentifier:).md)
  Returns the URL for a given persistent identifier.
- [func item(for: NSFileProviderItemIdentifier) throws -> NSFileProviderItem](nsfileproviderextension/item(for:).md)
  Returns a description of the item associated with the persistent identifier.
- [struct NSFileProviderItemIdentifier](nsfileprovideritemidentifier.md)
  A unique identifier for an item managed by the File Provider extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderextension/enumerator(for:))*
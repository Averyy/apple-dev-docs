# NSFileProviderEnumerating

**Framework**: File Provider  
**Kind**: protocol

Support for enumerating the file provider’s contents.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
protocol NSFileProviderEnumerating : NSObjectProtocol
```

## Topics

### Accessing Enumerators
- [func enumerator(for: NSFileProviderItemIdentifier, request: NSFileProviderRequest) throws -> any NSFileProviderEnumerator](nsfileproviderenumerating/enumerator(for:request:).md)
  Tells the file provider to return an enumerator for the provided directory.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Inherited By
- [NSFileProviderReplicatedExtension](nsfileproviderreplicatedextension.md)

## See Also

- [protocol NSFileProviderReplicatedExtension](nsfileproviderreplicatedextension.md)
  A File Provider extension in which the system replicates the contents on disk.
- [protocol NSFileProviderIncrementalContentFetching](nsfileproviderincrementalcontentfetching.md)
  Support for fetching changes to the item’s content.
- [protocol NSFileProviderPartialContentFetching](nsfileproviderpartialcontentfetching.md)
  Support for fetching part of a file’s content.
- [protocol NSFileProviderServicing](nsfileproviderservicing.md)
  Support for providing a custom service source.
- [protocol NSFileProviderCustomAction](nsfileprovidercustomaction.md)
  Support for custom actions.
- [struct NSFileProviderExtensionActionIdentifier](nsfileproviderextensionactionidentifier.md)
  An identifier for custom actions.
- [protocol NSFileProviderThumbnailing](nsfileproviderthumbnailing.md)
  Support for item thumbnails.
- [protocol NSFileProviderPendingSetEnumerator](nsfileproviderpendingsetenumerator.md)
  A protocol for enumerating pending items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderenumerating)*
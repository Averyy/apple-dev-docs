# NSFileProviderThumbnailing

**Framework**: File Provider  
**Kind**: protocol

Support for item thumbnails.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
protocol NSFileProviderThumbnailing : NSObjectProtocol
```

#### Overview

Adopt this protocol if your File Provider extension supports downloading thumbnails from the remote storage.

## Topics

### Providing Thumbnails
- [func fetchThumbnails(for: [NSFileProviderItemIdentifier], requestedSize: CGSize, perThumbnailCompletionHandler: (NSFileProviderItemIdentifier, Data?, (any Error)?) -> Void, completionHandler: ((any Error)?) -> Void) -> Progress](nsfileproviderthumbnailing/fetchthumbnails(for:requestedsize:perthumbnailcompletionhandler:completionhandler:).md)
  Asks the file provider for a thumbnail of the specified items.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol NSFileProviderReplicatedExtension](nsfileproviderreplicatedextension.md)
  A File Provider extension in which the system replicates the contents on disk.
- [protocol NSFileProviderEnumerating](nsfileproviderenumerating.md)
  Support for enumerating the file provider’s contents.
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
- [protocol NSFileProviderPendingSetEnumerator](nsfileproviderpendingsetenumerator.md)
  A protocol for enumerating pending items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderthumbnailing)*
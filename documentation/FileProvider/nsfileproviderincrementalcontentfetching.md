# NSFileProviderIncrementalContentFetching

**Framework**: File Provider  
**Kind**: protocol

Support for fetching changes to the item’s content.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
protocol NSFileProviderIncrementalContentFetching : NSObjectProtocol
```

#### Overview

Adopt this protocol to support the incremental fetching of changes from your remote storage. If you don’t implement the [`fetchContents(for:version:usingExistingContentsAt:existingVersion:request:completionHandler:)`](nsfileproviderincrementalcontentfetching/fetchcontents(for:version:usingexistingcontentsat:existingversion:request:completionhandler:).md) method, the system calls your [`fetchContents(for:version:request:completionHandler:)`](nsfileproviderreplicatedextension/fetchcontents(for:version:request:completionhandler:).md) method for all updates.

## Topics

### Incrementally Fetching Contents
- [func fetchContents(for: NSFileProviderItemIdentifier, version: NSFileProviderItemVersion?, usingExistingContentsAt: URL, existingVersion: NSFileProviderItemVersion, request: NSFileProviderRequest, completionHandler: (URL?, NSFileProviderItem?, (any Error)?) -> Void) -> Progress](nsfileproviderincrementalcontentfetching/fetchcontents(for:version:usingexistingcontentsat:existingversion:request:completionhandler:).md)
  Asks the file provider for an update of the specified item.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol NSFileProviderReplicatedExtension](nsfileproviderreplicatedextension.md)
  A File Provider extension in which the system replicates the contents on disk.
- [protocol NSFileProviderEnumerating](nsfileproviderenumerating.md)
  Support for enumerating the file provider’s contents.
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

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderincrementalcontentfetching)*
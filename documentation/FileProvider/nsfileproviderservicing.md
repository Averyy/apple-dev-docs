# NSFileProviderServicing

**Framework**: File Provider  
**Kind**: protocol

Support for providing a custom service source.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
protocol NSFileProviderServicing : NSObjectProtocol
```

#### Overview

Adopt this protocol if your File Provider extension supports custom services. For more information on custom services, see [`NSFileProviderService`](https://developer.apple.com/documentation/Foundation/NSFileProviderService).

## Topics

### Providing a Service Source
- [func supportedServiceSources(for: NSFileProviderItemIdentifier, completionHandler: ([any NSFileProviderServiceSource]?, (any Error)?) -> Void) -> Progress](nsfileproviderservicing/supportedservicesources(for:completionhandler:).md)
  Asks the File Provider extension for an array of custom communication channels.

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
- [protocol NSFileProviderCustomAction](nsfileprovidercustomaction.md)
  Support for custom actions.
- [struct NSFileProviderExtensionActionIdentifier](nsfileproviderextensionactionidentifier.md)
  An identifier for custom actions.
- [protocol NSFileProviderThumbnailing](nsfileproviderthumbnailing.md)
  Support for item thumbnails.
- [protocol NSFileProviderPendingSetEnumerator](nsfileproviderpendingsetenumerator.md)
  A protocol for enumerating pending items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderservicing)*
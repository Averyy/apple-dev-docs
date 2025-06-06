# NSFileProviderExtensionActionIdentifier

**Framework**: File Provider  
**Kind**: struct

An identifier for custom actions.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
struct NSFileProviderExtensionActionIdentifier
```

## Topics

### Creating Identifiers
- [init(String)](nsfileproviderextensionactionidentifier/init(_:).md)
  Creates a new identifier from the provided string.
- [init(rawValue: String)](nsfileproviderextensionactionidentifier/init(rawvalue:).md)
  Creates a new identifier from the provided value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

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
- [protocol NSFileProviderThumbnailing](nsfileproviderthumbnailing.md)
  Support for item thumbnails.
- [protocol NSFileProviderPendingSetEnumerator](nsfileproviderpendingsetenumerator.md)
  A protocol for enumerating pending items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderextensionactionidentifier)*
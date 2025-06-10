# NSFileProviderPartialContentFetching

**Framework**: File Provider  
**Kind**: protocol

Support for fetching part of a file’s content.

**Availability**:
- macOS 12.3+

## Declaration

```swift
protocol NSFileProviderPartialContentFetching : NSObjectProtocol
```

#### Overview

Adopt this protocol to let the system request only part of a file. Apps that read files provided by your extension can benefit from this feature, either by minimizing the amount of data your file provider needs to download, or by finishing the download quickly, freeing up the reading process.

> ❗ **Important**:  To trigger a partial download, an app must use POSIX read operations to read part of the file. If you clone the entire file, or read the file using file coordination, the system requests the entire file.

For example, a photo app could read just the metadata from each picture in a large album, without having to completely download all the images. Alternatively, a video streaming app could begin playing the video before reading the whole file, reading chunks of data just before it needs them.

## Topics

### Fetching Ranges from a File
- [func fetchPartialContents(for: NSFileProviderItemIdentifier, version: NSFileProviderItemVersion, request: NSFileProviderRequest, minimalRange: NSRange, aligningTo: Int, options: NSFileProviderFetchContentsOptions, completionHandler: (URL?, NSFileProviderItem?, NSRange, NSFileProviderMaterializationFlags, (any Error)?) -> Void) -> Progress](nsfileproviderpartialcontentfetching/fetchpartialcontents(for:version:request:minimalrange:aligningto:options:completionhandler:).md)
  Tells the file provider to download the requested item from remote storage.
- [struct NSFileProviderFetchContentsOptions](nsfileproviderfetchcontentsoptions.md)
  Options for fetching a range of data from a file.
- [struct NSFileProviderMaterializationFlags](nsfileprovidermaterializationflags.md)
  Flags that provides additional information about the provided content.

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

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderpartialcontentfetching)*
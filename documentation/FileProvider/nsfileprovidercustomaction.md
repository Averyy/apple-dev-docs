# NSFileProviderCustomAction

**Framework**: File Provider  
**Kind**: protocol

Support for custom actions.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
protocol NSFileProviderCustomAction : NSObjectProtocol
```

#### Overview

Adopt this protocol to add a custom action to the context menu (for example, when the user control-clicks an item in Finder).

If you want to create an action that displays custom user interface elements, add actions using the [`File Provider UI`](https://developer.apple.com/documentation/FileProviderUI) framework instead. For more information, see `Adding Actions to the Context Menu`.

## Topics

### Performing Custom Actions
- [func performAction(identifier: NSFileProviderExtensionActionIdentifier, onItemsWithIdentifiers: [NSFileProviderItemIdentifier], completionHandler: ((any Error)?) -> Void) -> Progress](nsfileprovidercustomaction/performaction(identifier:onitemswithidentifiers:completionhandler:).md)
  Tells the File Provider extension to perform a custom action.

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
- [struct NSFileProviderExtensionActionIdentifier](nsfileproviderextensionactionidentifier.md)
  An identifier for custom actions.
- [protocol NSFileProviderThumbnailing](nsfileproviderthumbnailing.md)
  Support for item thumbnails.
- [protocol NSFileProviderPendingSetEnumerator](nsfileproviderpendingsetenumerator.md)
  A protocol for enumerating pending items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidercustomaction)*
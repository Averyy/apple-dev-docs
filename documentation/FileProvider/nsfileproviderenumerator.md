# NSFileProviderEnumerator

**Framework**: File Provider  
**Kind**: protocol

A protocol for enumerating items and changes.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
protocol NSFileProviderEnumerator : NSObjectProtocol
```

## Mentions

- [Synchronizing the File Provider Extension](synchronizing-the-file-provider-extension.md)
- [Defining Your File Provider’s Content](defining-your-file-provider-s-content.md)

## Topics

### Enumerating Items and Changes
- [func enumerateItems(for: any NSFileProviderEnumerationObserver, startingAt: NSFileProviderPage)](nsfileproviderenumerator/enumerateitems(for:startingat:).md)
  Requests the next batch of items, starting at the specified page.
- [func enumerateChanges(for: any NSFileProviderChangeObserver, from: NSFileProviderSyncAnchor)](nsfileproviderenumerator/enumeratechanges(for:from:).md)
  Requests the next batch of changes after the specified sync anchor.
- [func currentSyncAnchor(completionHandler: (NSFileProviderSyncAnchor?) -> Void)](nsfileproviderenumerator/currentsyncanchor(completionhandler:).md)
  Returns the current sync anchor.
- [func invalidate()](nsfileproviderenumerator/invalidate.md)
  Stops the enumeration of items and changes.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Inherited By
- [NSFileProviderPendingSetEnumerator](nsfileproviderpendingsetenumerator.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderenumerator)*
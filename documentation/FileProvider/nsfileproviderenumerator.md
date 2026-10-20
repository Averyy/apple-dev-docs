# NSFileProviderEnumerator

**Framework**: File Provider  
**Kind**: protocol  
**Role**: Protocol

A protocol for enumerating items and changes.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
protocol NSFileProviderEnumerator : NSObjectProtocol
```

```objc
@protocol NSFileProviderEnumerator <NSObject>
```

## Mentions

- [Defining Your File Provider’s Content](./defining-your-file-provider-s-content.md)
- [Synchronizing the File Provider Extension](./synchronizing-the-file-provider-extension.md)

## Topics

### Enumerating Items and Changes
- [func enumerateItems(for: any NSFileProviderEnumerationObserver, startingAt: NSFileProviderPage)](./nsfileproviderenumerator/enumerateitems%28for,startingat%29.md)
  Requests the next batch of items, starting at the specified page.
- [func enumerateChanges(for: any NSFileProviderChangeObserver, from: NSFileProviderSyncAnchor)](./nsfileproviderenumerator/enumeratechanges%28for,from%29.md)
  Requests the next batch of changes after the specified sync anchor.
- [func currentSyncAnchor(completionHandler: (NSFileProviderSyncAnchor?) -> Void)](./nsfileproviderenumerator/currentsyncanchor%28completionhandler%29.md)
  Returns the current sync anchor.
- [func invalidate()](./nsfileproviderenumerator/invalidate%28%29.md)
  Stops the enumeration of items and changes.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Inherited By
- [NSFileProviderPendingSetEnumerator](./nsfileproviderpendingsetenumerator.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderenumerator)*
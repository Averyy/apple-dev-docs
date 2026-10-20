# invalidate()

**Framework**: File Provider  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Stops the enumeration of items and changes.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func invalidate()
```

```objc
- (void) invalidate;
```

## See Also

### Enumerating Items and Changes
- [func enumerateItems(for: any NSFileProviderEnumerationObserver, startingAt: NSFileProviderPage)](./enumerateitems%28for,startingat%29.md)
  Requests the next batch of items, starting at the specified page.
- [func enumerateChanges(for: any NSFileProviderChangeObserver, from: NSFileProviderSyncAnchor)](./enumeratechanges%28for,from%29.md)
  Requests the next batch of changes after the specified sync anchor.
- [func currentSyncAnchor(completionHandler: (NSFileProviderSyncAnchor?) -> Void)](./currentsyncanchor%28completionhandler%29.md)
  Returns the current sync anchor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderenumerator/invalidate())*
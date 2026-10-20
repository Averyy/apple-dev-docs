# deleteItems(withIdentifiers:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Deletes the items with the specified identifiers from the snapshot.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func deleteItems(withIdentifiers identifiers: [Any])
```

```objc
- (void) deleteItemsWithIdentifiers:(NSArray<id> *) identifiers;
```

## Parameters

- `identifiers`: The array of identifiers corresponding to the items to delete from the snapshot.

## See Also

### Removing items and sections
- [func deleteAllItems()](./deleteallitems%28%29.md)
  Deletes all of the items from the snapshot.
- [func deleteSections(withIdentifiers: [Any])](./deletesections%28withidentifiers%29.md)
  Deletes the sections with the specified identifiers from the snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdiffabledatasourcesnapshotreference/deleteitems(withidentifiers:))*
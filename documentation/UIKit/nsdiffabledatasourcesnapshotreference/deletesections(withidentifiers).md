# deleteSections(withIdentifiers:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Deletes the sections with the specified identifiers from the snapshot.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func deleteSections(withIdentifiers sectionIdentifiers: [Any])
```

```objc
- (void) deleteSectionsWithIdentifiers:(NSArray<id> *) sectionIdentifiers;
```

## Parameters

- `sectionIdentifiers`: The array of identifiers corresponding to the sections to delete from the snapshot.

## See Also

### Removing items and sections
- [func deleteAllItems()](./deleteallitems%28%29.md)
  Deletes all of the items from the snapshot.
- [func deleteItems(withIdentifiers: [Any])](./deleteitems%28withidentifiers%29.md)
  Deletes the items with the specified identifiers from the snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesnapshotreference/deletesections(withidentifiers:))*
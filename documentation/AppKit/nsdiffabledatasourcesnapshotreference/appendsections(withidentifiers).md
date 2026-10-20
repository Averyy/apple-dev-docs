# appendSections(withIdentifiers:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Adds the sections with the specified identifiers to the snapshot.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func appendSections(withIdentifiers sectionIdentifiers: [Any])
```

```objc
- (void) appendSectionsWithIdentifiers:(NSArray<id> *) sectionIdentifiers;
```

## Parameters

- `sectionIdentifiers`: An array of identifiers specifying the sections to add to the snapshot.

## See Also

### Creating a snapshot
- [func appendItems(withIdentifiers: [Any], intoSectionWithIdentifier: Any)](./appenditems%28withidentifiers,intosectionwithidentifier%29.md)
  Adds the items with the specified identifiers to the specified section of the snapshot.
- [func appendItems(withIdentifiers: [Any])](./appenditems%28withidentifiers%29.md)
  Adds the items with the specified identifiers to the last section of the snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdiffabledatasourcesnapshotreference/appendsections(withidentifiers:))*
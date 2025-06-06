# appendItems(_:toSection:)

**Framework**: AppKit  
**Kind**: method

Adds the items with the specified identifiers to the specified section of the snapshot.

**Availability**:
- macOS 10.15.1+

## Declaration

```swift
mutating func appendItems(_ identifiers: [ItemIdentifierType], toSection sectionIdentifier: SectionIdentifierType? = nil)
```

## Parameters

- `identifiers`: An array of identifiers specifying the items to add to the snapshot.
- `sectionIdentifier`: The section to which to add the items. If no value is provided, the items are appended to the last section of the snapshot.

## See Also

- [init()](nsdiffabledatasourcesnapshot-swift.struct/init.md)
  Creates an empty snapshot.
- [func appendSections([SectionIdentifierType])](nsdiffabledatasourcesnapshot-swift.struct/appendsections(_:).md)
  Adds the sections with the specified identifiers to the snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdiffabledatasourcesnapshot-swift.struct/appenditems(_:tosection:))*
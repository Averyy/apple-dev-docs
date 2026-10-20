# appendSections(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Adds the sections with the specified identifiers to the snapshot.

**Availability**:
- macOS 10.15.1+

## Declaration

```swift
mutating func appendSections(_ identifiers: [SectionIdentifierType])
```

## Parameters

- `identifiers`: An array of identifiers specifying the sections to add to the snapshot.

## See Also

### Creating a Snapshot
- [init()](./init%28%29.md)
  Creates an empty snapshot.
- [func appendItems([ItemIdentifierType], toSection: SectionIdentifierType?)](./appenditems%28_,tosection%29.md)
  Adds the items with the specified identifiers to the specified section of the snapshot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdiffabledatasourcesnapshot-swift.struct/appendsections(_:))*
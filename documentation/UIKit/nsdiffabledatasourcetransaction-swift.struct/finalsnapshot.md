# finalSnapshot

**Framework**: UIKit  
**Kind**: property

The snapshot after the transaction occured.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
var finalSnapshot: NSDiffableDataSourceSnapshot<SectionIdentifierType, ItemIdentifierType> { get }
```

## See Also

- [var sectionTransactions: [NSDiffableDataSourceSectionTransaction<SectionIdentifierType, ItemIdentifierType>]](nsdiffabledatasourcetransaction-swift.struct/sectiontransactions.md)
  An array of section transactions for the transaction.
- [var initialSnapshot: NSDiffableDataSourceSnapshot<SectionIdentifierType, ItemIdentifierType>](nsdiffabledatasourcetransaction-swift.struct/initialsnapshot.md)
  The snapshot before the transaction occured.
- [var difference: CollectionDifference<ItemIdentifierType>](nsdiffabledatasourcetransaction-swift.struct/difference.md)
  A collection of insertions and removals that describe the difference between initial and final snapshots.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcetransaction-swift.struct/finalsnapshot)*
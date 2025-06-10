# sectionTransactions

**Framework**: UIKit  
**Kind**: property

An array of section transactions for the transaction.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
var sectionTransactions: [NSDiffableDataSourceSectionTransaction<SectionIdentifierType, ItemIdentifierType>] { get }
```

## See Also

- [var initialSnapshot: NSDiffableDataSourceSnapshot<SectionIdentifierType, ItemIdentifierType>](nsdiffabledatasourcetransaction-swift.struct/initialsnapshot.md)
  The snapshot before the transaction occured.
- [var finalSnapshot: NSDiffableDataSourceSnapshot<SectionIdentifierType, ItemIdentifierType>](nsdiffabledatasourcetransaction-swift.struct/finalsnapshot.md)
  The snapshot after the transaction occured.
- [var difference: CollectionDifference<ItemIdentifierType>](nsdiffabledatasourcetransaction-swift.struct/difference.md)
  A collection of insertions and removals that describe the difference between initial and final snapshots.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcetransaction-swift.struct/sectiontransactions)*
# initialSnapshot

**Framework**: UIKit  
**Kind**: property

The section snapshot before the transaction occured.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
var initialSnapshot: NSDiffableDataSourceSectionSnapshot<ItemIdentifierType> { get }
```

## See Also

- [var sectionIdentifier: SectionIdentifierType](nsdiffabledatasourcesectiontransaction-swift.struct/sectionidentifier.md)
  The identifier of the section for the transaction.
- [var finalSnapshot: NSDiffableDataSourceSectionSnapshot<ItemIdentifierType>](nsdiffabledatasourcesectiontransaction-swift.struct/finalsnapshot.md)
  The section snapshot after the transaction occured.
- [var difference: CollectionDifference<ItemIdentifierType>](nsdiffabledatasourcesectiontransaction-swift.struct/difference.md)
  A collection of insertions and removals that describe the difference between initial and final section snapshots.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesectiontransaction-swift.struct/initialsnapshot)*
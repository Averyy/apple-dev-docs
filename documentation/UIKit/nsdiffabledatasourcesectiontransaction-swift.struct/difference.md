# difference

**Framework**: UIKit  
**Kind**: property

A collection of insertions and removals that describe the difference between initial and final section snapshots.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
var difference: CollectionDifference<ItemIdentifierType> { get }
```

## See Also

- [var sectionIdentifier: SectionIdentifierType](nsdiffabledatasourcesectiontransaction-swift.struct/sectionidentifier.md)
  The identifier of the section for the transaction.
- [var initialSnapshot: NSDiffableDataSourceSectionSnapshot<ItemIdentifierType>](nsdiffabledatasourcesectiontransaction-swift.struct/initialsnapshot.md)
  The section snapshot before the transaction occured.
- [var finalSnapshot: NSDiffableDataSourceSectionSnapshot<ItemIdentifierType>](nsdiffabledatasourcesectiontransaction-swift.struct/finalsnapshot.md)
  The section snapshot after the transaction occured.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesectiontransaction-swift.struct/difference)*
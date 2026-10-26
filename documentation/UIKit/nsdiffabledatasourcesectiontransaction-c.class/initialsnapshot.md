# initialSnapshot

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The section snapshot before the transaction occured.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```objc
@property (nonatomic, readonly) NSDiffableDataSourceSectionSnapshot<id> * initialSnapshot;
```

## See Also

### Accessing a transaction’s information
- [sectionIdentifier](./sectionidentifier.md)
  The identifier of the section for the transaction.
- [finalSnapshot](./finalsnapshot.md)
  The section snapshot after the transaction occured.
- [difference](./difference.md)
  A collection of insertions and removals that describe the difference between initial and final section snapshots.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesectiontransaction-c.class/initialsnapshot)*
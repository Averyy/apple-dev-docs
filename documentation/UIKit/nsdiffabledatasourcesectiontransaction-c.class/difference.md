# difference

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A collection of insertions and removals that describe the difference between initial and final section snapshots.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```objc
@property (nonatomic, readonly) NSOrderedCollectionDifference<id> * difference;
```

## See Also

### Accessing a transaction’s information
- [sectionIdentifier](./sectionidentifier.md)
  The identifier of the section for the transaction.
- [initialSnapshot](./initialsnapshot.md)
  The section snapshot before the transaction occured.
- [finalSnapshot](./finalsnapshot.md)
  The section snapshot after the transaction occured.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesectiontransaction-c.class/difference)*
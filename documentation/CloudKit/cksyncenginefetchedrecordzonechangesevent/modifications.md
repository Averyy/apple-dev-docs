# modifications

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The fetched record modifications.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```objc
@property (nonatomic, copy, readonly) NSArray<CKRecord *> * modifications;
```

## See Also

### Accessing changes
- [deletions](./deletions.md)
  The fetched record deletions.
- [CKSyncEngineFetchedRecordDeletion](../cksyncenginefetchedrecorddeletion.md)
  An object that describes the deletion of an individual record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncenginefetchedrecordzonechangesevent/modifications)*
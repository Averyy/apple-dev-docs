# initWithRecordIDs:

**Framework**: CloudKit  
**Kind**: method  
**Role**: Instance Method

Creates a scope that includes only the given record IDs. If `recordIDs` is nil, this scope contains all records.

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
- (instancetype) initWithRecordIDs:(NSSet<CKRecordID *> *) recordIDs;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncenginesendchangesscope/initwithrecordids:)*
# CKSyncEngineSendChangesScope

**Framework**: CloudKit  
**Kind**: class  
**Role**: Class

A scope in which the sync engine will send changes to the server.

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
@interface CKSyncEngineSendChangesScope : NSObject
```

## Topics

### Instance Properties
- [excludedZoneIDs](./cksyncenginesendchangesscope/excludedzoneids.md)
  A specific set of zone IDs to exclude from this scope. If you know that you don’t want to send changes for a particular set of zones, you can set those zones here.
- [recordIDs](./cksyncenginesendchangesscope/recordids.md)
  The scope of record IDs in which to send changes.
- [zoneIDs](./cksyncenginesendchangesscope/zoneids.md)
  The scope of zone IDs in which to send changes.
### Instance Methods
- [- containsPendingRecordZoneChange:](./cksyncenginesendchangesscope/containspendingrecordzonechange_.md)
  Returns true if this scope includes the given pending change.
- [- containsRecordID:](./cksyncenginesendchangesscope/containsrecordid_.md)
  Returns true if this scope includes the given record ID.
- [- initWithExcludedZoneIDs:](./cksyncenginesendchangesscope/initwithexcludedzoneids_.md)
  Creates a scope that contains all zones except for the given zone IDs.
- [- initWithRecordIDs:](./cksyncenginesendchangesscope/initwithrecordids_.md)
  Creates a scope that includes only the given record IDs. If `recordIDs` is nil, this scope contains all records.
- [- initWithZoneIDs:](./cksyncenginesendchangesscope/initwithzoneids_.md)
  Creates a scope that contains only the given zone IDs. If `zoneIDs` is `nil`, then this scope contains all zones.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [NSCopying](../Foundation/nscopying.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksyncenginesendchangesscope)*
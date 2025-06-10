# CKQueryOperation.Cursor

**Framework**: CloudKit  
**Kind**: class

An object that marks the stopping point for a query and the starting point for retrieving the remaining results.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class Cursor
```

#### Overview

You don’t create instances of this class yourself. When fetching records using a query operation, if the number of results exceeds the limit for the query, CloudKit provides a cursor. Use that cursor to create a new instance of [`CKQueryOperation`](ckqueryoperation.md) and retrieve the next batch of results for the same query.

For information about how to use a [`CKQueryOperation.Cursor`](ckqueryoperation/cursor-swift.class.md) object, see [`CKQueryOperation`](ckqueryoperation.md).

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var query: CKQuery?](ckqueryoperation/query.md)
  The query for the search.
- [var cursor: CKQueryOperation.Cursor?](ckqueryoperation/cursor-swift.property.md)
  The  cursor for continuing the search.
- [var zoneID: CKRecordZone.ID?](ckqueryoperation/zoneid.md)
  The ID of the record zone that contains the records to search.
- [var resultsLimit: Int](ckqueryoperation/resultslimit.md)
  The maximum number of records to return at one time.
- [class let maximumResults: Int](ckqueryoperation/maximumresults.md)
  A constant value that represents the maximum number of results CloudKit retrieves.
- [var desiredKeys: [CKRecord.FieldKey]?](ckqueryoperation/desiredkeys-7qrse.md)
  The fields of the records to fetch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckqueryoperation/cursor-swift.class)*
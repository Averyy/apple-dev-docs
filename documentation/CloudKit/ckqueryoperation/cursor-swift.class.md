# CKQueryOperation.Cursor

**Framework**: CloudKit  
**Kind**: class  
**Role**: Class

An object that marks the stopping point for a query and the starting point for retrieving the remaining results.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class Cursor
```

```objc
@interface CKQueryCursor : NSObject
```

#### Overview

You don’t create instances of this class yourself. When fetching records using a query operation, if the number of results exceeds the limit for the query, CloudKit provides a cursor. Use that cursor to create a new instance of [`CKQueryOperation`](../ckqueryoperation.md) and retrieve the next batch of results for the same query.

For information about how to use a [`CKQueryOperation.Cursor`](./cursor-swift.class.md) object, see [`CKQueryOperation`](../ckqueryoperation.md).

## Topics

### Initializers
- [init?(coder: NSCoder)](./cursor-swift.class/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSCoding](../../Foundation/nscoding.md)
- [NSCopying](../../Foundation/nscopying.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../../Foundation/nssecurecoding.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring the Query Operation
- [var query: CKQuery?](./query.md)
  The query for the search.
- [var cursor: CKQueryOperation.Cursor?](./cursor-swift.property.md)
  The cursor for continuing the search.
- [var zoneID: CKRecordZone.ID?](./zoneid.md)
  The ID of the record zone that contains the records to search.
- [var resultsLimit: Int](./resultslimit.md)
  The maximum number of records to return at one time.
- [class let maximumResults: Int](./maximumresults.md)
  A constant value that represents the maximum number of results CloudKit retrieves.
- [var desiredKeys: [CKRecord.FieldKey]?](./desiredkeys-7qrse.md)
  The fields of the records to fetch.
- [desiredKeys](./desiredkeys-4a6vy.md)
  The fields of the records to fetch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckqueryoperation/cursor-swift.class)*
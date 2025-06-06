# default()

**Framework**: CloudKit  
**Kind**: method

Returns the default record zone.

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
class func `default`() -> CKRecordZone
```

#### Discussion

Always use this method to retrieve the default zone for a database. You can use the returned object to specify the default zone for either the public or private database of a container. You don’t need to save the returned zone object before using it. The owner of the zone is [`CKOwnerDefaultName`](ckownerdefaultname.md), which corresponds to the current user.

The default zone of a database is a convenient place to store and access records. If you don’t explicitly assign a zone to a record, CloudKit puts the record in the default zone.

The disadvantage of using the default zone for storing records is that it doesn’t have any special capabilities. You can’t save a group of records to iCloud atomically in the default zone. Similarly, you can’t use a [`CKFetchRecordChangesOperation`](ckfetchrecordchangesoperation.md) object on records in the default zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecordzone/default())*
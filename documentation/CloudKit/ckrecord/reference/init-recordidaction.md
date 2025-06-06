# init(recordID:action:)

**Framework**: CloudKit  
**Kind**: init

Creates a reference object that points to the record with the specified ID.

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
init(recordID: CKRecord.ID, action: CKRecord.ReferenceAction)
```

#### Return Value

An initialized reference object that points to the specified record, or `nil` if CloudKit can’t initialize the reference.

#### Discussion

Use this method when you have only the ID of the record for the target of a link. You might use this method if you save only the ID of the record to a local data cache.

When you create a reference object for use in a search predicate, the predicate ignores the value in the `action` parameter. Search predicates use only the ID of the record during their comparison.

## Parameters

- `recordID`: The ID of the target record. This method throws an exception if you specify   for this parameter.
- `action`: The ownership option use between the target record and any records that incorporate this reference object. If you specify the   option, the record that the   parameter references becomes the owner of (or acts as the parent of) any objects that use this reference object. For a list of possible values, see  .

## See Also

- [convenience init(record: CKRecord, action: CKRecord.ReferenceAction)](ckrecord/reference/init(record:action:).md)
  Creates a reference object that points to the specified record object.
- [CKRecord.Reference.Action](ckrecord/reference/action-swift.typealias.md)
  A type that represents additional actions that occur when deleting references.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecord/reference/init(recordid:action:))*
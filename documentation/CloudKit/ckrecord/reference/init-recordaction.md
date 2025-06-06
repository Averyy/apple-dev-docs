# init(record:action:)

**Framework**: CloudKit  
**Kind**: init

Creates a reference object that points to the specified record object.

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
convenience init(record: CKRecord, action: CKRecord.ReferenceAction)
```

#### Return Value

An initialized reference object that points to the specified record, or `nil` if CloudKit can’t initialize the reference.

#### Discussion

Use this method to initialize a reference to a local record object. The local record can be one that you create or one that you fetch from the server.

When you create a reference object for use in a search predicate, the predicate ignores the value in the `action` parameter. Search predicates use only the ID of the record during their comparison.

## Parameters

- `record`: The target record of the reference.
- `action`: The ownership options to use for the records. If you specify the   option, the object that the   parameter references becomes the owner of (or acts as the parent of) any objects that use this reference object. For a list of possible values, see  .

## See Also

- [init(recordID: CKRecord.ID, action: CKRecord.ReferenceAction)](ckrecord/reference/init(recordid:action:).md)
  Creates a reference object that points to the record with the specified ID.
- [CKRecord.Reference.Action](ckrecord/reference/action-swift.typealias.md)
  A type that represents additional actions that occur when deleting references.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecord/reference/init(record:action:))*
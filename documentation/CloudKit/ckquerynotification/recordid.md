# recordID

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The ID of the record that CloudKit creates, updates, or deletes.

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
@NSCopying
var recordID: CKRecord.ID? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) CKRecordID * recordID;
```

## Discussion

Use this value to fetch the record.

## See Also

### Getting the Record Information
- [var recordFields: [String : Any]?](./recordfields.md)
  A dictionary of fields that have changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckquerynotification/recordid)*
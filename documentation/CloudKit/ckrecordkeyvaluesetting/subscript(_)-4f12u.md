# subscript(_:)

**Framework**: CloudKit  
**Kind**: subscript  
**Role**: Instance Subscript

Accesses the value for the specified key in the record.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS
- watchOS 3.0+

## Declaration

```swift
@nonobjc
subscript<T>(key: CKRecord.FieldKey) -> T? where T : CKRecordValueProtocol { get set }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckrecordkeyvaluesetting/subscript(_:)-4f12u)*
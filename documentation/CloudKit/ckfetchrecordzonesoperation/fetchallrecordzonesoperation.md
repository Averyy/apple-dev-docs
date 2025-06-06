# fetchAllRecordZonesOperation()

**Framework**: CloudKit  
**Kind**: method

Returns an operation for fetching all record zones in the current database.

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
class func fetchAllRecordZonesOperation() -> Self
```

#### Discussion

Assign a value to the [`fetchRecordZonesCompletionBlock`](ckfetchrecordzonesoperation/fetchrecordzonescompletionblock.md) property of the operation that this method returns so that you can process the results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonesoperation/fetchallrecordzonesoperation())*
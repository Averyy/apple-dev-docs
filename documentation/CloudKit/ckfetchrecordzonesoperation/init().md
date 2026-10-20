# init()

**Framework**: CloudKit  
**Kind**: init  
**Role**: Initializer

Creates an empty fetch zones operation.

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
init()
```

```objc
- (instancetype) init;
```

#### Discussion

You must set the [`recordZoneIDs`](./recordzoneids.md) property before you execute the operation.

After creating the operation, assign a value to the [`fetchRecordZonesCompletionBlock`](./fetchrecordzonescompletionblock.md) property so you can process the results.

## See Also

### Initializing the Zone Fetch Operation
- [convenience init(recordZoneIDs: [CKRecordZone.ID])](./init%28recordzoneids%29.md)
  Creates an operation for fetching the specified record zones.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonesoperation/init())*
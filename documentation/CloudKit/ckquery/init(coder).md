# init(coder:)

**Framework**: CloudKit  
**Kind**: init  
**Role**: Initializer

Creates a query from a serialized instance.

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
init(coder aDecoder: NSCoder)
```

```objc
- (instancetype) initWithCoder:(NSCoder *) aDecoder;
```

## Parameters

- `aDecoder`: The coder to use when deserializing the query.

## See Also

### Creating a Query
- [convenience init(recordType: CKRecord.RecordType, predicate: NSPredicate)](./init%28recordtype,predicate%29.md)
  Creates a query with the specified record type and predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/ckquery/init(coder:))*
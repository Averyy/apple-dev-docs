# update(withValues:version:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Update the values and version to reflect new data being saved to or loaded from the external store.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func update(withValues values: [String : Any], version: UInt64)
```

```objc
- (void) updateWithValues:(NSDictionary<NSString *,id> *) values version:(uint64_t) version;
```

## Discussion

Update the values and version to reflect new data being saved to or loaded from the external store.  // The values dictionary is in the same format as the initializer

## Parameters

- `values`: A dictionary containing updated values, in the same format as that described in [`init(objectID:withValues:version:)`](./init%28objectid,withvalues,version%29.md).
- `version`: The version number for the transaction.

## See Also

### Managing Node Data
- [var objectID: NSManagedObjectID](./objectid.md)
  The object ID that identifies the data stored by the receiver.
- [func value(for: NSPropertyDescription) -> Any?](./value%28for%29.md)
  Returns the value for the given property.
- [var version: UInt64](./version.md)
  The version of data in the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsincrementalstorenode/update(withvalues:version:))*
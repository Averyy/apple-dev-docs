# update(withValues:version:)

**Framework**: Core Data  
**Kind**: method

Update the values and version to reflect new data being saved to or loaded from the external store.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func update(withValues values: [String : Any], version: UInt64)
```

#### Discussion

Update the values and version to reflect new data being saved to or loaded from the external store.  // The values dictionary is in the same format as the initializer

## Parameters

- `values`: A dictionary containing updated values, in the same format as that described in  .
- `version`: The version number for the transaction.

## See Also

- [var objectID: NSManagedObjectID](nsincrementalstorenode/objectid.md)
  The object ID that identifies the data stored by the receiver.
- [func value(for: NSPropertyDescription) -> Any?](nsincrementalstorenode/value(for:).md)
  Returns the value for the given property.
- [var version: UInt64](nsincrementalstorenode/version.md)
  The version of data in the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsincrementalstorenode/update(withvalues:version:))*
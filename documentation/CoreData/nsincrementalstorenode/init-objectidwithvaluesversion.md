# init(objectID:withValues:version:)

**Framework**: Core Data  
**Kind**: init

Returns an object initialized with the given values.

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
init(objectID: NSManagedObjectID, withValues values: [String : Any], version: UInt64)
```

#### Return Value

An object initialized with the given values.

## Parameters

- `objectID`: A managed object ID.
- `values`: Unknown or unmodeled keys are stripped out.
- `version`: The revision number of this state. This value is used for conflict detection and merging.

## See Also

- [Incremental Store Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/IncrementalStorePG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010706)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsincrementalstorenode/init(objectid:withvalues:version:))*
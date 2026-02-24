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
- `values`: A dictionary containing the values persisted in an external store with keys corresponding to the names of the property description in the `NSEntityDescription` object described by `objectID`: - For attributes: an immutable value (an instance of a value class such as `NSNumber`, `NSString`, `NSData`). Missing attribute keys will assume a nil value.
- For to-one relationships: the managed object ID of the related object or an instance of `NSNull` for nil relationship values. A missing key will be resolved lazily through calling `newValueForRelationship:forObjectWithID:withContext:error:` on the `NSPersistentStore` object. Lazy resolution for to-one relationships is discouraged.
- For to-many relationships: an instance of `NSArray` or `NSSet` containing the managed object IDs of the related objects. Empty to-many relationships must be represented by an empty non-nil collection. A missing key will be resolved lazily through calling `newValueForRelationship:forObjectWithID:withContext:error:` on the `NSPersistentStore` object. Lazy resolution for to-many relationships is encouraged. Unknown or unmodeled keys are stripped out.
- `version`: The revision number of this state. This value is used for conflict detection and merging.

## See Also

- [Incremental Store Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/IncrementalStorePG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010706)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsincrementalstorenode/init(objectid:withvalues:version:))*
# value(for:)

**Framework**: Core Data  
**Kind**: method

Returns the value for the given property.

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
func value(for prop: NSPropertyDescription) -> Any?
```

#### Return Value

The value for the property specified by `prop`. May return an instance of `NSNull` for to-one relationships.

#### Discussion

If a relationship is `nil`, you should create a new value by invoking `newValueForRelationship:forObjectWithID:withContext:error:` on the `NSPersistentStore` object.

## Parameters

- `prop`: A property description for one of the properties in the receiver.

## See Also

- [var objectID: NSManagedObjectID](nsincrementalstorenode/objectid.md)
  The object ID that identifies the data stored by the receiver.
- [func update(withValues: [String : Any], version: UInt64)](nsincrementalstorenode/update(withvalues:version:).md)
  Update the values and version to reflect new data being saved to or loaded from the external store.
- [var version: UInt64](nsincrementalstorenode/version.md)
  The version of data in the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsincrementalstorenode/value(for:))*
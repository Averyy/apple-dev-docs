# obtainPermanentIDs(for:)

**Framework**: Core Data  
**Kind**: method

Returns an array containing the object IDs for a given array of newly-inserted objects.

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
func obtainPermanentIDs(for array: [NSManagedObject]) throws -> [NSManagedObjectID]
```

#### Return Value

An array containing the object IDs for the objects in `array`.

#### Discussion

The returned array must return the object IDs in the same order as the objects appear in `array`.

#### Discussion

This method is called before [`execute(_:with:)`](nsincrementalstore/execute(_:with:).md) with a save request, to assign permanent IDs to newly-inserted objects.

## Parameters

- `array`: An array of newly-inserted objects.

## See Also

- [func execute(NSPersistentStoreRequest, with: NSManagedObjectContext?) throws -> Any](nsincrementalstore/execute(_:with:).md)
  Returns a value as appropriate for the given request, or nil if the request cannot be completed.
- [func newValuesForObject(with: NSManagedObjectID, with: NSManagedObjectContext) throws -> NSIncrementalStoreNode](nsincrementalstore/newvaluesforobject(with:with:).md)
  Returns an incremental store node encapsulating the persistent external values of the object with a given object ID.
- [func newValue(forRelationship: NSRelationshipDescription, forObjectWith: NSManagedObjectID, with: NSManagedObjectContext?) throws -> Any](nsincrementalstore/newvalue(forrelationship:forobjectwith:with:).md)
  Returns the relationship for the given relationship of the object with a given object ID.
- [func newObjectID(for: NSEntityDescription, referenceObject: Any) -> NSManagedObjectID](nsincrementalstore/newobjectid(for:referenceobject:).md)
  Returns a new object ID that uses given data as the key.
- [func referenceObject(for: NSManagedObjectID) -> Any](nsincrementalstore/referenceobject(for:).md)
  Returns the reference data used to construct a given object ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsincrementalstore/obtainpermanentids(for:))*
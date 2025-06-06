# referenceObject(for:)

**Framework**: Core Data  
**Kind**: method

Returns the reference data used to construct a given object ID.

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
func referenceObject(for objectID: NSManagedObjectID) -> Any
```

#### Return Value

The reference data used to construct objectID.

#### Discussion

This method raises an [`invalidArgumentException`](https://developer.apple.com/documentation/foundation/nsexceptionname/1415426-invalidargumentexception) if the object ID was not created by the receiving store.

You should not override this method.

## Parameters

- `objectID`: An object ID created by the receiver.

## See Also

- [func execute(NSPersistentStoreRequest, with: NSManagedObjectContext?) throws -> Any](nsincrementalstore/execute(_:with:).md)
  Returns a value as appropriate for the given request, or nil if the request cannot be completed.
- [func newValuesForObject(with: NSManagedObjectID, with: NSManagedObjectContext) throws -> NSIncrementalStoreNode](nsincrementalstore/newvaluesforobject(with:with:).md)
  Returns an incremental store node encapsulating the persistent external values of the object with a given object ID.
- [func newValue(forRelationship: NSRelationshipDescription, forObjectWith: NSManagedObjectID, with: NSManagedObjectContext?) throws -> Any](nsincrementalstore/newvalue(forrelationship:forobjectwith:with:).md)
  Returns the relationship for the given relationship of the object with a given object ID.
- [func obtainPermanentIDs(for: [NSManagedObject]) throws -> [NSManagedObjectID]](nsincrementalstore/obtainpermanentids(for:).md)
  Returns an array containing the object IDs for a given array of newly-inserted objects.
- [func newObjectID(for: NSEntityDescription, referenceObject: Any) -> NSManagedObjectID](nsincrementalstore/newobjectid(for:referenceobject:).md)
  Returns a new object ID that uses given data as the key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsincrementalstore/referenceobject(for:))*
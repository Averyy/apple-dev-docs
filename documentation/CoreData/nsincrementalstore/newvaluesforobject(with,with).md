# newValuesForObject(with:with:)

**Framework**: Core Data  
**Kind**: method

Returns an incremental store node encapsulating the persistent external values of the object with a given object ID.

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
func newValuesForObject(with objectID: NSManagedObjectID, with context: NSManagedObjectContext) throws -> NSIncrementalStoreNode
```

#### Return Value

An incremental store node encapsulating the persistent external values of the object with object ID `objectID`, or `nil` if the corresponding object cannot be found.

#### Discussion

The returned node should include all attributes values and may include to-one relationship values as instances of [`NSManagedObjectID`](nsmanagedobjectid.md).

If an object with object ID `objectID` cannot be found, the method should return `nil` and—if `error` is not `NULL`—create and return an appropriate error object in `error`.

## Parameters

- `objectID`: The ID of the object for which values are requested.
- `context`: The managed object context into which values will be returned.

## See Also

- [func execute(NSPersistentStoreRequest, with: NSManagedObjectContext?) throws -> Any](nsincrementalstore/execute(_:with:).md)
  Returns a value as appropriate for the given request, or nil if the request cannot be completed.
- [func newValue(forRelationship: NSRelationshipDescription, forObjectWith: NSManagedObjectID, with: NSManagedObjectContext?) throws -> Any](nsincrementalstore/newvalue(forrelationship:forobjectwith:with:).md)
  Returns the relationship for the given relationship of the object with a given object ID.
- [func obtainPermanentIDs(for: [NSManagedObject]) throws -> [NSManagedObjectID]](nsincrementalstore/obtainpermanentids(for:).md)
  Returns an array containing the object IDs for a given array of newly-inserted objects.
- [func newObjectID(for: NSEntityDescription, referenceObject: Any) -> NSManagedObjectID](nsincrementalstore/newobjectid(for:referenceobject:).md)
  Returns a new object ID that uses given data as the key.
- [func referenceObject(for: NSManagedObjectID) -> Any](nsincrementalstore/referenceobject(for:).md)
  Returns the reference data used to construct a given object ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsincrementalstore/newvaluesforobject(with:with:))*
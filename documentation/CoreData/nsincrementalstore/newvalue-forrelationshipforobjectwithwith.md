# newValue(forRelationship:forObjectWith:with:)

**Framework**: Core Data  
**Kind**: method

Returns the relationship for the given relationship of the object with a given object ID.

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
func newValue(forRelationship relationship: NSRelationshipDescription, forObjectWith objectID: NSManagedObjectID, with context: NSManagedObjectContext?) throws -> Any
```

#### Return Value

The value of the relationship specified `relationship` of the object with object ID `objectID`, or `nil` if an error occurs.

#### Discussion

If the relationship is a to-one, the method should return an [`NSManagedObjectID`](nsmanagedobjectid.md) instance that identifies the destination, or an instance of [`NSNull`](https://developer.apple.com/documentation/Foundation/NSNull) if the relationship value is `nil`.

If the relationship is a to-many, the method should return a collection object containing [`NSManagedObjectID`](nsmanagedobjectid.md) instances to identify the related objects. Using an `NSArray` instance is preferred because it will be the most efficient. A store may also return an instance of `NSSet` or `NSOrderedSet`; an instance of `NSDictionary` is not acceptable.

If an object with object ID `objectID` cannot be found, the method should return `nil` and—if `error` is not `NULL`—create and return an appropriate error object in `error`.

## Parameters

- `relationship`: The relationship for which values are requested.
- `objectID`: The ID of the object for which values are requested.
- `context`: The managed object context into which values will be returned.

## See Also

- [func execute(NSPersistentStoreRequest, with: NSManagedObjectContext?) throws -> Any](nsincrementalstore/execute(_:with:).md)
  Returns a value as appropriate for the given request, or nil if the request cannot be completed.
- [func newValuesForObject(with: NSManagedObjectID, with: NSManagedObjectContext) throws -> NSIncrementalStoreNode](nsincrementalstore/newvaluesforobject(with:with:).md)
  Returns an incremental store node encapsulating the persistent external values of the object with a given object ID.
- [func obtainPermanentIDs(for: [NSManagedObject]) throws -> [NSManagedObjectID]](nsincrementalstore/obtainpermanentids(for:).md)
  Returns an array containing the object IDs for a given array of newly-inserted objects.
- [func newObjectID(for: NSEntityDescription, referenceObject: Any) -> NSManagedObjectID](nsincrementalstore/newobjectid(for:referenceobject:).md)
  Returns a new object ID that uses given data as the key.
- [func referenceObject(for: NSManagedObjectID) -> Any](nsincrementalstore/referenceobject(for:).md)
  Returns the reference data used to construct a given object ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsincrementalstore/newvalue(forrelationship:forobjectwith:with:))*
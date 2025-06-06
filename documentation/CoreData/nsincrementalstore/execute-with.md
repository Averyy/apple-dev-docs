# execute(_:with:)

**Framework**: Core Data  
**Kind**: method

Returns a value as appropriate for the given request, or nil if the request cannot be completed.

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
func execute(_ request: NSPersistentStoreRequest, with context: NSManagedObjectContext?) throws -> Any
```

#### Return Value

A value as appropriate for `request`, or `nil` if the request cannot be completed

#### Discussion

The value to return depends on the result type (see [`resultType`](nsfetchrequest/resulttype.md)) of `request`:

- If it is `NSManagedObjectResultType`, `NSManagedObjectIDResultType`, or `NSDictionaryResultType`, the method should return an array containing all objects in the store matching the request.
- If it is `NSCountResultType`, the method should return an array containing an `NSNumber` whose value is the count of all objects in the store matching the request.
- If the request is a save request, the method should return an empty array.

If the save request contains nil values for the inserted/updated/deleted/locked collections; you should treat it as a request to save the store metadata.

You should implement this method conservatively, and expect that unknown request types may at some point be passed to the method. The correct behavior in these cases is to return `nil` and an error.

## Parameters

- `request`: A fetch request.
- `context`: The managed object context used to execute  .

## See Also

- [func newValuesForObject(with: NSManagedObjectID, with: NSManagedObjectContext) throws -> NSIncrementalStoreNode](nsincrementalstore/newvaluesforobject(with:with:).md)
  Returns an incremental store node encapsulating the persistent external values of the object with a given object ID.
- [func newValue(forRelationship: NSRelationshipDescription, forObjectWith: NSManagedObjectID, with: NSManagedObjectContext?) throws -> Any](nsincrementalstore/newvalue(forrelationship:forobjectwith:with:).md)
  Returns the relationship for the given relationship of the object with a given object ID.
- [func obtainPermanentIDs(for: [NSManagedObject]) throws -> [NSManagedObjectID]](nsincrementalstore/obtainpermanentids(for:).md)
  Returns an array containing the object IDs for a given array of newly-inserted objects.
- [func newObjectID(for: NSEntityDescription, referenceObject: Any) -> NSManagedObjectID](nsincrementalstore/newobjectid(for:referenceobject:).md)
  Returns a new object ID that uses given data as the key.
- [func referenceObject(for: NSManagedObjectID) -> Any](nsincrementalstore/referenceobject(for:).md)
  Returns the reference data used to construct a given object ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsincrementalstore/execute(_:with:))*
# referenceObject(for:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Returns the reference data used to construct a given object ID.

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
func referenceObject(for objectID: NSManagedObjectID) -> Any
```

```objc
- (id) referenceObjectForObjectID:(NSManagedObjectID *) objectID;
```

#### Return Value

The reference data used to construct objectID.

#### Discussion

This method raises an [`invalidArgumentException`](../../Foundation/nsexceptionname/invalidargumentexception.md) if the object ID was not created by the receiving store.

You should not override this method.

## Parameters

- `objectID`: An object ID created by the receiver.

## See Also

### Manipulating Managed Objects
- [func execute(NSPersistentStoreRequest, with: NSManagedObjectContext?) throws -> Any](./execute%28_,with%29.md)
  Returns a value as appropriate for the given request, or nil if the request cannot be completed.
- [func newValuesForObject(with: NSManagedObjectID, with: NSManagedObjectContext) throws -> NSIncrementalStoreNode](./newvaluesforobject%28with,with%29.md)
  Returns an incremental store node encapsulating the persistent external values of the object with a given object ID.
- [func newValue(forRelationship: NSRelationshipDescription, forObjectWith: NSManagedObjectID, with: NSManagedObjectContext?) throws -> Any](./newvalue%28forrelationship,forobjectwith,with%29.md)
  Returns the relationship for the given relationship of the object with a given object ID.
- [func obtainPermanentIDs(for: [NSManagedObject]) throws -> [NSManagedObjectID]](./obtainpermanentids%28for%29.md)
  Returns an array containing the object IDs for a given array of newly-inserted objects.
- [func newObjectID(for: NSEntityDescription, referenceObject: Any) -> NSManagedObjectID](./newobjectid%28for,referenceobject%29.md)
  Returns a new object ID that uses given data as the key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsincrementalstore/referenceobject(for:))*
# newObjectID(for:referenceObject:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Returns a new object ID that uses given data as the key.

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
func newObjectID(for entity: NSEntityDescription, referenceObject data: Any) -> NSManagedObjectID
```

```objc
- (NSManagedObjectID *) newObjectIDForEntity:(NSEntityDescription *) entity referenceObject:(id) data;
```

#### Return Value

A new object ID for an instance of the entity specified by `entity` and that uses `data` as the key.

#### Discussion

You should not override this method.

## Parameters

- `entity`: The entity for the new object ID.
- `data`: An object of type [`NSString`](../../Foundation/nsstring.md) or [`NSNumber`](../../Foundation/nsnumber.md) to use as the key.

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
- [func referenceObject(for: NSManagedObjectID) -> Any](./referenceobject%28for%29.md)
  Returns the reference data used to construct a given object ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsincrementalstore/newobjectid(for:referenceobject:))*
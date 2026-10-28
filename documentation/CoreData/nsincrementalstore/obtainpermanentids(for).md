# obtainPermanentIDs(for:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Returns an array containing the object IDs for a given array of newly-inserted objects.

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
func obtainPermanentIDs(for array: [NSManagedObject]) throws -> [NSManagedObjectID]
```

```objc
- (NSArray<NSManagedObjectID *> *) obtainPermanentIDsForObjects:(NSArray<NSManagedObject *> *) array error:(NSError **) error;
```

## Return Value

An array containing the object IDs for the objects in `array`.

## Discussion

The returned array must return the object IDs in the same order as the objects appear in `array`.

## Discussion

This method is called before [`execute(_:with:)`](./execute%28_,with%29.md) with a save request, to assign permanent IDs to newly-inserted objects.

## Parameters

- `array`: An array of newly-inserted objects.

## See Also

### Manipulating Managed Objects
- [func execute(NSPersistentStoreRequest, with: NSManagedObjectContext?) throws -> Any](./execute%28_,with%29.md)
  Returns a value as appropriate for the given request, or nil if the request cannot be completed.
- [func newValuesForObject(with: NSManagedObjectID, with: NSManagedObjectContext) throws -> NSIncrementalStoreNode](./newvaluesforobject%28with,with%29.md)
  Returns an incremental store node encapsulating the persistent external values of the object with a given object ID.
- [func newValue(forRelationship: NSRelationshipDescription, forObjectWith: NSManagedObjectID, with: NSManagedObjectContext?) throws -> Any](./newvalue%28forrelationship,forobjectwith,with%29.md)
  Returns the relationship for the given relationship of the object with a given object ID.
- [func newObjectID(for: NSEntityDescription, referenceObject: Any) -> NSManagedObjectID](./newobjectid%28for,referenceobject%29.md)
  Returns a new object ID that uses given data as the key.
- [func referenceObject(for: NSManagedObjectID) -> Any](./referenceobject%28for%29.md)
  Returns the reference data used to construct a given object ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsincrementalstore/obtainpermanentids(for:))*
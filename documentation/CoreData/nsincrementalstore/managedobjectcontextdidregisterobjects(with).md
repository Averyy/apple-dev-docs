# managedObjectContextDidRegisterObjects(with:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Indicates that objects identified by a given array of object IDs are in use in a managed object context.

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
func managedObjectContextDidRegisterObjects(with objectIDs: [NSManagedObjectID])
```

```objc
- (void) managedObjectContextDidRegisterObjectsWithIDs:(NSArray<NSManagedObjectID *> *) objectIDs;
```

#### Discussion

This method and [`managedObjectContextDidUnregisterObjects(with:)`](./managedobjectcontextdidunregisterobjects%28with%29.md) allow managed object contexts to communicate interest in the row data of specific objects in a manner akin to reference counting. For more details, see [`managedObjectContextDidUnregisterObjects(with:)`](./managedobjectcontextdidunregisterobjects%28with%29.md).

## Parameters

- `objectIDs`: An array of object IDs.

## See Also

### Responding to Context Changes
- [func managedObjectContextDidUnregisterObjects(with: [NSManagedObjectID])](./managedobjectcontextdidunregisterobjects%28with%29.md)
  Indicates that objects identified by a given array of object IDs are no longer being used by a managed object context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsincrementalstore/managedobjectcontextdidregisterobjects(with:))*
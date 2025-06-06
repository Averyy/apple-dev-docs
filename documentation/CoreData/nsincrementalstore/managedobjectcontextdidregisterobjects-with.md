# managedObjectContextDidRegisterObjects(with:)

**Framework**: Core Data  
**Kind**: method

Indicates that objects identified by a given array of object IDs are in use in a managed object context.

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
func managedObjectContextDidRegisterObjects(with objectIDs: [NSManagedObjectID])
```

#### Discussion

This method and [`managedObjectContextDidUnregisterObjects(with:)`](nsincrementalstore/managedobjectcontextdidunregisterobjects(with:).md) allow managed object contexts to communicate interest in the row data of specific objects in a manner akin to reference counting. For more details, see [`managedObjectContextDidUnregisterObjects(with:)`](nsincrementalstore/managedobjectcontextdidunregisterobjects(with:).md).

## Parameters

- `objectIDs`: An array of object IDs.

## See Also

- [func managedObjectContextDidUnregisterObjects(with: [NSManagedObjectID])](nsincrementalstore/managedobjectcontextdidunregisterobjects(with:).md)
  Indicates that objects identified by a given array of object IDs are no longer being used by a managed object context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsincrementalstore/managedobjectcontextdidregisterobjects(with:))*
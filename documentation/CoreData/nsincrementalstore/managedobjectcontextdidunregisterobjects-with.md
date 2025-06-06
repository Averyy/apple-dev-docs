# managedObjectContextDidUnregisterObjects(with:)

**Framework**: Core Data  
**Kind**: method

Indicates that objects identified by a given array of object IDs are no longer being used by a managed object context.

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
func managedObjectContextDidUnregisterObjects(with objectIDs: [NSManagedObjectID])
```

#### Discussion

This method is the counterpart to [`managedObjectContextDidRegisterObjects(with:)`](nsincrementalstore/managedobjectcontextdidregisterobjects(with:).md).

Passing an object ID in the object IDs array of [`managedObjectContextDidRegisterObjects(with:)`](nsincrementalstore/managedobjectcontextdidregisterobjects(with:).md) is akin to incrementing the object ID’s reference count by 1; passing an object ID in the object IDs array of [`managedObjectContextDidUnregisterObjects(with:)`](nsincrementalstore/managedobjectcontextdidunregisterobjects(with:).md) is akin to decrementing the object ID’s reference count by 1. It is only when an object ID’s reference count is 0 that no contexts indicate that they are using the corresponding managed object. (Object IDs start with a reference count of 0.)

For example, if the register methods is invoked on two occasions when the object IDs array contains a given object ID, and the unregister method is invoked once when the object IDs array contains that object ID, then a context is still using the object with the given ID.

## Parameters

- `objectIDs`: An array of object IDs.

## See Also

- [func managedObjectContextDidRegisterObjects(with: [NSManagedObjectID])](nsincrementalstore/managedobjectcontextdidregisterobjects(with:).md)
  Indicates that objects identified by a given array of object IDs are in use in a managed object context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsincrementalstore/managedobjectcontextdidunregisterobjects(with:))*
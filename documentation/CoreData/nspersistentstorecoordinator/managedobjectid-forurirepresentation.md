# managedObjectID(forURIRepresentation:)

**Framework**: Core Data  
**Kind**: method

Returns the object identifier for the specified URI representation.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func managedObjectID(forURIRepresentation url: URL) -> NSManagedObjectID?
```

#### Return Value

An object ID for the object specified by `url`.

#### Discussion

The URI representation contains a UUID of the store the ID is coming from, and the coordinator can match it against the stores added to it.

## Parameters

- `url`: An URL object containing a URI that specify a managed object.

## See Also

- [func object(with: NSManagedObjectID) -> NSManagedObject](nsmanagedobjectcontext/object(with:).md)
  Returns either an existing object from the context or a fault that represents that object.
- [func uriRepresentation() -> URL](nsmanagedobjectid/urirepresentation.md)
  Returns a URI that provides an archiveable reference to the object for the object ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/managedobjectid(forurirepresentation:))*
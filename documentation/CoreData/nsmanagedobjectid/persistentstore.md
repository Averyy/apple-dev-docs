# persistentStore

**Framework**: Core Data  
**Kind**: property

The persistent store that fetched the object for the object ID.

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
weak var persistentStore: NSPersistentStore? { get }
```

#### Discussion

`nil` if the ID is for a newly-inserted object that has not yet been saved to a persistent store.

## See Also

- [var entity: NSEntityDescription](nsmanagedobjectid/entity.md)
  The entity description associated with the object ID.
- [var isTemporaryID: Bool](nsmanagedobjectid/istemporaryid.md)
  A Boolean value that indicates whether the object ID is temporary.
- [func uriRepresentation() -> URL](nsmanagedobjectid/urirepresentation.md)
  Returns a URI that provides an archiveable reference to the object for the object ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectid/persistentstore)*
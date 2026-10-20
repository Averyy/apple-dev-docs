# persistentStore

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The persistent store that fetched the object for the object ID.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
weak var persistentStore: NSPersistentStore? { get }
```

```objc
@property (weak, readonly, nullable) NSPersistentStore * persistentStore;
```

#### Discussion

`nil` if the ID is for a newly-inserted object that has not yet been saved to a persistent store.

## See Also

### Getting Managed Object ID Information
- [var entity: NSEntityDescription](./entity.md)
  The entity description associated with the object ID.
- [var isTemporaryID: Bool](./istemporaryid.md)
  A Boolean value that indicates whether the object ID is temporary.
- [func uriRepresentation() -> URL](./urirepresentation%28%29.md)
  Returns a URI that provides an archiveable reference to the object for the object ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectid/persistentstore)*
# isTemporaryID

**Framework**: Core Data  
**Kind**: property

A Boolean value that indicates whether the object ID is temporary.

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
var isTemporaryID: Bool { get }
```

#### Discussion

[`true`](https://developer.apple.com/documentation/swift/true) if the receiver is temporary, otherwise [`false`](https://developer.apple.com/documentation/swift/false). Most object IDs return [`false`](https://developer.apple.com/documentation/swift/false). New objects inserted into a managed object context are assigned a temporary ID which is replaced with a permanent one once the object gets saved to a persistent store.

## See Also

- [var entity: NSEntityDescription](nsmanagedobjectid/entity.md)
  The entity description associated with the object ID.
- [var persistentStore: NSPersistentStore?](nsmanagedobjectid/persistentstore.md)
  The persistent store that fetched the object for the object ID.
- [func uriRepresentation() -> URL](nsmanagedobjectid/urirepresentation.md)
  Returns a URI that provides an archiveable reference to the object for the object ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectid/istemporaryid)*
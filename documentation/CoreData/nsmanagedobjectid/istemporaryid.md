# isTemporaryID

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the object ID is temporary.

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
var isTemporaryID: Bool { get }
```

```objc
@property (readonly, getter=isTemporaryID) BOOL temporaryID;
```

## Discussion

[`true`](../../Swift/true.md) if the receiver is temporary, otherwise [`false`](../../Swift/false.md). Most object IDs return [`false`](../../Swift/false.md). New objects inserted into a managed object context are assigned a temporary ID which is replaced with a permanent one once the object gets saved to a persistent store.

## See Also

### Getting Managed Object ID Information
- [var entity: NSEntityDescription](./entity.md)
  The entity description associated with the object ID.
- [var persistentStore: NSPersistentStore?](./persistentstore.md)
  The persistent store that fetched the object for the object ID.
- [func uriRepresentation() -> URL](./urirepresentation%28%29.md)
  Returns a URI that provides an archiveable reference to the object for the object ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectid/istemporaryid)*
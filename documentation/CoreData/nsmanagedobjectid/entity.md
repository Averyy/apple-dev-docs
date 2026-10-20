# entity

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The entity description associated with the object ID.

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
var entity: NSEntityDescription { get }
```

```objc
@property (strong, readonly) NSEntityDescription * entity;
```

## See Also

### Related Documentation
- [Core Data Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/index.html#//apple_ref/doc/uid/TP40001075)
- [var entity: NSEntityDescription](../nsmanagedobject/entity-swift.property.md)
  The entity description of the managed object.
### Getting Managed Object ID Information
- [var isTemporaryID: Bool](./istemporaryid.md)
  A Boolean value that indicates whether the object ID is temporary.
- [var persistentStore: NSPersistentStore?](./persistentstore.md)
  The persistent store that fetched the object for the object ID.
- [func uriRepresentation() -> URL](./urirepresentation%28%29.md)
  Returns a URI that provides an archiveable reference to the object for the object ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectid/entity)*
# isTransient

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the receiver is transient.

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
var isTransient: Bool { get set }
```

```objc
@property (getter=isTransient) BOOL transient;
```

#### Discussion

[`true`](../../Swift/true.md) if the receiver is transient, otherwise [`false`](../../Swift/false.md). The transient flag specifies whether or not a property’s value is ignored when an object is saved to a persistent store. Transient properties are not saved to the persistent store, but are still managed for undo, redo, validation, and so on.

##### Special Considerations

Setting this property raises an exception if the receiver’s model has been used by an object graph manager.

## See Also

### Accessing Features of a Property
- [var entity: NSEntityDescription](./entity.md)
  The entity description of the receiver.
- [var isIndexed: Bool](./isindexed.md)
  A Boolean value that indicates whether the receiver should be indexed for searching.
- [var isOptional: Bool](./isoptional.md)
  A Boolean value that indicates whether the receiver is optional.
- [var name: String](./name.md)
  The name of the receiver.
- [var userInfo: [AnyHashable : Any]?](./userinfo.md)
  The user info dictionary of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspropertydescription/istransient)*
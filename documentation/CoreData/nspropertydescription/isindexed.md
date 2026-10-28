# isIndexed

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the receiver should be indexed for searching.

**Availability**:
- iOS 3.0+ - Deprecated in 11.0
- iPadOS 3.0+ - Deprecated in 11.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.5+ - Deprecated in 10.13
- tvOS 9.0+ - Deprecated in 11.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 4.0

> **Deprecated**: Use NSEntityDescription.indexes instead

## Declaration

```swift
var isIndexed: Bool { get set }
```

```objc
@property (getter=isIndexed) BOOL indexed;
```

## Discussion

[`true`](../../Swift/true.md) if the receiver should be indexed for searching, otherwise [`false`](../../Swift/false.md). Object stores can optionally use this information upon store creation for operations such as defining indexes.

### Special Considerations

Setting this property raises an exception if the receiver’s model has been used by an object graph manager.

## See Also

### Accessing Features of a Property
- [var entity: NSEntityDescription](./entity.md)
  The entity description of the receiver.
- [var isOptional: Bool](./isoptional.md)
  A Boolean value that indicates whether the receiver is optional.
- [var isTransient: Bool](./istransient.md)
  A Boolean value that indicates whether the receiver is transient.
- [var name: String](./name.md)
  The name of the receiver.
- [var userInfo: [AnyHashable : Any]?](./userinfo.md)
  The user info dictionary of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspropertydescription/isindexed)*
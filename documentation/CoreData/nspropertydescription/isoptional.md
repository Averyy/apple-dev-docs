# isOptional

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the receiver is optional.

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
var isOptional: Bool { get set }
```

```objc
@property (getter=isOptional) BOOL optional;
```

#### Discussion

[`true`](../../Swift/true.md) if the receiver is optional, otherwise [`false`](../../Swift/false.md). The optionality flag specifies whether a property’s value can be `nil` before an object can be saved to a persistent store.

##### Special Considerations

Setting this property raises an exception if the receiver’s model has been used by an object graph manager.

## See Also

### Accessing Features of a Property
- [var entity: NSEntityDescription](./entity.md)
  The entity description of the receiver.
- [var isIndexed: Bool](./isindexed.md)
  A Boolean value that indicates whether the receiver should be indexed for searching.
- [var isTransient: Bool](./istransient.md)
  A Boolean value that indicates whether the receiver is transient.
- [var name: String](./name.md)
  The name of the receiver.
- [var userInfo: [AnyHashable : Any]?](./userinfo.md)
  The user info dictionary of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspropertydescription/isoptional)*
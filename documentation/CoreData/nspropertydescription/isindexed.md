# isIndexed

**Framework**: Core Data  
**Kind**: property

A Boolean value that indicates whether the receiver should be indexed for searching.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var isIndexed: Bool { get set }
```

#### Discussion

[`true`](https://developer.apple.com/documentation/swift/true) if the receiver should be indexed for searching, otherwise [`false`](https://developer.apple.com/documentation/swift/false). Object stores can optionally use this information upon store creation for operations such as defining indexes.

##### Special Considerations

Setting this property raises an exception if the receiver’s model has been used by an object graph manager.

## See Also

- [var entity: NSEntityDescription](nspropertydescription/entity.md)
  The entity description of the receiver.
- [var isOptional: Bool](nspropertydescription/isoptional.md)
  A Boolean value that indicates whether the receiver is optional.
- [var isTransient: Bool](nspropertydescription/istransient.md)
  A Boolean value that indicates whether the receiver is transient.
- [var name: String](nspropertydescription/name.md)
  The name of the receiver.
- [var userInfo: [AnyHashable : Any]?](nspropertydescription/userinfo.md)
  The user info dictionary of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspropertydescription/isindexed)*
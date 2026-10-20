# userInfo

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The user info dictionary of the receiver.

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
var userInfo: [AnyHashable : Any]? { get set }
```

```objc
@property (nonatomic, strong, nullable) NSDictionary * userInfo;
```

#### Discussion

Setting the user info raises an exception if the receiver’s model has been used by an object graph manager.

## See Also

### Accessing Features of a Property
- [var entity: NSEntityDescription](./entity.md)
  The entity description of the receiver.
- [var isIndexed: Bool](./isindexed.md)
  A Boolean value that indicates whether the receiver should be indexed for searching.
- [var isOptional: Bool](./isoptional.md)
  A Boolean value that indicates whether the receiver is optional.
- [var isTransient: Bool](./istransient.md)
  A Boolean value that indicates whether the receiver is transient.
- [var name: String](./name.md)
  The name of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspropertydescription/userinfo)*
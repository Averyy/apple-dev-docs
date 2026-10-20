# entity

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The entity description of the receiver.

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
unowned(unsafe) var entity: NSEntityDescription { get }
```

```objc
@property (nonatomic, assign, readonly) NSEntityDescription * entity;
```

## See Also

### Related Documentation
- [Core Data Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/index.html#//apple_ref/doc/uid/TP40001075)
- [var properties: [NSPropertyDescription]](../nsentitydescription/properties.md)
  An array containing the properties of the receiver.
### Accessing Features of a Property
- [var isIndexed: Bool](./isindexed.md)
  A Boolean value that indicates whether the receiver should be indexed for searching.
- [var isOptional: Bool](./isoptional.md)
  A Boolean value that indicates whether the receiver is optional.
- [var isTransient: Bool](./istransient.md)
  A Boolean value that indicates whether the receiver is transient.
- [var name: String](./name.md)
  The name of the receiver.
- [var userInfo: [AnyHashable : Any]?](./userinfo.md)
  The user info dictionary of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspropertydescription/entity)*
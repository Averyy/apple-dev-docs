# name

**Framework**: Core Data  
**Kind**: property

The name of the receiver.

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
var name: String { get set }
```

#### Discussion

A property name cannot be the same as any no-parameter method name of `NSObject` or `NSManagedObject`. Since there are hundreds of methods on `NSObject` which may conflict with property names, you should avoid very general words (like “font”, and “color”) and words or phrases that overlap with Cocoa paradigms (such as “isEditing” and “objectSpecifier”).

##### Special Considerations

Setting the name raises an exception if the receiver’s model has been used by an object graph manager.

## See Also

- [var entity: NSEntityDescription](nspropertydescription/entity.md)
  The entity description of the receiver.
- [var isIndexed: Bool](nspropertydescription/isindexed.md)
  A Boolean value that indicates whether the receiver should be indexed for searching.
- [var isOptional: Bool](nspropertydescription/isoptional.md)
  A Boolean value that indicates whether the receiver is optional.
- [var isTransient: Bool](nspropertydescription/istransient.md)
  A Boolean value that indicates whether the receiver is transient.
- [var userInfo: [AnyHashable : Any]?](nspropertydescription/userinfo.md)
  The user info dictionary of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspropertydescription/name)*
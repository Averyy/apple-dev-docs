# subentities

**Framework**: Core Data  
**Kind**: property

An array containing the sub-entities of the receiver.

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
var subentities: [NSEntityDescription] { get set }
```

#### Discussion

The sub-entities are instances of `NSEntityDescription`.

##### Special Considerations

Setting the sub-entities raises an exception if the receiver’s model has been used by an object graph manager.

## See Also

- [var subentitiesByName: [String : NSEntityDescription]](nsentitydescription/subentitiesbyname.md)
  A dictionary containing the receiver’s sub-entities.
- [var superentity: NSEntityDescription?](nsentitydescription/superentity.md)
  The super-entity of the receiver.
- [func isKindOf(entity: NSEntityDescription) -> Bool](nsentitydescription/iskindof(entity:).md)
  Returns a Boolean value that indicates whether the receiver is a sub-entity of another given entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsentitydescription/subentities)*
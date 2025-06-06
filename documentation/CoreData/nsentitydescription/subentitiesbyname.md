# subentitiesByName

**Framework**: Core Data  
**Kind**: property

A dictionary containing the receiver’s sub-entities.

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
var subentitiesByName: [String : NSEntityDescription] { get }
```

#### Return Value

The keys in the dictionary are the sub-entity names, the corresponding values are instances of `NSEntityDescription`.

## See Also

- [var subentities: [NSEntityDescription]](nsentitydescription/subentities.md)
  An array containing the sub-entities of the receiver.
- [var superentity: NSEntityDescription?](nsentitydescription/superentity.md)
  The super-entity of the receiver.
- [func isKindOf(entity: NSEntityDescription) -> Bool](nsentitydescription/iskindof(entity:).md)
  Returns a Boolean value that indicates whether the receiver is a sub-entity of another given entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsentitydescription/subentitiesbyname)*
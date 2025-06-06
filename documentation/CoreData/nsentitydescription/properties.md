# properties

**Framework**: Core Data  
**Kind**: property

An array containing the properties of the receiver.

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
var properties: [NSPropertyDescription] { get set }
```

#### Discussion

The elements in the array are instances of [`NSAttributeDescription`](nsattributedescription.md), [`NSRelationshipDescription`](nsrelationshipdescription.md), and/or [`NSFetchedPropertyDescription`](nsfetchedpropertydescription.md).

##### Special Considerations

Setting the properties raises an exception if the receiver’s model has been used by an object graph manager.

## See Also

- [var propertiesByName: [String : NSPropertyDescription]](nsentitydescription/propertiesbyname.md)
  A dictionary containing the properties of the receiver.
- [var attributesByName: [String : NSAttributeDescription]](nsentitydescription/attributesbyname.md)
  The attributes of the receiver in a dictionary.
- [var relationshipsByName: [String : NSRelationshipDescription]](nsentitydescription/relationshipsbyname.md)
  The relationships of the receiver in a dictionary.
- [func relationships(forDestination: NSEntityDescription) -> [NSRelationshipDescription]](nsentitydescription/relationships(fordestination:).md)
  Returns an array containing the relationships of the receiver where the entity description of the relationship is a given entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsentitydescription/properties)*
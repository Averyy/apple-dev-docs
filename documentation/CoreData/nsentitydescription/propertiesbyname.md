# propertiesByName

**Framework**: Core Data  
**Kind**: property

A dictionary containing the properties of the receiver.

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
var propertiesByName: [String : NSPropertyDescription] { get }
```

#### Discussion

The keys in the dictionary are the property names and the values are instances of [`NSAttributeDescription`](nsattributedescription.md) and/or [`NSRelationshipDescription`](nsrelationshipdescription.md).

## See Also

- [var properties: [NSPropertyDescription]](nsentitydescription/properties.md)
  An array containing the properties of the receiver.
- [var attributesByName: [String : NSAttributeDescription]](nsentitydescription/attributesbyname.md)
  The attributes of the receiver in a dictionary.
- [var relationshipsByName: [String : NSRelationshipDescription]](nsentitydescription/relationshipsbyname.md)
  The relationships of the receiver in a dictionary.
- [func relationships(forDestination: NSEntityDescription) -> [NSRelationshipDescription]](nsentitydescription/relationships(fordestination:).md)
  Returns an array containing the relationships of the receiver where the entity description of the relationship is a given entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsentitydescription/propertiesbyname)*
# relationshipsByName

**Framework**: Core Data  
**Kind**: property

The relationships of the receiver in a dictionary.

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
var relationshipsByName: [String : NSRelationshipDescription] { get }
```

#### Discussion

The keys in the dictionary are the relationship names and the values are instances of [`NSRelationshipDescription`](nsrelationshipdescription.md).

## See Also

- [var propertiesByName: [String : NSPropertyDescription]](nsentitydescription/propertiesbyname.md)
  A dictionary containing the properties of the receiver.
- [var properties: [NSPropertyDescription]](nsentitydescription/properties.md)
  An array containing the properties of the receiver.
- [var attributesByName: [String : NSAttributeDescription]](nsentitydescription/attributesbyname.md)
  The attributes of the receiver in a dictionary.
- [func relationships(forDestination: NSEntityDescription) -> [NSRelationshipDescription]](nsentitydescription/relationships(fordestination:).md)
  Returns an array containing the relationships of the receiver where the entity description of the relationship is a given entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsentitydescription/relationshipsbyname)*
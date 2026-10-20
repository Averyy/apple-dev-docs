# relationshipsByName

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The relationships of the receiver in a dictionary.

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
var relationshipsByName: [String : NSRelationshipDescription] { get }
```

```objc
@property (copy, readonly) NSDictionary<NSString *,NSRelationshipDescription *> * relationshipsByName;
```

#### Discussion

The keys in the dictionary are the relationship names and the values are instances of [`NSRelationshipDescription`](../nsrelationshipdescription.md).

## See Also

### Working with properties
- [var propertiesByName: [String : NSPropertyDescription]](./propertiesbyname.md)
  A dictionary containing the properties of the receiver.
- [var properties: [NSPropertyDescription]](./properties.md)
  An array containing the properties of the receiver.
- [var attributesByName: [String : NSAttributeDescription]](./attributesbyname.md)
  The attributes of the receiver in a dictionary.
- [func relationships(forDestination: NSEntityDescription) -> [NSRelationshipDescription]](./relationships%28fordestination%29.md)
  Returns an array containing the relationships of the receiver where the entity description of the relationship is a given entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsentitydescription/relationshipsbyname)*
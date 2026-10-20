# relationships(forDestination:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

Returns an array containing the relationships of the receiver where the entity description of the relationship is a given entity.

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
func relationships(forDestination entity: NSEntityDescription) -> [NSRelationshipDescription]
```

```objc
- (NSArray<NSRelationshipDescription *> *) relationshipsWithDestinationEntity:(NSEntityDescription *) entity;
```

#### Return Value

An array containing the relationships of the receiver where the entity description of the relationship is `entity`. Elements in the array are instances of [`NSRelationshipDescription`](../nsrelationshipdescription.md).

## Parameters

- `entity`: An entity description.

## See Also

### Working with properties
- [var propertiesByName: [String : NSPropertyDescription]](./propertiesbyname.md)
  A dictionary containing the properties of the receiver.
- [var properties: [NSPropertyDescription]](./properties.md)
  An array containing the properties of the receiver.
- [var attributesByName: [String : NSAttributeDescription]](./attributesbyname.md)
  The attributes of the receiver in a dictionary.
- [var relationshipsByName: [String : NSRelationshipDescription]](./relationshipsbyname.md)
  The relationships of the receiver in a dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsentitydescription/relationships(fordestination:))*
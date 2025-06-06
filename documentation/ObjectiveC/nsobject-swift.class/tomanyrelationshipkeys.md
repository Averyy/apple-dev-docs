# toManyRelationshipKeys

**Framework**: Objective-C Runtime  
**Kind**: property

An array containing the keys for the to-many relationship properties of the receiver.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
var toManyRelationshipKeys: [String] { get }
```

## See Also

- [var attributeKeys: [String]](nsobject-swift.class/attributekeys.md)
  An array of `NSString` objects containing the names of immutable values that instances of the receiver’s class contain.
- [var classDescription: NSClassDescription](nsobject-swift.class/classdescription.md)
  An object containing information about the attributes and relationships of the receiver’s class.
- [func inverse(forRelationshipKey: String) -> String?](nsobject-swift.class/inverse(forrelationshipkey:).md)
  For a given key that defines the name of the relationship from the receiver’s class to another class, returns the name of the relationship from the other class to the receiver’s class.
- [var toOneRelationshipKeys: [String]](nsobject-swift.class/toonerelationshipkeys.md)
  The keys for the to-one relationship properties of the receiver, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/tomanyrelationshipkeys)*
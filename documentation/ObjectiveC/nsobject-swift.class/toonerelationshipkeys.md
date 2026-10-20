# toOneRelationshipKeys

**Framework**: Objective-C Runtime  
**Kind**: property  
**Role**: Instance Property

The keys for the to-one relationship properties of the receiver, if any.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
var toOneRelationshipKeys: [String] { get }
```

```objc
@property (copy, readonly) NSArray<NSString *> * toOneRelationshipKeys;
```

## See Also

### Working with Class Descriptions
- [var attributeKeys: [String]](./attributekeys.md)
  An array of `NSString` objects containing the names of immutable values that instances of the receiver’s class contain.
- [var classDescription: NSClassDescription](./classdescription.md)
  An object containing information about the attributes and relationships of the receiver’s class.
- [func inverse(forRelationshipKey: String) -> String?](./inverse%28forrelationshipkey%29.md)
  For a given key that defines the name of the relationship from the receiver’s class to another class, returns the name of the relationship from the other class to the receiver’s class.
- [var toManyRelationshipKeys: [String]](./tomanyrelationshipkeys.md)
  An array containing the keys for the to-many relationship properties of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/toonerelationshipkeys)*
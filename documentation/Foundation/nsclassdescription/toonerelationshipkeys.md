# toOneRelationshipKeys

**Framework**: Foundation  
**Kind**: property

Overridden by subclasses to return the keys for the to-one relationship properties of instances of the described class.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var toOneRelationshipKeys: [String] { get }
```

#### Return Value

An array of `NSString` objects containing the names of the to-one relationship properties of instances of the described class.

#### Discussion

To-one relationship properties are single objects.

If you have an instance of the class the receiver describes, you can use the `NSObject` instance method [`toOneRelationshipKeys`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/toOneRelationshipKeys) instead.

## See Also

- [var attributeKeys: [String]](nsclassdescription/attributekeys.md)
  Overridden by subclasses to return the names of attributes of instances of the described class.
- [func inverse(forRelationshipKey: String) -> String?](nsclassdescription/inverse(forrelationshipkey:).md)
  Overridden by subclasses to return the name of the inverse relationship from a relationship specified by a given key.
- [var toManyRelationshipKeys: [String]](nsclassdescription/tomanyrelationshipkeys.md)
  Overridden by subclasses to return the keys for the to-many relationship properties of instances of the described class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsclassdescription/toonerelationshipkeys)*
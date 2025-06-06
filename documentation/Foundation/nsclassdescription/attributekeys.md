# attributeKeys

**Framework**: Foundation  
**Kind**: property

Overridden by subclasses to return the names of attributes of instances of the described class.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var attributeKeys: [String] { get }
```

#### Return Value

An array of `NSString` objects containing the names of attributes of instances of the described class.

#### Discussion

For example, a class description that describes Movie objects could return the attribute keys `title`, `dateReleased`, and `rating`.

If you have an instance of the class the receiver describes, you can use the `NSObject` instance method [`attributeKeys`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/attributeKeys) instead.

## See Also

- [var toManyRelationshipKeys: [String]](nsclassdescription/tomanyrelationshipkeys.md)
  Overridden by subclasses to return the keys for the to-many relationship properties of instances of the described class.
- [var toOneRelationshipKeys: [String]](nsclassdescription/toonerelationshipkeys.md)
  Overridden by subclasses to return the keys for the to-one relationship properties of instances of the described class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsclassdescription/attributekeys)*
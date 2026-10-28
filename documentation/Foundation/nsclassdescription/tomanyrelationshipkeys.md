# toManyRelationshipKeys

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Overridden by subclasses to return the keys for the to-many relationship properties of instances of the described class.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var toManyRelationshipKeys: [String] { get }
```

```objc
@property (copy, readonly) NSArray<NSString *> * toManyRelationshipKeys;
```

## Return Value

An array of `NSString` objects containing the names of the to-many relationship properties of instances of the described class.

## Discussion

To-many relationship properties are arrays of objects.

If you have an instance of the class the receiver describes, you can use the `NSObject` instance method [`toManyRelationshipKeys`](../../ObjectiveC/nsobject-swift.class/tomanyrelationshipkeys.md) instead.

## See Also

### Related Documentation
- [var attributeKeys: [String]](./attributekeys.md)
  Overridden by subclasses to return the names of attributes of instances of the described class.
### Relationship keys
- [func inverse(forRelationshipKey: String) -> String?](./inverse%28forrelationshipkey%29.md)
  Overridden by subclasses to return the name of the inverse relationship from a relationship specified by a given key.
- [var toOneRelationshipKeys: [String]](./toonerelationshipkeys.md)
  Overridden by subclasses to return the keys for the to-one relationship properties of instances of the described class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsclassdescription/tomanyrelationshipkeys)*
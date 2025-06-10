# inverse(forRelationshipKey:)

**Framework**: Foundation  
**Kind**: method

Overridden by subclasses to return the name of the inverse relationship from a relationship specified by a given key.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func inverse(forRelationshipKey relationshipKey: String) -> String?
```

#### Return Value

The name of the inverse relationship from the relationship specified by `relationshipKey`.

#### Discussion

For a given key that defines the name of the relationship from the receiver’s class to another class, returns the name of the relationship from the other class to the receiver’s class. For example, suppose an Employee class has a relationship named `department` to a Department class, and that Department has a relationship named `employees` to Employee. The statement:

```objc
[employee inverseForRelationshipKey:@"department"];
```

returns the string `employees`.

If you have an instance of the class the receiver describes, you can use the `NSObject` instance method doc://com.apple.documentation/documentation/objectivec/nsobject/1411046-inverse instead.

## See Also

- [var toManyRelationshipKeys: [String]](nsclassdescription/tomanyrelationshipkeys.md)
  Overridden by subclasses to return the keys for the to-many relationship properties of instances of the described class.
- [var toOneRelationshipKeys: [String]](nsclassdescription/toonerelationshipkeys.md)
  Overridden by subclasses to return the keys for the to-one relationship properties of instances of the described class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsclassdescription/inverse(forrelationshipkey:))*
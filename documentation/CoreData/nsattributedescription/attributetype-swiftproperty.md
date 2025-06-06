# attributeType

**Framework**: Core Data  
**Kind**: property

The attribute’s type.

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
var attributeType: NSAttributeType { get set }
```

#### Discussion

Don’t change an attribute’s type after you add its containing managed object model to a persistent store coordinator; otherwise, Core Data throws an exception.

## See Also

- [var attributeValueClassName: String?](nsattributedescription/attributevalueclassname.md)
  The class name that represents the attribute’s value.
- [var type: NSAttributeDescription.AttributeType](nsattributedescription/type.md)
  The attribute’s type.
- [NSAttributeDescription.AttributeType](nsattributedescription/attributetype-swift.struct.md)
  The types of attributes that Core Data supports.
- [enum NSAttributeType](nsattributetype.md)
  The types of attribute that Core Data supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsattributedescription/attributetype-swift.property)*
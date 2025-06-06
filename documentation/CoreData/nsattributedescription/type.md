# type

**Framework**: Core Data  
**Kind**: property

The attribute’s type.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
var type: NSAttributeDescription.AttributeType { get set }
```

#### Discussion

Don’t change an attribute’s type after you add its containing managed object model to a persistent store coordinator; otherwise, Core Data throws an exception.

## See Also

- [var attributeValueClassName: String?](nsattributedescription/attributevalueclassname.md)
  The class name that represents the attribute’s value.
- [NSAttributeDescription.AttributeType](nsattributedescription/attributetype-swift.struct.md)
  The types of attributes that Core Data supports.
- [var attributeType: NSAttributeType](nsattributedescription/attributetype-swift.property.md)
  The attribute’s type.
- [enum NSAttributeType](nsattributetype.md)
  The types of attribute that Core Data supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsattributedescription/type)*
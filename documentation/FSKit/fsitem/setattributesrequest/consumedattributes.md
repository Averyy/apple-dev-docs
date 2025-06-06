# consumedAttributes

**Framework**: FSKit  
**Kind**: property

The attributes successfully used by the file system.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var consumedAttributes: FSItem.Attribute { get set }
```

#### Discussion

This property is a bit field in Objective-C and an [`OptionSet`](https://developer.apple.com/documentation/Swift/OptionSet) in Swift.

## See Also

- [func wasAttributeConsumed(FSItem.Attribute) -> Bool](fsitem/setattributesrequest/wasattributeconsumed(_:).md)
  A method that indicates whether the file system used the given attribute.
- [FSItem.Attribute](fsitem/attribute.md)
  A value that indicates a set of item attributes to get or set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsitem/setattributesrequest/consumedattributes)*
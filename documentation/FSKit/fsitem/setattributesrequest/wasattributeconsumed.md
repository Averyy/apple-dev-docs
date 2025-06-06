# wasAttributeConsumed(_:)

**Framework**: FSKit  
**Kind**: method

A method that indicates whether the file system used the given attribute.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func wasAttributeConsumed(_ attribute: FSItem.Attribute) -> Bool
```

## Parameters

- `attribute`: The   to check.

## See Also

- [var consumedAttributes: FSItem.Attribute](fsitem/setattributesrequest/consumedattributes.md)
  The attributes successfully used by the file system.
- [FSItem.Attribute](fsitem/attribute.md)
  A value that indicates a set of item attributes to get or set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsitem/setattributesrequest/wasattributeconsumed(_:))*
# isValid(_:)

**Framework**: FSKit  
**Kind**: method

Returns a Boolean value that indicates whether the attribute is valid.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func isValid(_ attribute: FSItem.Attribute) -> Bool
```

#### Discussion

If the value returned by this method is `YES` (Objective-C) or `true` (Swift), a caller can safely use the given attribute.

## See Also

- [func invalidateAllProperties()](fsitem/attributes/invalidateallproperties.md)
  Marks all attributes inactive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsitem/attributes/isvalid(_:))*
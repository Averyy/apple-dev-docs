# isValid(_:)

**Framework**: FSKit  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether the attribute is valid.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func isValid(_ attribute: FSItem.Attribute) -> Bool
```

```objc
- (BOOL) isValid:(FSItemAttribute) attribute;
```

## Discussion

If the value returned by this method is `YES` (Objective-C) or `true` (Swift), a caller can safely use the given attribute.

## See Also

### Validating and invalidating attributes
- [func invalidateAllProperties()](./invalidateallproperties%28%29.md)
  Marks all attributes inactive.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsitem/attributes/isvalid(_:))*
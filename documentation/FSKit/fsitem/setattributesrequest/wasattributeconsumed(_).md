# wasAttributeConsumed(_:)

**Framework**: FSKit  
**Kind**: method  
**Role**: Instance Method

A method that indicates whether the file system used the given attribute.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func wasAttributeConsumed(_ attribute: FSItem.Attribute) -> Bool
```

```objc
- (BOOL) wasAttributeConsumed:(FSItemAttribute) attribute;
```

## Parameters

- `attribute`: The [`FSItem.Attribute`](../attribute.md) to check.

## See Also

### Inspecting used attributes
- [var consumedAttributes: FSItem.Attribute](./consumedattributes.md)
  The attributes successfully used by the file system.
- [FSItem.Attribute](../attribute.md)
  A value that indicates a set of item attributes to get or set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsitem/setattributesrequest/wasattributeconsumed(_:))*
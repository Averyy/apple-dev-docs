# init(attributes:)

**Framework**: FSKit  
**Kind**: init

Creates a result for an attribute-getting operation.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
init?(attributes: FSItem.Attributes)
```

#### Return Value

A populated result instance, or `nil` if validation fails.

## Parameters

- `attributes`: The requested [`FSItem.Attributes`](fsitem/attributes.md) for the item.

## See Also

- [FSItem.Attributes](fsitem/attributes.md)
  Attributes of an item, such as size, creation and modification times, and user and group identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsgetattributesresult/init(attributes:))*
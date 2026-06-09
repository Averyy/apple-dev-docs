# init(itemAttributes:)

**Framework**: FSKit  
**Kind**: init

Creates a result for an I/O-completion operation.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
init?(itemAttributes attributes: FSItem.Attributes)
```

#### Return Value

A populated result instance, or `nil` if validation fails.

## Parameters

- `attributes`: The updated [`FSItem.Attributes`](fsitem/attributes.md) of the file after the I/O completion operation (e.g., updated size, modification time).

## See Also

- [FSItem.Attributes](fsitem/attributes.md)
  Attributes of an item, such as size, creation and modification times, and user and group identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fscompleteioresult/init(itemattributes:))*
# init(bytesRead:itemAttributes:)

**Framework**: FSKit  
**Kind**: init

Creates a result for a file-reading operation.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
init?(bytesRead actuallyRead: Int, itemAttributes attributes: FSItem.Attributes)
```

#### Return Value

A populated result instance, or `nil` if validation fails.

## Parameters

- `actuallyRead`: The number of bytes actually read from the file. This may be less than the requested length if the end of file was reached.
- `attributes`: The updated [`FSItem.Attributes`](fsitem/attributes.md) of the file after the read operation (e.g., updated access time).

## See Also

- [FSItem.Attributes](fsitem/attributes.md)
  Attributes of an item, such as size, creation and modification times, and user and group identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsreadfileresult/init(bytesread:itemattributes:))*
# init(contents:symlinkAttributes:)

**Framework**: FSKit  
**Kind**: init

Creates a result for a symlink-reading operation.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
init?(contents: FSFileName, symlinkAttributes attributes: FSItem.Attributes)
```

#### Return Value

A populated result instance, or `nil` if validation fails.

## Parameters

- `contents`: The contents of the symbolic link.
- `attributes`: The [`FSItem.Attributes`](fsitem/attributes.md) of the symbolic link.

## See Also

- [class FSFileName](fsfilename.md)
  The name of a file, expressed as a data buffer.
- [FSItem.Attributes](fsitem/attributes.md)
  Attributes of an item, such as size, creation and modification times, and user and group identifiers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsreadsymlinkresult/init(contents:symlinkattributes:))*
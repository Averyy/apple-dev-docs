# init(rootItem:)

**Framework**: FSKit  
**Kind**: init

Creates a result instance with all required properties populated.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
init?(rootItem: FSItem)
```

#### Return Value

A populated result instance, or `nil` if validation fails.

## Parameters

- `rootItem`: The root [`FSItem`](fsitem.md) of the volume.

## See Also

- [class FSItem](fsitem.md)
  A distinct object in a file hierarchy, such as a file, directory, symlink, socket, and more.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsactivateresult/init(rootitem:))*
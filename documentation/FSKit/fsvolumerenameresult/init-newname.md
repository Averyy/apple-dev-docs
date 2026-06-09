# init(newName:)

**Framework**: FSKit  
**Kind**: init

Creates a result for a volume-renaming operation.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
init?(newName: FSFileName)
```

#### Return Value

A populated result instance, or `nil` if validation fails.

## Parameters

- `newName`: The new volume name.

## See Also

- [class FSFileName](fsfilename.md)
  The name of a file, expressed as a data buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolumerenameresult/init(newname:))*
# init(xattrNames:)

**Framework**: FSKit  
**Kind**: init

Creates a result instance with all required properties populated.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
init?(xattrNames: [FSFileName])
```

#### Return Value

A populated result instance, or `nil` if validation fails.

## Parameters

- `xattrNames`: An array of [`FSFileName`](fsfilename.md) instances representing the names of all extended attributes currently set on the item.

## See Also

- [class FSFileName](fsfilename.md)
  The name of a file, expressed as a data buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fslistxattrsresult/init(xattrnames:))*
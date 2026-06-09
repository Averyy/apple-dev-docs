# init(xattrValue:)

**Framework**: FSKit  
**Kind**: init

Creates a result for an extended-attribute-getting operation.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
init?(xattrValue value: Data)
```

#### Return Value

A populated result instance, or `nil` if validation fails.

## Parameters

- `value`: The extended attribute value for the requested attribute name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsgetxattrresult/init(xattrvalue:))*
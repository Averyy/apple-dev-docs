# init(type:creator:)

**Framework**: File Provider  
**Kind**: init

Creates a structure that contains the provided type and creator codes.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
init(type: OSType, creator: OSType)
```

## Parameters

- `type`: The first word of the   structure. It matches the file type code.
- `creator`: The second word of the   structure. It matches the creator code.

## See Also

- [init()](nsfileprovidertypeandcreator/init.md)
  Returns a new type and creator structure with both codes set to `0`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidertypeandcreator/init(type:creator:))*
# offset(for:)

**Framework**: Metal  
**Kind**: method

Returns the byte offset into the buffer for the given plane.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func offset(for plane: MTLTensorPlaneType) -> Int
```

#### Return Value

The byte offset for the given plane.

## Parameters

- `plane`: The plane type to look up.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltensorbufferattachments/offset(for:))*
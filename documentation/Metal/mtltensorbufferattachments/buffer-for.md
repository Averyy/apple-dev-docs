# buffer(for:)

**Framework**: Metal  
**Kind**: method

Returns the buffer backing the given plane, or `nil` if none has been set.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func buffer(for plane: MTLTensorPlaneType) -> (any MTLBuffer)?
```

#### Return Value

The buffer for the given plane, or `nil`.

## Parameters

- `plane`: The plane type to look up.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltensorbufferattachments/buffer(for:))*
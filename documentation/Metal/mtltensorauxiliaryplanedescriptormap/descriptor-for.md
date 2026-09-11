# descriptor(for:)

**Framework**: Metal  
**Kind**: method

Returns the auxiliary plane descriptor for the given plane type, or `nil` if none has been set.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func descriptor(for plane: MTLTensorPlaneType) -> MTLTensorAuxiliaryPlaneDescriptor?
```

#### Return Value

The descriptor for the given plane type, or `nil`.

## Parameters

- `plane`: The plane type to look up.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltensorauxiliaryplanedescriptormap/descriptor(for:))*
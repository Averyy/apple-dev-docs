# descriptor(for:)

**Framework**: Metal  
**Kind**: method

Returns the auxiliary plane descriptor for the given plane type, or `nil` if none has been set.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

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
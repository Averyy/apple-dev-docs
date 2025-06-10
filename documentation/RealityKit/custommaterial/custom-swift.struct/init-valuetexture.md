# init(value:texture:)

**Framework**: RealityKit  
**Kind**: init

Creates a custom object from a vector and texture.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)

## Declaration

```swift
init(value: SIMD4<Float> = .init(repeating: 0), texture: CustomMaterial.Texture? = nil)
```

#### Discussion

Use this initializer to create a new [`CustomMaterial.Custom`](custommaterial/custom-swift.struct.md) object from a four-component vector, a texture, or both. RealityKit passes these values automatically to your custom material’s shader functions. Custom values have no predefined meaning, and RealityKit doesn’t use them other than to make them available in your surface shader and geometry modifier.

## Parameters

- `value`: A four-component vector.
- `texture`: An optional texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/custommaterial/custom-swift.struct/init(value:texture:))*
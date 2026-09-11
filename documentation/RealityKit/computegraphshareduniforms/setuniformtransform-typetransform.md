# setUniformTransform(type:transform:)

**Framework**: RealityKit  
**Kind**: method

Registers a raw-data transformer closure for a uniform of type `V`.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func setUniformTransform<V>(type: V.Type, transform: @escaping @_lifetime(0: copy 0) (inout MutableRawSpan, Entity) -> Void) where V : BitwiseCopyable
```

#### Discussion

Use this overload when the transformation is most naturally expressed over the raw byte representation of the value.

## Parameters

- `type`: The `BitwiseCopyable` type the transformer operates on.
- `transform`: A closure `(inout MutableRawSpan, Entity) -> Void`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/computegraphshareduniforms/setuniformtransform(type:transform:))*
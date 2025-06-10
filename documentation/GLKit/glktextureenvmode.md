# GLKTextureEnvMode

**Framework**: GLKit  
**Kind**: enum

The mode used to combine the texture with other color components.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
enum GLKTextureEnvMode
```

## Topics

### Constants
- [GLKTextureEnvMode.replace](glktextureenvmode/replace.md)
  The output color is set to the color fetched from the texture. The input color is ignored.
- [GLKTextureEnvMode.modulate](glktextureenvmode/modulate.md)
  The output color is calculated by multiplying the texture’s color by the input color.
- [GLKTextureEnvMode.decal](glktextureenvmode/decal.md)
  The output color is calculated by using the texture’s alpha component to blend the texture’s color with the input color.
### Initializers
- [init?(rawValue: GLint)](glktextureenvmode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum GLKTextureTarget](glktexturetarget.md)
  The kind of texture pointed to by the property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glktextureenvmode)*
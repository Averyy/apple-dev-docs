# constantBlockAlignment

**Framework**: Metal  
**Kind**: property

The alignment of the constant block.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var constantBlockAlignment: Int { get set }
```

#### Discussion

If set, this property forces the constant block to be aligned to the specified value. It should be set on the first constant only, and is valid only if a corresponding explicit `alignas` specifier is applied to the constant in the Metal shader language.

## See Also

- [var dataType: MTLDataType](mtlargumentdescriptor/datatype.md)
  The data type of the argument.
- [var index: Int](mtlargumentdescriptor/index.md)
  The index ID of the argument.
- [var access: MTLBindingAccess](mtlargumentdescriptor/access.md)
  The access permissions of the argument.
- [var arrayLength: Int](mtlargumentdescriptor/arraylength.md)
  The length of an array argument.
- [var textureType: MTLTextureType](mtlargumentdescriptor/texturetype.md)
  The texture type of a texture argument.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlargumentdescriptor/constantblockalignment)*
# arrayLength

**Framework**: Metal  
**Kind**: property

The length of an array argument.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var arrayLength: Int { get set }
```

#### Discussion

For a nonarray argument, this value must be `0`.

## See Also

- [var dataType: MTLDataType](mtlargumentdescriptor/datatype.md)
  The data type of the argument.
- [var index: Int](mtlargumentdescriptor/index.md)
  The index ID of the argument.
- [var access: MTLBindingAccess](mtlargumentdescriptor/access.md)
  The access permissions of the argument.
- [var constantBlockAlignment: Int](mtlargumentdescriptor/constantblockalignment.md)
  The alignment of the constant block.
- [var textureType: MTLTextureType](mtlargumentdescriptor/texturetype.md)
  The texture type of a texture argument.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlargumentdescriptor/arraylength)*
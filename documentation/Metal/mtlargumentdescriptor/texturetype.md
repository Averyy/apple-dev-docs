# textureType

**Framework**: Metal  
**Kind**: property

The texture type of a texture argument.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var textureType: MTLTextureType { get set }
```

#### Discussion

For a nontexture argument, this value is ignored.

## See Also

- [var dataType: MTLDataType](mtlargumentdescriptor/datatype.md)
  The data type of the argument.
- [var index: Int](mtlargumentdescriptor/index.md)
  The index ID of the argument.
- [var access: MTLBindingAccess](mtlargumentdescriptor/access.md)
  The access permissions of the argument.
- [var arrayLength: Int](mtlargumentdescriptor/arraylength.md)
  The length of an array argument.
- [var constantBlockAlignment: Int](mtlargumentdescriptor/constantblockalignment.md)
  The alignment of the constant block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlargumentdescriptor/texturetype)*
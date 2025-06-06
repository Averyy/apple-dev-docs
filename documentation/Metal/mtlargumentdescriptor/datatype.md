# dataType

**Framework**: Metal  
**Kind**: property

The data type of the argument.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var dataType: MTLDataType { get set }
```

#### Discussion

For a constant data argument, this value must match the binary format of the data stored in the buffer for that argument. For other parameter types, such as textures or samplers, specify the appropriate constant. See [`MTLDataType`](mtldatatype.md) for possible values.

## See Also

- [var index: Int](mtlargumentdescriptor/index.md)
  The index ID of the argument.
- [var access: MTLBindingAccess](mtlargumentdescriptor/access.md)
  The access permissions of the argument.
- [var arrayLength: Int](mtlargumentdescriptor/arraylength.md)
  The length of an array argument.
- [var constantBlockAlignment: Int](mtlargumentdescriptor/constantblockalignment.md)
  The alignment of the constant block.
- [var textureType: MTLTextureType](mtlargumentdescriptor/texturetype.md)
  The texture type of a texture argument.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlargumentdescriptor/datatype)*
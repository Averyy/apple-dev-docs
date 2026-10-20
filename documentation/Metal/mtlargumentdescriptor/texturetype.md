# textureType

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic) MTLTextureType textureType;
```

#### Discussion

For a nontexture argument, this value is ignored.

## See Also

### Setting the descriptor’s properties
- [var dataType: MTLDataType](./datatype.md)
  The data type of the argument.
- [var index: Int](./index.md)
  The index ID of the argument.
- [var access: MTLBindingAccess](./access.md)
  The access permissions of the argument.
- [var arrayLength: Int](./arraylength.md)
  The length of an array argument.
- [var constantBlockAlignment: Int](./constantblockalignment.md)
  The alignment of the constant block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlargumentdescriptor/texturetype)*
# dataType

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic) MTLDataType dataType;
```

## Discussion

For a constant data argument, this value needs to match the binary format of the data stored in the buffer for that argument. For other parameter types, such as textures or samplers, specify the appropriate constant. See [`MTLDataType`](../mtldatatype.md) for possible values.

## See Also

### Setting the descriptor’s properties
- [var index: Int](./index.md)
  The index ID of the argument.
- [var access: MTLBindingAccess](./access.md)
  The access permissions of the argument.
- [var arrayLength: Int](./arraylength.md)
  The length of an array argument.
- [var constantBlockAlignment: Int](./constantblockalignment.md)
  The alignment of the constant block.
- [var textureType: MTLTextureType](./texturetype.md)
  The texture type of a texture argument.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlargumentdescriptor/datatype)*
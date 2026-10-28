# arrayLength

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic) NSUInteger arrayLength;
```

## Discussion

For a nonarray argument, this value needs to be `0`.

## See Also

### Setting the descriptor’s properties
- [var dataType: MTLDataType](./datatype.md)
  The data type of the argument.
- [var index: Int](./index.md)
  The index ID of the argument.
- [var access: MTLBindingAccess](./access.md)
  The access permissions of the argument.
- [var constantBlockAlignment: Int](./constantblockalignment.md)
  The alignment of the constant block.
- [var textureType: MTLTextureType](./texturetype.md)
  The texture type of a texture argument.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlargumentdescriptor/arraylength)*
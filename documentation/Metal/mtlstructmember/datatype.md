# dataType

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The data type of the struct member.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var dataType: MTLDataType { get }
```

```objc
@property (readonly) MTLDataType dataType;
```

## Discussion

For information on possible values, see [`MTLDataType`](../mtldatatype.md). If the value is [`MTLDataType.array`](../mtldatatype/array.md), then the [`arrayType()`](./arraytype%28%29.md) method returns an object that describes the underlying array. If the value is [`MTLDataType.struct`](../mtldatatype/struct.md), then the [`structType()`](./structtype%28%29.md) method returns an object that describes the underlying struct.

## See Also

### Describing the struct member
- [var name: String](./name.md)
  The name of the struct member.
- [var offset: Int](./offset.md)
  The location of this member relative to the start of its struct, in bytes.
- [var argumentIndex: Int](./argumentindex.md)
  The index in the argument table that corresponds to the struct member.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlstructmember/datatype)*
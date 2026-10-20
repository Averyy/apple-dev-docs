# dataSize

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The size, in bytes, of the element data.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var dataSize: Int { get }
```

```objc
@property (readonly) NSUInteger dataSize;
```

## See Also

### Describing the pointer elements
- [var alignment: Int](./alignment.md)
  The required byte alignment in memory for the element data.
- [var elementType: MTLDataType](./elementtype.md)
  The data type of the element data.
- [var access: MTLBindingAccess](./access.md)
  The function’s read/write access to the element data.
- [var elementIsArgumentBuffer: Bool](./elementisargumentbuffer.md)
  A Boolean value that indicates whether the element is an argument buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlpointertype/datasize)*
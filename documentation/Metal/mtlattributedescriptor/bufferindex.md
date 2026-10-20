# bufferIndex

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The index in the buffer argument table for the buffer that contains the data for this attribute.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var bufferIndex: Int { get set }
```

```objc
@property (nonatomic, assign) NSUInteger bufferIndex;
```

## See Also

### Defining attribute location
- [var offset: Int](./offset.md)
  The offset, in bytes, from the start of the buffer that contains the attribute data to the start of the data itself.
- [var format: MTLAttributeFormat](./format.md)
  The format of the attribute’s data.
- [enum MTLAttributeFormat](../mtlattributeformat.md)
  The data format options for acceleration structures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlattributedescriptor/bufferindex)*
# format

**Framework**: Model I/O  
**Kind**: property  
**Role**: Instance Property

The format of per-vertex data for the attribute.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var format: MDLVertexFormat { get set }
```

```objc
@property (nonatomic) MDLVertexFormat format;
```

#### Discussion

A [`MDLVertexFormat`](../mdlvertexformat.md) value describes the number of vector components for an attribute, as well as the data type of each component, and, for special packed formats, the layout of components.

## See Also

### Accessing Data for a Vertex Attribute
- [var dataStart: UnsafeMutableRawPointer](./datastart.md)
  The offset, in bytes, from the start of the data to where vertex attribute information begins.
- [var stride: Int](./stride.md)
  The stride, in bytes, between vertex information for consecutive vertices in the data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlvertexattributedata/format)*
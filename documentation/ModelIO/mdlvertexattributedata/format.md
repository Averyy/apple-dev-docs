# format

**Framework**: Model I/O  
**Kind**: property

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

#### Discussion

A [`MDLVertexFormat`](mdlvertexformat.md) value describes the number of vector components for an attribute, as well as the data type of each component, and, for special packed formats, the layout of components.

## See Also

- [var dataStart: UnsafeMutableRawPointer](mdlvertexattributedata/datastart.md)
  The offset, in bytes, from the start of the data to where vertex attribute information begins.
- [var stride: Int](mdlvertexattributedata/stride.md)
  The stride, in bytes, between vertex information for consecutive vertices in the data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlvertexattributedata/format)*
# dataStart

**Framework**: Model I/O  
**Kind**: property

The offset, in bytes, from the start of the data to where vertex attribute information begins.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var dataStart: UnsafeMutableRawPointer { get set }
```

## See Also

- [var stride: Int](mdlvertexattributedata/stride.md)
  The stride, in bytes, between vertex information for consecutive vertices in the data.
- [var format: MDLVertexFormat](mdlvertexattributedata/format.md)
  The format of per-vertex data for the attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlvertexattributedata/datastart)*
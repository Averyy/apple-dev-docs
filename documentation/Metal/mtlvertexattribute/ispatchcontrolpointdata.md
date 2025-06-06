# isPatchControlPointData

**Framework**: Metal  
**Kind**: property

A Boolean value that indicates whether this vertex attribute represents control point data.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var isPatchControlPointData: Bool { get }
```

#### Discussion

This value is always [`false`](https://developer.apple.com/documentation/swift/false) if the vertex function is not a post-tessellation vertex function.

## See Also

- [var name: String](mtlvertexattribute/name.md)
  The name of the attribute.
- [var attributeIndex: Int](mtlvertexattribute/attributeindex.md)
  The index of the attribute, as declared in Metal shader source code.
- [var attributeType: MTLDataType](mtlvertexattribute/attributetype.md)
  The data type for the attribute, as declared in Metal shader source code.
- [var isActive: Bool](mtlvertexattribute/isactive.md)
  A Boolean value that indicates whether this vertex attribute is active.
- [var isPatchData: Bool](mtlvertexattribute/ispatchdata.md)
  A Boolean value that indicates whether this vertex attribute represents patch data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlvertexattribute/ispatchcontrolpointdata)*
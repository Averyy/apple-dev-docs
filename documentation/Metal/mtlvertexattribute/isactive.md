# isActive

**Framework**: Metal  
**Kind**: property

A Boolean value that indicates whether this vertex attribute is active.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var isActive: Bool { get }
```

#### Discussion

If [`false`](https://developer.apple.com/documentation/Swift/false), this attribute is inactive and can be ignored.

## See Also

- [var name: String](mtlvertexattribute/name.md)
  The name of the attribute.
- [var attributeIndex: Int](mtlvertexattribute/attributeindex.md)
  The index of the attribute, as declared in Metal shader source code.
- [var attributeType: MTLDataType](mtlvertexattribute/attributetype.md)
  The data type for the attribute, as declared in Metal shader source code.
- [var isPatchControlPointData: Bool](mtlvertexattribute/ispatchcontrolpointdata.md)
  A Boolean value that indicates whether this vertex attribute represents control point data.
- [var isPatchData: Bool](mtlvertexattribute/ispatchdata.md)
  A Boolean value that indicates whether this vertex attribute represents patch data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlvertexattribute/isactive)*
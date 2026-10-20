# isPatchData

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether this vertex attribute represents patch data.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var isPatchData: Bool { get }
```

```objc
@property (readonly, getter=isPatchData) BOOL patchData;
```

#### Discussion

This value is always [`false`](../../Swift/false.md) if the vertex function is not a post-tessellation vertex function.

## See Also

### Describing the attribute
- [var name: String](./name.md)
  The name of the attribute.
- [var attributeIndex: Int](./attributeindex.md)
  The index of the attribute, as declared in Metal shader source code.
- [var attributeType: MTLDataType](./attributetype.md)
  The data type for the attribute, as declared in Metal shader source code.
- [var isActive: Bool](./isactive.md)
  A Boolean value that indicates whether this vertex attribute is active.
- [var isPatchControlPointData: Bool](./ispatchcontrolpointdata.md)
  A Boolean value that indicates whether this vertex attribute represents control point data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlvertexattribute/ispatchdata)*
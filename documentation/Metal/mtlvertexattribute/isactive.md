# isActive

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether this vertex attribute is active.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var isActive: Bool { get }
```

```objc
@property (readonly, getter=isActive) BOOL active;
```

## Discussion

If [`false`](../../Swift/false.md), this attribute is inactive and can be ignored.

## See Also

### Describing the attribute
- [var name: String](./name.md)
  The name of the attribute.
- [var attributeIndex: Int](./attributeindex.md)
  The index of the attribute, as declared in Metal shader source code.
- [var attributeType: MTLDataType](./attributetype.md)
  The data type for the attribute, as declared in Metal shader source code.
- [var isPatchControlPointData: Bool](./ispatchcontrolpointdata.md)
  A Boolean value that indicates whether this vertex attribute represents control point data.
- [var isPatchData: Bool](./ispatchdata.md)
  A Boolean value that indicates whether this vertex attribute represents patch data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlvertexattribute/isactive)*
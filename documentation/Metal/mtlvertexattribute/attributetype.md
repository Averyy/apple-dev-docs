# attributeType

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The data type for the attribute, as declared in Metal shader source code.

**Availability**:
- iOS 8.3+
- iPadOS 8.3+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var attributeType: MTLDataType { get }
```

```objc
@property (readonly) MTLDataType attributeType;
```

## See Also

### Describing the attribute
- [var name: String](./name.md)
  The name of the attribute.
- [var attributeIndex: Int](./attributeindex.md)
  The index of the attribute, as declared in Metal shader source code.
- [var isActive: Bool](./isactive.md)
  A Boolean value that indicates whether this vertex attribute is active.
- [var isPatchControlPointData: Bool](./ispatchcontrolpointdata.md)
  A Boolean value that indicates whether this vertex attribute represents control point data.
- [var isPatchData: Bool](./ispatchdata.md)
  A Boolean value that indicates whether this vertex attribute represents patch data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlvertexattribute/attributetype)*
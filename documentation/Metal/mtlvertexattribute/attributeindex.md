# attributeIndex

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The index of the attribute, as declared in Metal shader source code.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var attributeIndex: Int { get }
```

```objc
@property (readonly) NSUInteger attributeIndex;
```

## See Also

### Describing the attribute
- [var name: String](./name.md)
  The name of the attribute.
- [var attributeType: MTLDataType](./attributetype.md)
  The data type for the attribute, as declared in Metal shader source code.
- [var isActive: Bool](./isactive.md)
  A Boolean value that indicates whether this vertex attribute is active.
- [var isPatchControlPointData: Bool](./ispatchcontrolpointdata.md)
  A Boolean value that indicates whether this vertex attribute represents control point data.
- [var isPatchData: Bool](./ispatchdata.md)
  A Boolean value that indicates whether this vertex attribute represents patch data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlvertexattribute/attributeindex)*
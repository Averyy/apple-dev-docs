# name

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The name of the attribute.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var name: String { get }
```

```objc
@property (readonly) NSString * name;
```

## See Also

### Related Documentation
- [Metal Shading Language Guide](https://developer.apple.com/library/archive/documentation/Metal/Reference/MetalShadingLanguageGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014364)
- [Metal Programming Guide](https://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014221)
### Describing the attribute
- [var attributeIndex: Int](./attributeindex.md)
  The index of the attribute, as declared in Metal shader source code.
- [var attributeType: MTLDataType](./attributetype.md)
  The data type for the attribute, as declared in Metal shader source code.
- [var isActive: Bool](./isactive.md)
  A Boolean value that indicates whether this vertex attribute is active.
- [var isPatchControlPointData: Bool](./ispatchcontrolpointdata.md)
  A Boolean value that indicates whether this vertex attribute represents control point data.
- [var isPatchData: Bool](./ispatchdata.md)
  A Boolean value that indicates whether this vertex attribute represents patch data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlvertexattribute/name)*
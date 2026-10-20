# name

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The name of the attribute.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var name: String { get }
```

```objc
@property (readonly) NSString * name;
```

## See Also

### Reading an attribute’s properties
- [var attributeIndex: Int](./attributeindex.md)
  The index of the attribute, as declared in Metal shader source code.
- [var attributeType: MTLDataType](./attributetype.md)
  The data type for the attribute, as declared in Metal shader source code.
- [var isActive: Bool](./isactive.md)
  A Boolean value that indicates whether the attribute is active.
- [var isPatchControlPointData: Bool](./ispatchcontrolpointdata.md)
  A Boolean value that indicates whether the attribute represents control point data.
- [var isPatchData: Bool](./ispatchdata.md)
  A Boolean value that indicates whether the attribute represents tessellation patch data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlattribute/name)*
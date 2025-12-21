# MTLVertexAttribute

**Framework**: Metal  
**Kind**: class

An instance that represents an attribute of a vertex function.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
class MTLVertexAttribute
```

#### Overview

An [`MTLVertexAttribute`](mtlvertexattribute.md) instance represents an attribute for per-vertex input in a vertex function. You use vertex attribute instances to inspect the inputs of a vertex function by examining the [`vertexAttributes`](mtlfunction/vertexattributes.md) property of the corresponding [`MTLFunction`](mtlfunction.md) instance.

## Topics

### Describing the attribute
- [var name: String](mtlvertexattribute/name.md)
  The name of the attribute.
- [var attributeIndex: Int](mtlvertexattribute/attributeindex.md)
  The index of the attribute, as declared in Metal shader source code.
- [var attributeType: MTLDataType](mtlvertexattribute/attributetype.md)
  The data type for the attribute, as declared in Metal shader source code.
- [var isActive: Bool](mtlvertexattribute/isactive.md)
  A Boolean value that indicates whether this vertex attribute is active.
- [var isPatchControlPointData: Bool](mtlvertexattribute/ispatchcontrolpointdata.md)
  A Boolean value that indicates whether this vertex attribute represents control point data.
- [var isPatchData: Bool](mtlvertexattribute/ispatchdata.md)
  A Boolean value that indicates whether this vertex attribute represents patch data.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MTLAttribute](mtlattribute.md)
  An object that describes an attribute defined in the stage-in argument for a shader.
- [class MTLArgument](mtlargument.md)
  Information about an argument of a graphics or compute function.
- [typealias MTLAutoreleasedArgument](mtlautoreleasedargument.md)
  A convenience type alias for an autoreleased argument instance.
- [enum MTLArgumentType](mtlargumenttype.md)
  The resource type for an argument of a function.
- [typealias MTLArgumentAccess](mtlargumentaccess.md)
  Function access restrictions to argument data in the shading language code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlvertexattribute)*
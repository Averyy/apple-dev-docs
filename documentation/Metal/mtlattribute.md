# MTLAttribute

**Framework**: Metal  
**Kind**: class  
**Role**: Class

An object that describes an attribute defined in the stage-in argument for a shader.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class MTLAttribute
```

```objc
@interface MTLAttribute : NSObject
```

## Topics

### Reading an attribute’s properties
- [var name: String](./mtlattribute/name.md)
  The name of the attribute.
- [var attributeIndex: Int](./mtlattribute/attributeindex.md)
  The index of the attribute, as declared in Metal shader source code.
- [var attributeType: MTLDataType](./mtlattribute/attributetype.md)
  The data type for the attribute, as declared in Metal shader source code.
- [var isActive: Bool](./mtlattribute/isactive.md)
  A Boolean value that indicates whether the attribute is active.
- [var isPatchControlPointData: Bool](./mtlattribute/ispatchcontrolpointdata.md)
  A Boolean value that indicates whether the attribute represents control point data.
- [var isPatchData: Bool](./mtlattribute/ispatchdata.md)
  A Boolean value that indicates whether the attribute represents tessellation patch data.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Function arguments
- [class MTLVertexAttribute](./mtlvertexattribute.md)
  An instance that represents an attribute of a vertex function.
- [class MTLArgument](./mtlargument.md)
  Information about an argument of a graphics or compute function.
- [typealias MTLAutoreleasedArgument](./mtlautoreleasedargument.md)
  A convenience type alias for an autoreleased argument instance.
- [enum MTLArgumentType](./mtlargumenttype.md)
  The resource type for an argument of a function.
- [typealias MTLArgumentAccess](./mtlargumentaccess.md)
  Function access restrictions to argument data in the shading language code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlattribute)*
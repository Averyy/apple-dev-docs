# MTLVisibleFunctionTableDescriptor

**Framework**: Metal  
**Kind**: class  
**Role**: Class

A specification of how to create a visible function table.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
class MTLVisibleFunctionTableDescriptor
```

```objc
@interface MTLVisibleFunctionTableDescriptor : NSObject
```

## Topics

### Configuring the function table
- [var functionCount: Int](./mtlvisiblefunctiontabledescriptor/functioncount.md)
  The number of entries in the function table.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Shader functions
- [class MTLFunctionDescriptor](./mtlfunctiondescriptor.md)
  A description of a function object to create.
- [protocol MTLFunction](./mtlfunction.md)
  A interface that represents a public shader function in a Metal library.
- [protocol MTLFunctionHandle](./mtlfunctionhandle.md)
  An object representing a function that you can add to a visible function table.
- [protocol MTLVisibleFunctionTable](./mtlvisiblefunctiontable.md)
  A table of shader functions visible to your app that you can pass into compute commands to customize the behavior of a shader.
- [class MTLIntersectionFunctionDescriptor](./mtlintersectionfunctiondescriptor.md)
  A description of an intersection function that performs an intersection test.
- [class MTLIntersectionFunctionTableDescriptor](./mtlintersectionfunctiontabledescriptor.md)
  A specification of how to create an intersection function table.
- [protocol MTLIntersectionFunctionTable](./mtlintersectionfunctiontable.md)
  A table of intersection functions that Metal calls to perform ray-tracing intersection tests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlvisiblefunctiontabledescriptor)*
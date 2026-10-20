# MTLIntersectionFunctionTableDescriptor

**Framework**: Metal  
**Kind**: class  
**Role**: Class

A specification of how to create an intersection function table.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
class MTLIntersectionFunctionTableDescriptor
```

```objc
@interface MTLIntersectionFunctionTableDescriptor : NSObject
```

## Topics

### Configuring the table’s size
- [var functionCount: Int](./mtlintersectionfunctiontabledescriptor/functioncount.md)
  The number of entries in the intersection function table.

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

### Intersection function tables
- [protocol MTLIntersectionFunctionTable](./mtlintersectionfunctiontable.md)
  A table of intersection functions that Metal calls to perform ray-tracing intersection tests.
- [class MTLIntersectionFunctionDescriptor](./mtlintersectionfunctiondescriptor.md)
  A description of an intersection function that performs an intersection test.
- [struct MTLIntersectionFunctionSignature](./mtlintersectionfunctionsignature.md)
  Constants for specifying different types of custom intersection functions.
- [struct MTLIntersectionFunctionBufferArguments](./mtlintersectionfunctionbufferarguments.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlintersectionfunctiontabledescriptor)*
# MTLVisibleFunctionTable

**Framework**: Metal  
**Kind**: protocol

A table of shader functions visible to your app that you can pass into compute commands to customize the behavior of a shader.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
protocol MTLVisibleFunctionTable : MTLResource
```

## Topics

### Setting a Table Entry
- [func setFunction((any MTLFunctionHandle)?, index: Int)](mtlvisiblefunctiontable/setfunction(_:index:).md)
  Sets a table entry to point to a callable function.
- [func setFunctions([(any MTLFunctionHandle)?], range: Range<Int>)](mtlvisiblefunctiontable/setfunctions(_:range:).md)
  Sets a range of table entries to point to an array of callable functions.
### Instance Properties
- [var gpuResourceID: MTLResourceID](mtlvisiblefunctiontable/gpuresourceid.md)

## Relationships

### Inherits From
- [MTLAllocation](mtlallocation.md)
- [MTLResource](mtlresource.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MTLFunctionDescriptor](mtlfunctiondescriptor.md)
  A description of a function object to create.
- [protocol MTLFunction](mtlfunction.md)
  An object that represents a public shader function in a Metal library.
- [protocol MTLFunctionHandle](mtlfunctionhandle.md)
  An object representing a function that you can add to a visible function table.
- [class MTLVisibleFunctionTableDescriptor](mtlvisiblefunctiontabledescriptor.md)
  A specification of how to create a visible function table.
- [class MTLIntersectionFunctionDescriptor](mtlintersectionfunctiondescriptor.md)
  A description of an intersection function that performs an intersection test.
- [class MTLIntersectionFunctionTableDescriptor](mtlintersectionfunctiontabledescriptor.md)
  A specification of how to create an intersection function table.
- [protocol MTLIntersectionFunctionTable](mtlintersectionfunctiontable.md)
  A table of intersection functions that Metal calls to perform ray-tracing intersection tests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlvisiblefunctiontable)*
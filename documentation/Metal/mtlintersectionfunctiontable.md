# MTLIntersectionFunctionTable

**Framework**: Metal  
**Kind**: protocol

A table of intersection functions that Metal calls to perform ray-tracing intersection tests.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
protocol MTLIntersectionFunctionTable : MTLResource
```

#### Overview

Don’t implement this protocol yourself. Instead create a [`MTLIntersectionFunctionTableDescriptor`](mtlintersectionfunctiontabledescriptor.md) object and configure its properties. Then call the appropriate method on the pipeline state object that you want to use this table with:

If you use the same ray-tracing functions with more than one pipeline, make a separate table for each.

Use the methods on this object to set the table entries to point at the intersection functions, and to provide buffers as arguments for those functions. For more information about intersection functions, see [`Metal Shading Language Specification`](https://developer.apple.comhttps://developer.apple.com/metal/Metal-Shading-Language-Specification.pdf).

## Topics

### Setting a Table Entry
- [func setFunction((any MTLFunctionHandle)?, index: Int)](mtlintersectionfunctiontable/setfunction(_:index:).md)
  Sets an entry in the table.
- [func setFunctions([(any MTLFunctionHandle)?], range: Range<Int>)](mtlintersectionfunctiontable/setfunctions(_:range:).md)
  Sets a range of entries in the table.
### Specifying Arguments for Intersection Functions
- [func setBuffer((any MTLBuffer)?, offset: Int, index: Int)](mtlintersectionfunctiontable/setbuffer(_:offset:index:).md)
  Sets a buffer for the intersection functions.
- [func setBuffers([(any MTLBuffer)?], offsets: [Int], range: Range<Int>)](mtlintersectionfunctiontable/setbuffers(_:offsets:range:).md)
  Sets a range of buffers for the intersection functions.
- [func setVisibleFunctionTable((any MTLVisibleFunctionTable)?, bufferIndex: Int)](mtlintersectionfunctiontable/setvisiblefunctiontable(_:bufferindex:).md)
  Sets a visible function table for the intersection functions.
- [func setVisibleFunctionTables([(any MTLVisibleFunctionTable)?], bufferRange: Range<Int>)](mtlintersectionfunctiontable/setvisiblefunctiontables(_:bufferrange:).md)
  Sets a range of visible function tables for the intersection functions.
### Specifying Opaque Triangle Intersection Testing
- [func setOpaqueTriangleIntersectionFunction(signature: MTLIntersectionFunctionSignature, index: Int)](mtlintersectionfunctiontable/setopaquetriangleintersectionfunction(signature:index:).md)
  Sets an entry in the intersection table to point to a system-defined opaque triangle intersection function.
- [func setOpaqueTriangleIntersectionFunction(signature: MTLIntersectionFunctionSignature, range: NSRange)](mtlintersectionfunctiontable/setopaquetriangleintersectionfunction(signature:range:).md)
  Sets a range of entries in the intersection table to point to a system-defined opaque triangle intersection function.
### Instance Properties
- [var gpuResourceID: MTLResourceID](mtlintersectionfunctiontable/gpuresourceid.md)
### Instance Methods
- [func setOpaqueCurveIntersectionFunction(signature: MTLIntersectionFunctionSignature, index: Int)](mtlintersectionfunctiontable/setopaquecurveintersectionfunction(signature:index:).md)
- [func setOpaqueCurveIntersectionFunction(signature: MTLIntersectionFunctionSignature, range: NSRange)](mtlintersectionfunctiontable/setopaquecurveintersectionfunction(signature:range:).md)

## Relationships

### Inherits From
- [MTLAllocation](mtlallocation.md)
- [MTLResource](mtlresource.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MTLIntersectionFunctionTableDescriptor](mtlintersectionfunctiontabledescriptor.md)
  A specification of how to create an intersection function table.
- [class MTLIntersectionFunctionDescriptor](mtlintersectionfunctiondescriptor.md)
  A description of an intersection function that performs an intersection test.
- [struct MTLIntersectionFunctionSignature](mtlintersectionfunctionsignature.md)
  Constants for specifying different types of custom intersection functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlintersectionfunctiontable)*
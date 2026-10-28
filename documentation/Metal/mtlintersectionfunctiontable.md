# MTLIntersectionFunctionTable

**Framework**: Metal  
**Kind**: protocol  
**Role**: Protocol

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

```objc
@protocol MTLIntersectionFunctionTable <MTLResource>
```

## Overview

Don’t implement this protocol yourself. Instead create an [`MTLIntersectionFunctionTableDescriptor`](./mtlintersectionfunctiontabledescriptor.md) instance and configure its properties. Then call the appropriate method on the pipeline state that you want to use this table with:

- **Compute pipeline**: [`makeIntersectionFunctionTable(descriptor:)`](./mtlcomputepipelinestate/makeintersectionfunctiontable%28descriptor%29.md)
- **Render pipeline**: [`makeIntersectionFunctionTable(descriptor:stage:)`](./mtlrenderpipelinestate/makeintersectionfunctiontable%28descriptor,stage%29.md)

If you use the same ray-tracing functions with more than one pipeline, make a separate table for each.

Use the methods on this instance to set the table entries to point at the intersection functions, and to provide buffers as arguments for those functions. For more information about intersection functions, see [Metal Shading Language Specification](https://developer.apple.com/metal/Metal-Shading-Language-Specification.pdf).

## Topics

### Setting a table entry
- [func setFunction((any MTLFunctionHandle)?, index: Int)](./mtlintersectionfunctiontable/setfunction%28_,index%29.md)
  Sets an entry in the table.
- [func setFunctions([(any MTLFunctionHandle)?], range: Range<Int>)](./mtlintersectionfunctiontable/setfunctions%28_,range%29.md)
  Sets a range of entries in the table.
- [- setFunctions:withRange:](./mtlintersectionfunctiontable/setfunctions_withrange_.md)
  Sets a range of entries in the table.
### Specifying arguments for intersection functions
- [func setBuffer((any MTLBuffer)?, offset: Int, index: Int)](./mtlintersectionfunctiontable/setbuffer%28_,offset,index%29.md)
  Sets a buffer for the intersection functions.
- [func setBuffers([(any MTLBuffer)?], offsets: [Int], range: Range<Int>)](./mtlintersectionfunctiontable/setbuffers%28_,offsets,range%29.md)
  Sets a range of buffers for the intersection functions.
- [func setVisibleFunctionTable((any MTLVisibleFunctionTable)?, bufferIndex: Int)](./mtlintersectionfunctiontable/setvisiblefunctiontable%28_,bufferindex%29.md)
  Sets a visible function table for the intersection functions.
- [func setVisibleFunctionTables([(any MTLVisibleFunctionTable)?], bufferRange: Range<Int>)](./mtlintersectionfunctiontable/setvisiblefunctiontables%28_,bufferrange%29.md)
  Sets a range of visible function tables for the intersection functions.
- [- setBuffers:offsets:withRange:](./mtlintersectionfunctiontable/setbuffers_offsets_withrange_.md)
  Sets a range of buffers for the intersection functions.
- [- setVisibleFunctionTables:withBufferRange:](./mtlintersectionfunctiontable/setvisiblefunctiontables_withbufferrange_.md)
  Sets a range of visible function tables for the intersection functions.
### Specifying opaque triangle intersection testing
- [func setOpaqueTriangleIntersectionFunction(signature: MTLIntersectionFunctionSignature, index: Int)](./mtlintersectionfunctiontable/setopaquetriangleintersectionfunction%28signature,index%29.md)
  Sets an entry in the intersection table to point to a system-defined opaque triangle intersection function.
- [func setOpaqueTriangleIntersectionFunction(signature: MTLIntersectionFunctionSignature, range: NSRange)](./mtlintersectionfunctiontable/setopaquetriangleintersectionfunction%28signature,range%29.md)
  Sets a range of entries in the intersection table to point to a system-defined opaque triangle intersection function.
### Instance Properties
- [var gpuResourceID: MTLResourceID](./mtlintersectionfunctiontable/gpuresourceid.md)
### Instance Methods
- [func setOpaqueCurveIntersectionFunction(signature: MTLIntersectionFunctionSignature, index: Int)](./mtlintersectionfunctiontable/setopaquecurveintersectionfunction%28signature,index%29.md)
- [func setOpaqueCurveIntersectionFunction(signature: MTLIntersectionFunctionSignature, range: NSRange)](./mtlintersectionfunctiontable/setopaquecurveintersectionfunction%28signature,range%29.md)

## Relationships

### Inherits From
- [MTLAllocation](./mtlallocation.md)
- [MTLResource](./mtlresource.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Intersection function tables
- [class MTLIntersectionFunctionTableDescriptor](./mtlintersectionfunctiontabledescriptor.md)
  A specification of how to create an intersection function table.
- [class MTLIntersectionFunctionDescriptor](./mtlintersectionfunctiondescriptor.md)
  A description of an intersection function that performs an intersection test.
- [struct MTLIntersectionFunctionSignature](./mtlintersectionfunctionsignature.md)
  Constants for specifying different types of custom intersection functions.
- [struct MTLIntersectionFunctionBufferArguments](./mtlintersectionfunctionbufferarguments.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlintersectionfunctiontable)*
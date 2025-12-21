# MTLIntersectionFunctionSignature

**Framework**: Metal  
**Kind**: struct

Constants for specifying different types of custom intersection functions.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct MTLIntersectionFunctionSignature
```

#### Overview

For more information on declaring intersection functions in MSL, see [`Metal Shading Language Specification`](https://developer.apple.comhttps://developer.apple.com/metal/Metal-Shading-Language-Specification.pdf).

## Topics

### Initializing the intersection function signature
- [init(rawValue: UInt)](mtlintersectionfunctionsignature/init(rawvalue:).md)
  Returns a new signature description from a specified raw value.
### Specifying the intersection function signature
- [static var instancing: MTLIntersectionFunctionSignature](mtlintersectionfunctionsignature/instancing.md)
  A flag indicating that function signature uses instancing.
- [static var triangleData: MTLIntersectionFunctionSignature](mtlintersectionfunctionsignature/triangledata.md)
  A flag indicating that function signature uses triangle data.
- [static var worldSpaceData: MTLIntersectionFunctionSignature](mtlintersectionfunctionsignature/worldspacedata.md)
  A flag indicating that function signature uses world space data.
### Type Properties
- [static var curveData: MTLIntersectionFunctionSignature](mtlintersectionfunctionsignature/curvedata.md)
- [static var extendedLimits: MTLIntersectionFunctionSignature](mtlintersectionfunctionsignature/extendedlimits.md)
- [static var instanceMotion: MTLIntersectionFunctionSignature](mtlintersectionfunctionsignature/instancemotion.md)
- [static var intersectionFunctionBuffer: MTLIntersectionFunctionSignature](mtlintersectionfunctionsignature/intersectionfunctionbuffer.md)
- [static var maxLevels: MTLIntersectionFunctionSignature](mtlintersectionfunctionsignature/maxlevels.md)
- [static var primitiveMotion: MTLIntersectionFunctionSignature](mtlintersectionfunctionsignature/primitivemotion.md)
- [static var userData: MTLIntersectionFunctionSignature](mtlintersectionfunctionsignature/userdata.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [protocol MTLIntersectionFunctionTable](mtlintersectionfunctiontable.md)
  A table of intersection functions that Metal calls to perform ray-tracing intersection tests.
- [class MTLIntersectionFunctionTableDescriptor](mtlintersectionfunctiontabledescriptor.md)
  A specification of how to create an intersection function table.
- [class MTLIntersectionFunctionDescriptor](mtlintersectionfunctiondescriptor.md)
  A description of an intersection function that performs an intersection test.
- [struct MTLIntersectionFunctionBufferArguments](mtlintersectionfunctionbufferarguments.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlintersectionfunctionsignature)*
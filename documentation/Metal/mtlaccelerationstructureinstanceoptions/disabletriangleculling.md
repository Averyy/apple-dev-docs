# disableTriangleCulling

**Framework**: Metal  
**Kind**: property  
**Role**: Type Property

An option that turns off culling for this instance if ray intersector has culling enabled.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
static var disableTriangleCulling: MTLAccelerationStructureInstanceOptions { get }
```

```c
MTLAccelerationStructureInstanceOptionDisableTriangleCulling
```

## See Also

### Usage options
- [static var triangleFrontFacingWindingCounterClockwise: MTLAccelerationStructureInstanceOptions](./trianglefrontfacingwindingcounterclockwise.md)
  Specifies that the instance specifies front facing triangles in counter-clockwise order.
- [static var opaque: MTLAccelerationStructureInstanceOptions](./opaque.md)
  Specifies that intersectors should treat the instance as opaque.
- [static var nonOpaque: MTLAccelerationStructureInstanceOptions](./nonopaque.md)
  Specifies that intersectors should treat the instance as non-opaque.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructureinstanceoptions/disabletriangleculling)*
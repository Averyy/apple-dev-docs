# intersectionFunctionTableOffset

**Framework**: Metal  
**Kind**: property

Sets the offset that this geometry contributes to determining the intersection function to invoke when a ray intersects it.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var intersectionFunctionTableOffset: Int { get set }
```

#### Discussion

When you perform a ray tracing operation in the Metal Shading Language, and provide the ray intersector object with an instance of [`MTLIntersectionFunctionTable`](mtlintersectionfunctiontable.md), Metal adds this offset to the instance offset from structs such as:

- [`MTLAccelerationStructureInstanceDescriptor`](mtlaccelerationstructureinstancedescriptor.md)
- [`MTLAccelerationStructureUserIDInstanceDescriptor`](mtlaccelerationstructureuseridinstancedescriptor.md)
- [`MTLAccelerationStructureMotionInstanceDescriptor`](mtlaccelerationstructuremotioninstancedescriptor.md)
- [`MTLIndirectAccelerationStructureInstanceDescriptor`](mtlindirectaccelerationstructureinstancedescriptor.md)
- [`MTLIndirectAccelerationStructureMotionInstanceDescriptor`](mtlindirectaccelerationstructuremotioninstancedescriptor.md)

The sum of these offsets provides an index into the intersection function table that the ray tracing system uses to retrieve and invoke the function at this index, allowing you to customize the intersection evaluation process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4accelerationstructuregeometrydescriptor/intersectionfunctiontableoffset)*
# MPSAccelerationStructureCompletionHandler

**Framework**: Metal Performance Shaders  
**Kind**: typealias  
**Role**: Type Alias

A block of code that’s invoked when an operation on an acceleration structure has completed.

**Availability**:
- iOS 12.0+ - Deprecated in 17.0
- iPadOS 12.0+ - Deprecated in 17.0
- Mac Catalyst 13.0+ - Deprecated in 17.0
- macOS 10.14+ - Deprecated in 14.0
- tvOS 12.0+ - Deprecated in 17.0
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
typealias MPSAccelerationStructureCompletionHandler = (MPSAccelerationStructure?) -> Void
```

```c
typedef void (^)(MPSAccelerationStructure *) MPSAccelerationStructureCompletionHandler;
```

## See Also

### Data Types
- [typealias MPSAxisAlignedBoundingBox](./mpsaxisalignedboundingbox-swift.typealias.md)
  An axis-aligned bounding box.
- [typealias MPSDeviceCaps](./mpsdevicecaps.md)
- [typealias MPSFunctionConstant](./mpsfunctionconstant.md)
- [typealias MPSFunctionConstantInMetal](./mpsfunctionconstantinmetal.md)
- [typealias MPSGradientNodeBlock](./mpsgradientnodeblock.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsaccelerationstructurecompletionhandler)*
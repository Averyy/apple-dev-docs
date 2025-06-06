# init(accelerationStructureSize:buildScratchBufferSize:refitScratchBufferSize:)

**Framework**: Metal  
**Kind**: init

Creates an acceleration sizes instance with specific values.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
init(accelerationStructureSize: Int, buildScratchBufferSize: Int, refitScratchBufferSize: Int)
```

## Parameters

- `accelerationStructureSize`: The size of the acceleration structure, in bytes.
- `buildScratchBufferSize`: The amount of scratch memory, in bytes, the GPU devices needs to build the acceleration structure.
- `refitScratchBufferSize`: The amount of scratch memory, in bytes, the GPU device needs to refit the acceleration structure.

## See Also

- [init()](mtlaccelerationstructuresizes/init.md)
  Creates an acceleration sizes instance with default values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructuresizes/init(accelerationstructuresize:buildscratchbuffersize:refitscratchbuffersize:))*
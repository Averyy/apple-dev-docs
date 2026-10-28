# init(flags:)

**Framework**: PHASE  
**Kind**: init  
**Role**: Initializer

Creates a spatial pipeline with the specified flags.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
init?(flags: PHASESpatialPipeline.Flags)
```

```objc
- (instancetype) initWithFlags:(PHASESpatialPipelineFlags) flags;
```

## Discussion

This initializer returns `nil` for a `nil` `flags` argument.

## Parameters

- `flags`: An array of sound-resonance effects to include in the spatial pipeline’s output. The framework adds an entry to the [`entries`](./entries.md) property for each element that the app includes in this collection.

## See Also

### Creating a Spatial Pipeline
- [PHASESpatialPipeline.Flags](./flags-swift.struct.md)
  Sound resonance options for a spatial pipeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasespatialpipeline/init(flags:))*
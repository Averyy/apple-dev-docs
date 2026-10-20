# init(spatialPipeline:identifier:)

**Framework**: PHASE  
**Kind**: init  
**Role**: Initializer

Creates a named mixer with the designated spatial pipeline.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(spatialPipeline: PHASESpatialPipeline, identifier: String)
```

```objc
- (instancetype) initWithSpatialPipeline:(PHASESpatialPipeline *) spatialPipeline identifier:(NSString *) identifier;
```

## Parameters

- `spatialPipeline`: An object that features optional sound resonance effects.
- `identifier`: A unique name for the spatial mixer.

## See Also

### Creating a Spatial Mixer
- [init(spatialPipeline: PHASESpatialPipeline)](./init%28spatialpipeline%29.md)
  Creates a mixer with the designated spatial pipeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasespatialmixerdefinition/init(spatialpipeline:identifier:))*
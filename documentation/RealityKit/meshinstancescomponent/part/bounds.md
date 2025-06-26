# bounds

**Framework**: RealityKit  
**Kind**: property

The bounding box to use for the instance group drawn by this part. This bounds should encompass all of your instances.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var bounds: BoundingBox?
```

#### Discussion

If bounds is nil, RealityKit calculates a bounding box for you each time you update your instances within LowLevelInstanceData

> ⚠️ **Warning**: Automatic bounds calculation is not supported when LowLevelInstanceData is updated via replace(using:). A non-nil bounds value must be provided when updating instances with Metal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshinstancescomponent/part/bounds)*
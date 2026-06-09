# commandQueue

**Framework**: RealityKit  
**Kind**: property

If this scene uses a MTLCommandQueue for rendering, returns it.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency var commandQueue: (any MTLCommandQueue)? { get }
```

#### Discussion

You use this command queue for GPU workloads that need consistent ordering relative to RealityKit’s scene rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene/commandqueue)*
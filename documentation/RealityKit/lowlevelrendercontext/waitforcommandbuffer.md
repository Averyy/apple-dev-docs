# waitForCommandBuffer(_:)

**Framework**: RealityKit  
**Kind**: method  
**Required**: Yes

Adds a command buffer that the renderer should wait on before using resources for rendering.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func waitForCommandBuffer(_ commandBuffer: any MTLCommandBuffer)
```

#### Discussion

Instead of passing the same command buffer to every individual `replace(commandBuffer:)` call, you can call this method once and then pass `nil` to each GPU replace call on this context. The renderer waits for this command buffer to complete before using any of those resources for rendering.

## Parameters

- `commandBuffer`: The command buffer whose completion the renderer waits for before using the updated GPU resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendercontext/waitforcommandbuffer(_:))*
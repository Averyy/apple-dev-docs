# presentOnSceneUpdate()

**Framework**: RealityKit  
**Kind**: method

Presents the updated texture to the renderer atomically with the current scene update.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func presentOnSceneUpdate()
```

#### Discussion

Needs to be called after all commands in the command buffer have been executed (e.g. after `MTLCommandBuffer.waitUntilCompleted()`). When you call this method, the drawable will make the new texture content available to the renderer at the same time as all other entity component changes made during the same scene update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/textureresource/drawable/presentonsceneupdate())*
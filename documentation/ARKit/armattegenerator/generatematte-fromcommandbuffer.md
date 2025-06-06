# generateMatte(from:commandBuffer:)

**Framework**: ARKit  
**Kind**: method

Generates alpha matte at either full resolution or half the resolution of the captured image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func generateMatte(from frame: ARFrame, commandBuffer: any MTLCommandBuffer) -> any MTLTexture
```

#### Return Value

An alpha matte texture at the resolution you chose at initialization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/armattegenerator/generatematte(from:commandbuffer:))*
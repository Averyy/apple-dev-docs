# generateMatte(from:commandBuffer:)

**Framework**: ARKit  
**Kind**: method  
**Role**: Instance Method

Generates alpha matte at either full resolution or half the resolution of the captured image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

## Declaration

```swift
func generateMatte(from frame: ARFrame, commandBuffer: any MTLCommandBuffer) -> any MTLTexture
```

```objc
- (id<MTLTexture>) generateMatteFromFrame:(ARFrame *) frame commandBuffer:(id<MTLCommandBuffer>) commandBuffer;
```

## Return Value

An alpha matte texture at the resolution you chose at initialization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/armattegenerator/generatematte(from:commandbuffer:))*
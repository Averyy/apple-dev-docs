# init(device:matteResolution:)

**Framework**: ARKit  
**Kind**: init  
**Role**: Initializer

Creates an AR matte generator.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

## Declaration

```swift
init(device: any MTLDevice, matteResolution: ARMatteGenerator.Resolution)
```

```objc
- (instancetype) initWithDevice:(id<MTLDevice>) device matteResolution:(ARMatteResolution) matteResolution;
```

#### Discussion

To create matte textures in real-time, create this object once and reuse it every frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/armattegenerator/init(device:matteresolution:))*
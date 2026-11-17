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

## Discussion

To create matte textures in real-time, create this object once and reuse it every frame.

> **See Also**: [`ARFrame`](../arframe.md)

> **See Also**: [`generateMatte(from:commandBuffer:)`](./generatematte%28from,commandbuffer%29.md)

> **See Also**: [`ARMatteGenerator.Resolution`](./resolution.md)

## Parameters

- `device`: The device the filter will run on.
- `matteResolution`: The resolution at which the matte is to be generated. Set using one of the values from ‘ARMatteResolution’.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/armattegenerator/init(device:matteresolution:))*
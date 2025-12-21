# init(originFromAnchorTransform:width:height:cameraEnhancement:)

**Framework**: ARKit  
**Kind**: init

Initialize a camera region anchor.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
init(originFromAnchorTransform: simd_float4x4, width: Float, height: Float, cameraEnhancement: CameraRegionAnchor.CameraEnhancement)
```

## Parameters

- `originFromAnchorTransform`: The transform from the anchor to the origin coordinate system.
- `width`: The width of the region, in meters.
- `height`: The height of the region, in meters.
- `cameraEnhancement`: The camera enhancement used with this anchor. This will affect the frame rate of the output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/cameraregionanchor/init(originfromanchortransform:width:height:cameraenhancement:))*
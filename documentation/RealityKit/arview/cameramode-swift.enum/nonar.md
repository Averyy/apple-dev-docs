# ARView.CameraMode.nonAR

**Framework**: RealityKit  
**Kind**: case

A mode that creates a fully virtual environment with no relationship to the real world.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+

## Declaration

```swift
case nonAR
```

#### Discussion

Use this mode to create pure virtual 3D environments using [`ARView`](arview.md). RealityKit doesn’t place `.nonAR` content into the real world and, as a result, doesn’t require a front-facing device camera.

## See Also

- [ARView.CameraMode.ar](arview/cameramode-swift.enum/ar.md)
  A mode that uses the device’s camera to place virtual entities relative to the real world.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/cameramode-swift.enum/nonar)*
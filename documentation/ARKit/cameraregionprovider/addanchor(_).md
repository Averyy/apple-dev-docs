# addAnchor(_:)

**Framework**: ARKit  
**Kind**: method  
**Role**: Instance Method

Add a camera region anchor.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
final func addAnchor(_ anchor: CameraRegionAnchor) async throws
```

#### Discussion

> **Throws**: `CameraRegionProvider.Error`

> **Note**: This could fail if the maximum anchors for the given camera enhancement has been reached.

## Parameters

- `anchor`: The anchor to add.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/cameraregionprovider/addanchor(_:))*
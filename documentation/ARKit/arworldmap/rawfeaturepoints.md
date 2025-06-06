# rawFeaturePoints

**Framework**: ARKit  
**Kind**: property

A coarse representation of the space-mapping data recorded in the world map.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var rawFeaturePoints: ARPointCloud { get }
```

#### Discussion

These points represent notable features detected in camera imagery during the session that recorded the world map. ARKit extrapolates the locations of these features in 3D world coordinate space as part of the image and motion analysis that tracks the device’s movement in a session. Taken together, these points loosely correlate to the contours of real-world objects that were in view of the camera during the session.

ARKit does not guarantee that the number and arrangement of raw feature points will remain stable between software releases. However, you can visualize the point cloud to debug your world map recording, or inspect its size to estimate the quality of a recorded world map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arworldmap/rawfeaturepoints)*
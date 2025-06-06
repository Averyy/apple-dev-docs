# init(from:zoom:name:)

**Framework**: DeveloperToolsSupport  
**Kind**: init

Creates a camera that looks toward the preview center from a specified unit point.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
init(from point: UnitPoint3D, zoom: Double = 1, name: String? = nil)
```

#### Discussion

Use one or more cameras with one of the preview macros that takes a `cameras` input — like [`Preview(_:traits:body:cameras:)`](https://developer.apple.com/documentation/SwiftUI/Preview(_:traits:body:cameras:)) — to create custom viewpoints for the preview. The canvas offers custom cameras in its camera picker along with a set of standard cameras.

## Parameters

- `point`: The point in 3D space where to place the camera, given as   a unit point relative to the preview center.
- `zoom`: An optional amount by which to scale the distance from the   camera to the preview center. Values larger than   move the camera   closer to the preview center. Fractional values move the camera   away.
- `name`: An optional name that the canvas uses to label the camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/developertoolssupport/previewcamera/init(from:zoom:name:))*
# init(lookingAt:from:name:)

**Framework**: DeveloperToolsSupport  
**Kind**: init

Creates a camera that looks towards a specified point in the preview from a different specified point.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
init(lookingAt position: Point3D, from: Point3D, name: String? = nil)
```

#### Discussion

Use one or more cameras with one of the preview macros that takes a `cameras` input — like [`Preview(_:traits:body:cameras:)`](https://developer.apple.com/documentation/SwiftUI/Preview(_:traits:body:cameras:)) — to create custom viewpoints for the preview. The canvas offers custom cameras in its camera picker along with a set of standard cameras.

## Parameters

- `position`: The point to aim the camera at, specified in meters from   the preview center.
- `from`: The position of the camera, specified in meters from the   preview center.
- `name`: An optional name that the canvas uses to label the camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/developertoolssupport/previewcamera/init(lookingat:from:name:))*
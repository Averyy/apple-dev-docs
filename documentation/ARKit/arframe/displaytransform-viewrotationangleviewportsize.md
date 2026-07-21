# displayTransform(viewRotationAngle:viewportSize:)

**Framework**: ARKit  
**Kind**: method

Returns a display transform for the provided viewport size and view angle.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)

## Declaration

```swift
func displayTransform(viewRotationAngle: CGFloat, viewportSize: CGSize) -> CGAffineTransform
```

#### Return Value

The display transform matrix.

#### Discussion

The display transform can be used to convert normalized points in the image-space coordinate system of the captured image to normalized points in the view’s coordinate space. The transform provides the correct rotation and aspect-fill for presenting the captured image in the given view angle and size.

The view angle, in degrees, is the clockwise rotation needed to keep the camera image level with the horizon (`0` LandscapeRight, `90` Portrait, `180` LandscapeLeft, `270` PortraitUpsideDown). Obtain it from `ARSession.viewRotationAngle`.

## Parameters

- `viewRotationAngle`: The view rotation angle, in degrees, of the viewport.
- `viewportSize`: The size of the viewport.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arframe/displaytransform(viewrotationangle:viewportsize:))*
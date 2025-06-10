# extrinsicMatrix(from:to:)

**Framework**: AVFoundation  
**Kind**: method

Returns the relative extrinsic matrix from one capture device to another.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
class func extrinsicMatrix(from fromDevice: AVCaptureDevice, to toDevice: AVCaptureDevice) -> Data?
```

#### Return Value

A [`Data`](https://developer.apple.com/documentation/Foundation/Data) containing a [`matrix_float4x3`](https://developer.apple.com/documentation/simd/matrix_float4x3) matrix, which is a column major with 3 rows and 4 columns.

#### Discussion

The extrinsic matrix consists of a unitless 3x3 rotation matrix (R) on the left and a translation (t) 3x1 column vector on the right, whose units are millimeters. The matrix expresses the destination camera’s extrinsics relative to the source camera. If `X_from` is a 3D point in the source camera’s coordinate system, you project it into the destination camera’s coordinate system with `X_to = [R | t] * X_from`.

Only physical cameras for which factory calibrations exist provide an extrinsic matrix. Virtual device cameras return `nil`.

> ❗ **Important**:  If you enable video stabilization by setting a [`preferredVideoStabilizationMode`](avcaptureconnection/preferredvideostabilizationmode.md) value, the pixels in stabilized video frames no longer match the relative extrinsic matrix from one device to another due to warping. Disable video stabilization if you’re using the extrinsic matrix and camera intrinsics.

## Parameters

- `fromDevice`: The capture device that represents the source camera.
- `toDevice`: The capture device that represents the destination camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedevice/extrinsicmatrix(from:to:))*
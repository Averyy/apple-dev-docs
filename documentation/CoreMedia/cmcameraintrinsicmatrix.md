# CMCameraIntrinsicMatrix

**Framework**: Core Media  
**Kind**: struct

A matrix that describes the camera’s intrinsic properties.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct CMCameraIntrinsicMatrix
```

#### Overview

This matrix has the following content

```None
 fx  0   ox
 0   fy  oy
 0   0   1
```

fx and fy are the focal length in pixels. For square pixels, they will have the same value. ox and oy are the coordinates of the principal point. The origin is the upper left of the frame.

## Topics

### Initializers
- [init(matrix: simd_float3x3)](cmcameraintrinsicmatrix/init(matrix:).md)
### Instance Properties
- [var matrix: simd_float3x3](cmcameraintrinsicmatrix/matrix.md)

## Relationships

### Conforms To
- [CVAttachmentValueRepresentable](../corevideo/cvattachmentvaluerepresentable.md)
- [Equatable](../swift/equatable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmcameraintrinsicmatrix)*
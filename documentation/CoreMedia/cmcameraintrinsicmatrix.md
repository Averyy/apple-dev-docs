# CMCameraIntrinsicMatrix

**Framework**: Core Media  
**Kind**: struct  
**Role**: Structure

A matrix that describes the camera’s intrinsic properties.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct CMCameraIntrinsicMatrix
```

## Overview

This matrix has the following content

```
 fx  0   ox
 0   fy  oy
 0   0   1
```

fx and fy are the focal length in pixels. For square pixels, they will have the same value. ox and oy are the coordinates of the principal point. The origin is the upper left of the frame.

## Topics

### Initializers
- [init(matrix: simd_float3x3)](./cmcameraintrinsicmatrix/init%28matrix%29.md)
### Instance Properties
- [var matrix: simd_float3x3](./cmcameraintrinsicmatrix/matrix.md)

## Relationships

### Conforms To
- [CVAttachmentValueRepresentable](../CoreVideo/cvattachmentvaluerepresentable.md)
- [Equatable](../Swift/equatable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmcameraintrinsicmatrix)*
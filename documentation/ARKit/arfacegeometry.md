# ARFaceGeometry

**Framework**: ARKit  
**Kind**: class  
**Role**: Class

A 3D mesh describing face topology for use in face-tracking AR sessions.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```swift
class ARFaceGeometry
```

```objc
@interface ARFaceGeometry : NSObject
```

## Overview

This class provides a general model for the detailed topology of a face, in the form of a 3D mesh appropriate for use with various rendering technologies or for exporting 3D assets. (For a quick way to visualize a face geometry using SceneKit, see the [`ARSCNFaceGeometry`](./arscnfacegeometry.md) class.)

When you obtain a face geometry from an [`ARFaceAnchor`](./arfaceanchor.md) object in a face-tracking AR session, the model conforms to match the dimensions, shape, and current expression of the detected face. You can also create a face mesh using a dictionary of named blend shape coefficients, which provides a detailed, but more efficient, description of the face’s current expression.

In an AR session, you can use this model as the basis for overlaying content that follows the shape of the user’s face—for example, to apply virtual makeup or tattoos. You can also use this model to create occlusion geometry, which hides other virtual content behind the 3D shape of the detected face in the camera image.

> **Note**:  Face mesh topology is constant across [`ARFaceGeometry`](./arfacegeometry.md) instances. That is, the values of the [`vertexCount`](./arfacegeometry/vertexcount.md), [`textureCoordinateCount`](./arfacegeometry/texturecoordinatecount.md), and [`triangleCount`](./arfacegeometry/trianglecount.md) properties never change, the [`triangleIndices`](./arfacegeometry/triangleindices-3tb1o.md) buffer always describes the same arrangement of vertices, and the [`textureCoordinates`](./arfacegeometry/texturecoordinates-8ahq1.md) buffer always maps the same vertex indices to the same texture coordinates.
>
> Only the [`vertices`](./arfacegeometry/vertices-fhdb.md) buffer changes between face meshes provided by an AR session, indicating the change in vertex positions as ARKit adapts the mesh to the shape and expression of the user’s face.

## Topics

### Accessing Mesh Data
- [var vertices: [simd_float3]](./arfacegeometry/vertices-7qq1y.md)
  An array of vertex positions for each point in the face mesh.
- [var textureCoordinates: [vector_float2]](./arfacegeometry/texturecoordinates-u42d.md)
  An array of texture coordinate values for each point in the face mesh.
- [var triangleCount: Int](./arfacegeometry/trianglecount.md)
  The number of triangles described by the [`triangleIndices`](./arfacegeometry/triangleindices-3tb1o.md) buffer.
- [var triangleIndices: [Int16]](./arfacegeometry/triangleindices-8isy8.md)
  An array of indices describing the triangle mesh formed by the face geometry’s vertex data.
- [vertexCount](./arfacegeometry/vertexcount.md)
  The number of elements in the [`vertices`](./arfacegeometry/vertices-fhdb.md) buffer.
- [vertices](./arfacegeometry/vertices-fhdb.md)
  A buffer of vertex positions for each point in the face mesh.
- [textureCoordinateCount](./arfacegeometry/texturecoordinatecount.md)
  The number of elements in the [`textureCoordinates`](./arfacegeometry/texturecoordinates-8ahq1.md) buffer.
- [textureCoordinates](./arfacegeometry/texturecoordinates-8ahq1.md)
  A buffer of texture coordinate values for each point in the face mesh.
- [triangleIndices](./arfacegeometry/triangleindices-3tb1o.md)
  A buffer of indices describing the triangle mesh formed by the face geometry’s vertex data.
### Creating a Mesh from Blend Shapes
- [init?(blendShapes: [ARFaceAnchor.BlendShapeLocation : NSNumber])](./arfacegeometry/init%28blendshapes%29.md)
  Creates a face geometry matching the facial expression described in the specified dictionary.
### Initializers
- [init?(coder: NSCoder)](./arfacegeometry/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Face Data
- [Tracking and visualizing faces](./tracking-and-visualizing-faces.md)
  Detect faces in a front-camera AR experience, overlay virtual content, and animate facial expressions in real-time.
- [Combining user face-tracking and world tracking](./combining-user-face-tracking-and-world-tracking.md)
  Track the user’s face in an app that displays an AR experience with the rear camera.
- [class ARSCNFaceGeometry](./arscnfacegeometry.md)
  A SceneKit representation of face topology for use with face information that an AR session provides.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arfacegeometry)*
# createReferenceObject(transform:center:extent:completionHandler:)

**Framework**: ARKit  
**Kind**: method

Creates a reference object (for 3D object detection) from the specified region of the session’s world space.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
func createReferenceObject(transform: simd_float4x4, center: simd_float3, extent: simd_float3) async throws -> ARReferenceObject
```

#### Discussion

> ❗ **Important**: This method is valid only when running a session with [`ARObjectScanningConfiguration`](arobjectscanningconfiguration.md), which enables the high-fidelity spatial data collection needed for scanning reference objects. Calling this method on a session with a different configuration immediately invokes your `completionHandler` with an error.

To use the extracted reference object for 3D object detection, assign it to the [`detectionObjects`](arworldtrackingconfiguration/detectionobjects.md) property of a world tracking configuration. You can bundle reference objects in an app by saving them to files and adding them to an Xcode asset catalog.

When ARKit detects a reference image, the transform of the resulting [`ARObjectAnchor`](arobjectanchor.md) is based on the orgin of the reference object’s coordinate system—the transform you specify when extracting the reference object. For example, if a reference object represents a physical item that sits on a horizontal surface, virtual content should appear to sit on whatever surface the physical object does. To adjust a reference object’s origin after extracting it, use the [`applyingTransform(_:)`](arreferenceobject/applyingtransform(_:).md) method.

## Parameters

- `transform`: A transform matrix defining the origin and orientation of the local coordinate system for the region to extract.
- `center`: A point, relative to the origin specified by  , that defines the center of the bounding box for the region to extract.
- `extent`: The width, height, and depth of the region to extract, centered on the   point and oriented to the local coordinate system specified by  .
- `completionHandler`: A handler to be invoked asynchronously after ARKit finishes creating the reference object. The handler takes two parameters:


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arsession/createreferenceobject(transform:center:extent:completionhandler:))*
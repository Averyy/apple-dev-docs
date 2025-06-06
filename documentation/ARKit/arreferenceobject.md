# ARReferenceObject

**Framework**: ARKit  
**Kind**: class

The description of a 3D object that you want ARKit to detect in the physical environment.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class ARReferenceObject
```

#### Overview

Object detection in ARKit lets you trigger AR content when the session recognizes a known 3D object. For example, your app could detect sculptures in an art museum and provide a virtual curator, or detect tabletop gaming figures and create visual effects for the game.

To provide a known 3D object for detection, you scan a real-world object using ARKit:

1. Run an AR session using [`ARObjectScanningConfiguration`](arobjectscanningconfiguration.md) to enable collection of high-fidelity spatial mapping data.
2. In that session, point the device camera at the real-world object from various angles, allowing ARKit to build up an internal map of the object and its surroundings. For an example of guiding user interactions to produce good scan data, see [`Scanning and Detecting 3D Objects`](scanning-and-detecting-3d-objects.md).
3. Determine the portion of the session’s world coordinate space representing the object to be recognized, and call [`createReferenceObject(transform:center:extent:completionHandler:)`](arsession/createreferenceobject(transform:center:extent:completionhandler:).md) to get that portion as an [`ARReferenceObject`](arreferenceobject.md) ready for use in object detection.
4. To save the reference object for use later or elsewhere, use the [`export(to:previewImage:)`](arreferenceobject/export(to:previewimage:).md) method to create an `.arobject` file.

To detect objects in an AR session, pass a collection of reference objects to your session configuration’s [`detectionObjects`](arworldtrackingconfiguration/detectionobjects.md) property. You need not scan and detect objects in the same app: For example, you might create one app for scanning museum collections that outputs `.arobject` files, then bundle those files into another app meant for museum visitors.

To bundle reference objects into an app, use your Xcode project’s asset catalog:

1. In your asset catalog, use the Add (+) button to create an AR Resource Group.
2. Drag `.arobject` into the resource group to create AR Reference Object entries in the asset catalog.
3. Optionally, use the Xcode inspector panel to provide a descriptive name for the object, which appears as the [`name`](arreferenceobject/name.md) property at runtime and can be useful for debugging.

## Topics

### Loading Reference Objects
- [init(archiveURL: URL) throws](arreferenceobject/init(archiveurl:).md)
  Loads a reference object from the specified file URL.
- [class func referenceObjects(inGroupNamed: String, bundle: Bundle?) -> Set<ARReferenceObject>?](arreferenceobject/referenceobjects(ingroupnamed:bundle:).md)
  Loads all reference objects in the specified AR Resource Group in your Xcode project’s asset catalog.
### Examining a Reference Object
- [var name: String?](arreferenceobject/name.md)
  A descriptive name for the reference object.
- [var resourceGroupName: String?](arreferenceobject/resourcegroupname.md)
- [var center: simd_float3](arreferenceobject/center.md)
  The center point of the reference object’s space-mapping data.
- [var extent: simd_float3](arreferenceobject/extent.md)
  The size of the reference object’s space-mapping data.
- [var scale: simd_float3](arreferenceobject/scale.md)
  A scale factor for the local coordinate space the reference object defines.
### Saving Recorded Objects
- [func export(to: URL, previewImage: UIImage?) throws](arreferenceobject/export(to:previewimage:).md)
  Writes a binary representation of the object to the specified file URL.
- [class let archiveExtension: String](arreferenceobject/archiveextension.md)
  The standard filename extension for exported [`ARReferenceObject`](arreferenceobject.md) instances.
### Creating Derivative Reference Objects
- [func applyingTransform(simd_float4x4) -> ARReferenceObject](arreferenceobject/applyingtransform(_:).md)
  Returns a new reference object created by applying the specified transform to this reference object’s geometric data.
- [func merging(ARReferenceObject) throws -> ARReferenceObject](arreferenceobject/merging(_:).md)
  Returns a new reference object that combines spatial information from both this reference object and another.
### Debugging a Reference Object
- [var rawFeaturePoints: ARPointCloud](arreferenceobject/rawfeaturepoints.md)
  A coarse representation of the space-mapping data contained in the reference object.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Visualizing and interacting with a reconstructed scene](visualizing-and-interacting-with-a-reconstructed-scene.md)
  Estimate the shape of the physical environment using a polygonal mesh.
- [Scanning and Detecting 3D Objects](scanning-and-detecting-3d-objects.md)
  Record spatial features of real-world objects, then use the results to find those objects in the user’s environment and trigger AR content.
- [class ARObjectAnchor](arobjectanchor.md)
  An anchor for a real-world 3D object that ARKit detects in the physical environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arreferenceobject)*
# ARReferenceObject

**Framework**: ARKit  
**Kind**: class  
**Role**: Class

A 3D object that ARKit can detect or track in the scene.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+

## Declaration

```swift
class ARReferenceObject
```

```objc
@interface ARReferenceObject : NSObject
```

## Overview

Train a reference object in the Create ML app to produce a `.referenceobject` file. Load the file from a local file URL with [`init(archiveURL:)`](./arreferenceobject/init%28archiveurl%29.md), then assign the resulting reference object to either [`detectionObjects`](./arworldtrackingconfiguration/detectionobjects.md) or [`trackingObjects`](./arworldtrackingconfiguration/trackingobjects.md) on your [`ARWorldTrackingConfiguration`](./arworldtrackingconfiguration.md), depending on whether the object moves in the scene:

- Use [`detectionObjects`](./arworldtrackingconfiguration/detectionobjects.md) for objects that are mostly stationary. The system holds the pose stable in world space, consuming less power.
- Use [`trackingObjects`](./arworldtrackingconfiguration/trackingobjects.md) for moving or handheld objects when you need precise pose updates. The system tracks the object at the full frame rate of the selected [`videoFormat`](./arconfiguration/videoformat-swift.property.md).

ARKit on iOS supports the `.referenceobject` format starting in iOS 27. If you already have `.referenceobject` files from a visionOS app, you can use them in your iOS app without retraining.

> **Note**: ARKit also continues to load the older `.arobject` format (introduced in iOS 12). Those files work only with [`detectionObjects`](./arworldtrackingconfiguration/detectionobjects.md). A single session can’t mix the two formats.

## Topics

### Initializers
- [init(archiveURL: URL) throws](./arreferenceobject/init%28archiveurl%29.md)
  Loads a reference object from the specified file URL.
- [init?(coder: NSCoder)](./arreferenceobject/init%28coder%29.md)
### Instance Properties
- [var center: simd_float3](./arreferenceobject/center.md)
  The center point of the reference object’s space-mapping data.
- [var extent: simd_float3](./arreferenceobject/extent.md)
  The size of the reference object’s space-mapping data.
- [var name: String?](./arreferenceobject/name.md)
  A descriptive name for the reference object.
- [var rawFeaturePoints: ARPointCloud](./arreferenceobject/rawfeaturepoints.md)
  A coarse representation of the space-mapping data contained in the reference object.
- [var resourceGroupName: String?](./arreferenceobject/resourcegroupname.md)
- [var scale: simd_float3](./arreferenceobject/scale.md)
  A scale factor for the local coordinate space the reference object defines.
- [var usdzFile: URL?](./arreferenceobject/usdzfile.md)
  The URL to the extracted USDZ model, if available.
### Instance Methods
- [func applyingTransform(simd_float4x4) -> ARReferenceObject](./arreferenceobject/applyingtransform%28_%29.md)
  Returns a new reference object created by applying the specified transform to this reference object’s geometric data.
- [func export(to: URL, previewImage: UIImage?) throws](./arreferenceobject/export%28to,previewimage%29.md)
  Writes a binary representation of the object to the specified file URL.
- [func merging(ARReferenceObject) throws -> ARReferenceObject](./arreferenceobject/merging%28_%29.md)
  Returns a new reference object that combines spatial information from both this reference object and another.
### Type Properties
- [class let archiveExtension: String](./arreferenceobject/archiveextension.md)
  The standard filename extension for exported [`ARReferenceObject`](./arreferenceobject.md) instances.
### Type Methods
- [class func referenceObjects(inGroupNamed: String, bundle: Bundle?) -> Set<ARReferenceObject>?](./arreferenceobject/referenceobjects%28ingroupnamed,bundle%29.md)
  Loads all reference objects in the specified AR Resource Group in your Xcode project’s asset catalog.

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
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Object Tracking
- [Using a reference object with ARKit in iOS](../visionOS/using-a-reference-object-with-arkit-in-ios.md)
  Track a real-world object in your iOS app by using a reference-object file.
- [class ARObjectAnchor](./arobjectanchor.md)
  An anchor for a real-world 3D object that ARKit detects in the physical environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arreferenceobject)*
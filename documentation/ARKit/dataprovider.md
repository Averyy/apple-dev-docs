# DataProvider

**Framework**: ARKit  
**Kind**: protocol

A source of live data from ARKit.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
protocol DataProvider : AnyObject, CustomStringConvertible, Sendable
```

#### Overview

Most providers supply an asynchronous sequence of updated anchors for the provider’s data type. For example, a [`HandTrackingProvider`](handtrackingprovider.md) instance’s [`anchorUpdates`](handtrackingprovider/anchorupdates.md) property gives updates over time for hand anchors.

## Topics

### Inspecting a data provider
- [var state: DataProviderState](dataprovider/state.md)
  The current status of data coming from this provider.
### Inspecting a data provider type
- [static var requiredAuthorizations: [ARKitSession.AuthorizationType]](dataprovider/requiredauthorizations.md)
  The kinds of authorization you need to use a particular data provider type.
- [static var isSupported: Bool](dataprovider/issupported.md)
  A Boolean value that indicates whether the current runtime environment supports a particular provider type.

## Relationships

### Inherits From
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Conforming Types
- [AccessoryTrackingProvider](accessorytrackingprovider.md)
- [BarcodeDetectionProvider](barcodedetectionprovider.md)
- [CameraFrameProvider](cameraframeprovider.md)
- [CameraRegionProvider](cameraregionprovider.md)
- [EnvironmentLightEstimationProvider](environmentlightestimationprovider.md)
- [HandTrackingProvider](handtrackingprovider.md)
- [ImageTrackingProvider](imagetrackingprovider.md)
- [ObjectTrackingProvider](objecttrackingprovider.md)
- [PlaneDetectionProvider](planedetectionprovider.md)
- [RoomTrackingProvider](roomtrackingprovider.md)
- [SceneReconstructionProvider](scenereconstructionprovider.md)
- [SharedCoordinateSpaceProvider](sharedcoordinatespaceprovider.md)
- [StereoPropertiesProvider](stereopropertiesprovider.md)
- [WorldTrackingProvider](worldtrackingprovider.md)

## See Also

- [Setting up access to ARKit data](../visionOS/setting-up-access-to-arkit-data.md)
  Check whether your app can use ARKit and respect people’s privacy.
- [class ARKitSession](arkitsession.md)
  The main entry point for receiving data from ARKit.
- [protocol Anchor](anchor.md)
  The identity, location, and orientation of an object in world space.
- [ARKit in visionOS](arkit-in-visionos.md)
  Create immersive augmented reality experiences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/dataprovider)*
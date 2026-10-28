# CameraRegionProvider

**Framework**: ARKit  
**Kind**: class  
**Role**: Class

A camera region provider.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
final class CameraRegionProvider
```

## Overview

An enterprise license is required to use the CameraRegionProvider. The provider will not deliver any data without it. The app must include the [`Camera Region access`](../BundleResources/entitlements/com.apple.developer.arkit.camera-region.allow.md) entitlement.

## Topics

### Structures
- [CameraRegionProvider.Error](./cameraregionprovider/error.md)
  A camera region error.
### Initializers
- [init()](./cameraregionprovider/init%28%29.md)
  Create a camera region provider.
### Instance Properties
- [var description: String](./cameraregionprovider/description.md)
  A textual representation of this camera region provider.
- [var state: DataProviderState](./cameraregionprovider/state.md)
  The state of this camera region provider.
### Instance Methods
- [func addAnchor(CameraRegionAnchor) async throws](./cameraregionprovider/addanchor%28_%29.md)
  Add a camera region anchor.
- [func anchorUpdates(forID: UUID) -> AnchorUpdateSequence<CameraRegionAnchor>](./cameraregionprovider/anchorupdates%28forid%29.md)
  An async sequence of anchor updates for a specific anchor.
- [func removeAnchor(CameraRegionAnchor) async throws](./cameraregionprovider/removeanchor%28_%29.md)
  Remove a camera region anchor.
- [func removeAnchor(forID: UUID) async throws](./cameraregionprovider/removeanchor%28forid%29.md)
  Remove an anchor with a given ID from camera region.
### Type Properties
- [static var isSupported: Bool](./cameraregionprovider/issupported.md)
  Determines whether this device supports the camera region provider.
- [static var requiredAuthorizations: [ARKitSession.AuthorizationType]](./cameraregionprovider/requiredauthorizations.md)
  The authorization type(s) required by the camera region provider.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [DataProvider](./dataprovider.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Camera region
- [struct CameraRegionAnchor](./cameraregionanchor.md)
  Represents a region in space for capturing a camera stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/cameraregionprovider)*
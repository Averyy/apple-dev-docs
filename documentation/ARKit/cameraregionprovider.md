# CameraRegionProvider

**Framework**: ARKit  
**Kind**: class

A camera region provider. An enterprise license is required to use the CameraRegionProvider. The provider will not deliver any data without it. The app must include the following entitlement: `com.apple.developer.arkit.camera-region.allow`

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
final class CameraRegionProvider
```

## Topics

### Structures
- [CameraRegionProvider.Error](cameraregionprovider/error.md)
  A camera region error.
### Initializers
- [init()](cameraregionprovider/init.md)
  Create a camera region provider.
### Instance Properties
- [var description: String](cameraregionprovider/description.md)
  A textual representation of this camera region provider.
- [var state: DataProviderState](cameraregionprovider/state.md)
  The state of this camera region provider.
### Instance Methods
- [func addAnchor(CameraRegionAnchor) async throws](cameraregionprovider/addanchor(_:).md)
  Add a camera region anchor.
- [func anchorUpdates(forID: UUID) -> AnchorUpdateSequence<CameraRegionAnchor>](cameraregionprovider/anchorupdates(forid:).md)
  An async sequence of anchor updates for a specific anchor.
- [func removeAnchor(CameraRegionAnchor) async throws](cameraregionprovider/removeanchor(_:).md)
  Remove a camera region anchor.
- [func removeAnchor(forID: UUID) async throws](cameraregionprovider/removeanchor(forid:).md)
  Remove an anchor with a given ID from camera region.
### Type Properties
- [static var isSupported: Bool](cameraregionprovider/issupported.md)
  Determines whether this device supports the camera region provider.
- [static var requiredAuthorizations: [ARKitSession.AuthorizationType]](cameraregionprovider/requiredauthorizations.md)
  The authorization type(s) required by the camera region provider.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [DataProvider](dataprovider.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/cameraregionprovider)*
# ObjectTrackingProvider

**Framework**: ARKit  
**Kind**: class

A source of real-time position of reference objects in a person’s environment.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
final class ObjectTrackingProvider
```

#### Overview

Use this class to configure ARKIt to track reference objects in a person’s environment and receive a stream of updates that contains [`ObjectAnchor`](objectanchor.md) structures that describe them.

## Topics

### Creating an object-tracking provider
- [init(referenceObjects: [ReferenceObject], trackingConfiguration: ObjectTrackingProvider.TrackingConfiguration?)](objecttrackingprovider/init(referenceobjects:trackingconfiguration:).md)
  Creates an object-tracking provider.
### Checking availability
- [static var isSupported: Bool](objecttrackingprovider/issupported.md)
  A Boolean value that indicates whether a device supports the object-tracking provider.
- [static var requiredAuthorizations: [ARKitSession.AuthorizationType]](objecttrackingprovider/requiredauthorizations.md)
  An array of authorization types the object-tracking provider requires.
### Configuring object-tracking
- [var trackingConfiguration: ObjectTrackingProvider.TrackingConfiguration](objecttrackingprovider/trackingconfiguration-swift.property.md)
  Returns the current parameters that are being used to configure object tracking.
- [ObjectTrackingProvider.TrackingConfiguration](objecttrackingprovider/trackingconfiguration-swift.struct.md)
  Parameters for changing object-tracking behavior.
### Inspecting an object-tracking provider
- [var state: DataProviderState](objecttrackingprovider/state.md)
  The state of an object-tracking provider.
- [var allAnchors: [ObjectAnchor]](objecttrackingprovider/allanchors.md)
  An array of all the object anchors the object-tracking provider is tracking.
- [var anchorUpdates: AnchorUpdateSequence<ObjectAnchor>](objecttrackingprovider/anchorupdates.md)
  An asynchronous sequence of anchors the framework updates.
- [ObjectTrackingProvider.Error](objecttrackingprovider/error.md)
  Values that represent an object-tracking error.
- [var description: String](objecttrackingprovider/description.md)
  A textual representation of this object tracking provider.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [DataProvider](dataprovider.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct ObjectAnchor](objectanchor.md)
  A reference object ARKit is tracking.
- [Exploring object tracking with ARKit](../visionOS/exploring_object_tracking_with_arkit.md)
  Find and track real-world objects in visionOS using reference objects trained with Create ML.
- [Implementing object tracking in your visionOS app](../visionOS/implementing-object-tracking-in-your-visionOS-app.md)
  Create engaging interactions by training models to recognize and track real-world objects in your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/objecttrackingprovider)*
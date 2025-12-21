# AccessoryTrackingProvider

**Framework**: ARKit  
**Kind**: class

Provides the real time position of accessories in the user’s environment.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
final class AccessoryTrackingProvider
```

## Topics

### Structures
- [AccessoryTrackingProvider.Error](accessorytrackingprovider/error.md)
  An accessory tracking error.
### Initializers
- [convenience init(accessories: [Accessory])](accessorytrackingprovider/init(accessories:).md)
  Create an accessory tracking provider.
### Instance Properties
- [var anchorUpdates: AnchorUpdateSequence<AccessoryAnchor>](accessorytrackingprovider/anchorupdates.md)
  An async sequence of all anchor updates.
- [var description: String](accessorytrackingprovider/description.md)
  A textual representation of this accessory tracking provider.
- [var latestAnchors: [AccessoryAnchor]](accessorytrackingprovider/latestanchors.md)
  The latest accessory anchors updated with the most recent inertial data.
- [var state: DataProviderState](accessorytrackingprovider/state.md)
  The state of this accessory tracking provider.
### Instance Methods
- [func predictAnchor(for: AccessoryAnchor, at: TimeInterval) -> AccessoryAnchor?](accessorytrackingprovider/predictanchor(for:at:).md)
  Predict an accessory anchor to a target timestamp.
### Type Properties
- [static var isSupported: Bool](accessorytrackingprovider/issupported.md)
  Determines whether this device supports the accessory tracking provider.
- [static var requiredAuthorizations: [ARKitSession.AuthorizationType]](accessorytrackingprovider/requiredauthorizations.md)
  The authorization type(s) required by the accessory tracking provider.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [DataProvider](dataprovider.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct Accessory](accessory.md)
  Represents an accessory to be tracked.
- [struct AccessoryAnchor](accessoryanchor.md)
  Represents a tracked accessory.
- [Tracking accessories in volumetric windows](tracking-accessories-in-volumetric-windows.md)
  Translate the position and velocity of tracked handheld accessories to throw virtual balls at a stack of cans.
- [Tracking a handheld accessory as a virtual sculpting tool](tracking-a-handheld-accessory-as-a-virtual-sculpting-tool.md)
  Use a tracked accessory with Apple Vision Pro to create a virtual sculpture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/accessorytrackingprovider)*
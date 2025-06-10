# AccessoryTrackingProvider

**Framework**: ARKit  
**Kind**: class

Provides the real time position of accessories in the user’s environment.

**Availability**:
- visionOS 26.0+ (Beta)

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
  Get the latest accessory anchors seen by the provider. These could be used for `predictAnchor` The output array may be empty if the provider is not running or no accessory is tracked at the moment.
- [var state: DataProviderState](accessorytrackingprovider/state.md)
  The state of this accessory tracking provider.
### Instance Methods
- [func predictAnchor(for: AccessoryAnchor, at: TimeInterval) -> AccessoryAnchor?](accessorytrackingprovider/predictanchor(for:at:).md)
  Get an `AccessoryAnchor` for a given time and accessory.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/accessorytrackingprovider)*
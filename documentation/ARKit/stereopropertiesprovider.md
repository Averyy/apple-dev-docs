# StereoPropertiesProvider

**Framework**: ARKit  
**Kind**: class

The StereoPropertiesProvider serves the latest viewpoint properties on the device.

**Availability**:
- visionOS 2.4+

## Declaration

```swift
final class StereoPropertiesProvider
```

## Topics

### Initializers
- [init()](stereopropertiesprovider/init.md)
  Initialize the StereoPropertiesProvider.
### Instance Properties
- [var description: String](stereopropertiesprovider/description.md)
  A textual representation of this stereo properties provider.
- [var latestViewpointProperties: ViewpointProperties?](stereopropertiesprovider/latestviewpointproperties.md)
  Returns the latest viewpoint properties, if available.
- [var state: DataProviderState](stereopropertiesprovider/state.md)
  The state of this stereo properties provider.
### Type Properties
- [static var isSupported: Bool](stereopropertiesprovider/issupported.md)
  Determines whether this device supports the stereo properties provider.
- [static var requiredAuthorizations: [ARKitSession.AuthorizationType]](stereopropertiesprovider/requiredauthorizations.md)
  The authorization type(s) required by the stereo properties provider.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [DataProvider](dataprovider.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/stereopropertiesprovider)*
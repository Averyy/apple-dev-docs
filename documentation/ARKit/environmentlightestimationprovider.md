# EnvironmentLightEstimationProvider

**Framework**: ARKit  
**Kind**: class

A source of live data about lighting information in the environment.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
final class EnvironmentLightEstimationProvider
```

#### Overview

Use the anchor this provider returns to reflect lighting from a person’s surroundings on the surfaces of virtual objects.

## Topics

### Creating an environment light estimation provider
- [convenience init()](environmentlightestimationprovider/init.md)
  Creates an environment light estimation provider.
### Inspecting the environment light estimation provider
- [var anchorUpdates: AnchorUpdateSequence<EnvironmentProbeAnchor>](environmentlightestimationprovider/anchorupdates.md)
  An asynchronous sequence of all anchor updates.
- [var description: String](environmentlightestimationprovider/description.md)
  A textual representation of this environment light estimation provider.
- [var state: DataProviderState](environmentlightestimationprovider/state.md)
  The state of an environment light estimation provider.
### Type properties
- [static var isSupported: Bool](environmentlightestimationprovider/issupported.md)
  A Boolean value that indicates whether a device supports the environment light estimation provider.
- [static var requiredAuthorizations: [ARKitSession.AuthorizationType]](environmentlightestimationprovider/requiredauthorizations.md)
  The authorization types that an environment light estimation provider requires.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [DataProvider](dataprovider.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct EnvironmentProbeAnchor](environmentprobeanchor.md)
  An environment probe in the world.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/environmentlightestimationprovider)*
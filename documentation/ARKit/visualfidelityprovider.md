# VisualFidelityProvider

**Framework**: ARKit  
**Kind**: class

A data provider that delivers visual fidelity monitoring data.

**Availability**:
- visionOS 27.0+ (Beta)

## Declaration

```swift
final class VisualFidelityProvider
```

## Topics

### Structures
- [VisualFidelityProvider.FieldOfView](visualfidelityprovider/fieldofview.md)
  A field of view (FoV) specification.
### Initializers
- [convenience init(fieldOfView: VisualFidelityProvider.FieldOfView?, requestDeviceFitUpdates: Bool, presentCoachingAlerts: Bool)](visualfidelityprovider/init(fieldofview:requestdevicefitupdates:presentcoachingalerts:).md)
  Create a visual fidelity data provider.
### Instance Properties
- [var anchorUpdates: AnchorUpdateSequence<FieldOfViewAnchor>](visualfidelityprovider/anchorupdates.md)
  An async sequence of anchor updates for visualizing a preset field of view (FoV).
- [var description: String](visualfidelityprovider/description.md)
  A textual representation of this visual fidelity data provider.
- [var fidelityDataUpdates: some AsyncSequence<VisualFidelityData, Never>](visualfidelityprovider/fidelitydataupdates.md)
  An async sequence of visual fidelity data updates.
- [var state: DataProviderState](visualfidelityprovider/state.md)
  The state of this visual fidelity data provider.
### Type Properties
- [static var isSupported: Bool](visualfidelityprovider/issupported.md)
  Determines whether this device supports the visual fidelity data provider.
- [static var requiredAuthorizations: [ARKitSession.AuthorizationType]](visualfidelityprovider/requiredauthorizations.md)
  The authorization type(s) required by the visual fidelity data provider.

## Relationships

### Conforms To
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [DataProvider](dataprovider.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct VisualFidelityData](visualfidelitydata.md)
  Visual fidelity data containing device fit and field of view verification.
- [struct FieldOfViewAnchor](fieldofviewanchor.md)
  An anchor representing a set of field of view (FoV) boundary polygon points in immersive space.
- [enum DeviceFitStatus](devicefitstatus.md)
  Device fit validation status indicating the user’s eye position relative to the optimal device fit range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/visualfidelityprovider)*
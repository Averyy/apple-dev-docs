# WorldTrackingProvider.Error

**Framework**: ARKit  
**Kind**: struct  
**Role**: Structure

An error that can occur during a world-tracking session.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
struct Error
```

## Topics

### Inspecting world-tracking errors
- [let anchor: WorldAnchor?](./error/anchor.md)
  The anchor that caused a world-tracking error.
- [var code: WorldTrackingProvider.Error.Code](./error/code-swift.property.md)
  The error code.
- [WorldTrackingProvider.Error.Code](./error/code-swift.enum.md)
  The error codes for errors that world tracking providers throw.
- [var errorDescription: String?](./error/errordescription.md)
  A localized message that describes the error that occurred.
### Providing recovery suggestions
- [var recoverySuggestion: String?](./error/recoverysuggestion.md)
  A localized message that describes how someone might recover from the error.
- [var failureReason: String?](./error/failurereason.md)
  A localized message that describes why the error occurred.
### Instance Properties
- [var description: String](./error/description.md)
  A textual description of the error that occurred.

## Relationships

### Conforms To
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Error](../../Swift/error.md)
- [LocalizedError](../../Foundation/localizederror.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Tracking objects
- [init()](./init%28%29.md)
  Creates a world-tracking provider.
- [var anchorUpdates: AnchorUpdateSequence<WorldAnchor>](./anchorupdates.md)
  A sequence of updates to anchors a provider tracks.
- [static var requiredAuthorizations: [ARKitSession.AuthorizationType]](./requiredauthorizations.md)
  The types of authorizations necessary for tracking world anchors.
- [static var isSupported: Bool](./issupported.md)
  A Boolean value that indicates whether the current runtime environment supports world-tracking providers.
- [var allAnchors: [WorldAnchor]?](./allanchors.md)
  An array of all known world anchors from the world-tracking provider.
- [func addAnchor(WorldAnchor) async throws](./addanchor%28_%29.md)
  Adds a world anchor you supply to the set of currently tracked anchors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/worldtrackingprovider/error)*
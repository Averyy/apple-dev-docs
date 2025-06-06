# WorldTrackingProvider.Error

**Framework**: ARKit  
**Kind**: struct

An error that can occur during a world-tracking session.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
struct Error
```

## Topics

### Inspecting world-tracking errors
- [let anchor: WorldAnchor?](worldtrackingprovider/error/anchor.md)
  The anchor that caused a world-tracking error.
- [var code: WorldTrackingProvider.Error.Code](worldtrackingprovider/error/code-swift.property.md)
  The error code.
- [WorldTrackingProvider.Error.Code](worldtrackingprovider/error/code-swift.enum.md)
  The error codes for errors that world tracking providers throw.
- [var errorDescription: String?](worldtrackingprovider/error/errordescription.md)
  A localized message that describes the error that occurred.
### Providing recovery suggestions
- [var recoverySuggestion: String?](worldtrackingprovider/error/recoverysuggestion.md)
  A localized message that describes how someone might recover from the error.
- [var failureReason: String?](worldtrackingprovider/error/failurereason.md)
  A localized message that describes why the error occurred.
### Instance Properties
- [var description: String](worldtrackingprovider/error/description.md)
  A textual description of the error that occurred.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Error](../Swift/Error.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [init()](worldtrackingprovider/init.md)
  Creates a world-tracking provider.
- [var anchorUpdates: AnchorUpdateSequence<WorldAnchor>](worldtrackingprovider/anchorupdates.md)
  A sequence of updates to anchors a provider tracks.
- [static var requiredAuthorizations: [ARKitSession.AuthorizationType]](worldtrackingprovider/requiredauthorizations.md)
  The types of authorizations necessary for tracking world anchors.
- [static var isSupported: Bool](worldtrackingprovider/issupported.md)
  A Boolean value that indicates whether the current runtime environment supports world-tracking providers.
- [var allAnchors: [WorldAnchor]?](worldtrackingprovider/allanchors.md)
  An array of all known world anchors from the world-tracking provider.
- [func addAnchor(WorldAnchor) async throws](worldtrackingprovider/addanchor(_:).md)
  Adds a world anchor you supply to the set of currently tracked anchors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/worldtrackingprovider/error)*
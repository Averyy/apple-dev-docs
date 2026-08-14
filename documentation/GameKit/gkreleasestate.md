# GKReleaseState

**Framework**: GameKit  
**Kind**: struct

Describes the release state of an App Store Connect resource, such as an Achievement or Leaderboard.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
struct GKReleaseState
```

## Topics

### Initializers
- [init(rawValue: UInt)](gkreleasestate/init(rawvalue:).md)
### Type Properties
- [static var prereleased: GKReleaseState](gkreleasestate/prereleased.md)
  The resource has been created in App Store Connect but isn’t yet associated with a released version of an App.
- [static var released: GKReleaseState](gkreleasestate/released.md)
  The resource is associated with a release in App Store Connect. This has no relationship with the “archived” state of a resource (i.e., A resource can be release *and* archived).

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)

## See Also

- [var releaseState: GKReleaseState](gkchallengedefinition/releasestate.md)
  The release state of the challenge definition in App Store Connect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkreleasestate)*
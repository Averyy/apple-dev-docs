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
  The resource is associated with a release in App Store Connect. This has no relationship with the “archived” state of a resource (i.e., A resource can be release  archived).

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkreleasestate)*
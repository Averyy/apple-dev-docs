# GKReleaseState

**Framework**: GameKit  
**Kind**: struct  
**Role**: Structure

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

```c
enum GKReleaseState : NSUInteger;
```

## Topics

### Initializers
- [init(rawValue: UInt)](./gkreleasestate/init%28rawvalue%29.md)
### Type Properties
- [static var prereleased: GKReleaseState](./gkreleasestate/prereleased.md)
  The resource has been created in App Store Connect but isn’t yet associated with a released version of an App.
- [static var released: GKReleaseState](./gkreleasestate/released.md)
  The resource is associated with a release in App Store Connect. This has no relationship with the “archived” state of a resource (i.e., A resource can be release *and* archived).

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Getting the release state
- [var releaseState: GKReleaseState](./gkchallengedefinition/releasestate.md)
  The release state of the challenge definition in App Store Connect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkreleasestate)*
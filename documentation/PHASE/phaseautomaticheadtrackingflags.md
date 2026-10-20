# PHASEAutomaticHeadTrackingFlags

**Framework**: PHASE  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 26.0+

## Declaration

```swift
struct PHASEAutomaticHeadTrackingFlags
```

```c
enum PHASEAutomaticHeadTrackingFlags : NSUInteger;
```

#### Overview

Automatic Head-Tracking flags.

```
On capable devices, listener orientation will be automatically rotated based on user's head-orientation.
```

```
On capable devices, listener position will be automatically set based on user's position.
```

## Topics

### Initializers
- [init(rawValue: UInt)](./phaseautomaticheadtrackingflags/init%28rawvalue%29.md)
### Type Properties
- [static var orientation: PHASEAutomaticHeadTrackingFlags](./phaseautomaticheadtrackingflags/orientation.md)
- [static var position: PHASEAutomaticHeadTrackingFlags](./phaseautomaticheadtrackingflags/position.md)

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseautomaticheadtrackingflags)*
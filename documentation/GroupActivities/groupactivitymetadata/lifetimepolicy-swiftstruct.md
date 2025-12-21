# GroupActivityMetadata.LifetimePolicy

**Framework**: Group Activities  
**Kind**: struct

An activity lifetime policy used by a Group Activity.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
struct LifetimePolicy
```

#### Overview

Activities that share content owned by the initiator may wish to customize their lifetime policy so that the activity ends when the initiator leaves.

## Topics

### Type Properties
- [static let automatic: GroupActivityMetadata.LifetimePolicy](groupactivitymetadata/lifetimepolicy-swift.struct/automatic.md)
  The default lifetime policy for a group activity.
- [static let endsWhenInitiatorLeaves: GroupActivityMetadata.LifetimePolicy](groupactivitymetadata/lifetimepolicy-swift.struct/endswheninitiatorleaves.md)
  The activity should end when the initiator of the activity leaves.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupactivitymetadata/lifetimepolicy-swift.struct)*
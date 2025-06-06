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

### Operators
- [static func == (GroupActivityMetadata.LifetimePolicy, GroupActivityMetadata.LifetimePolicy) -> Bool](groupactivitymetadata/lifetimepolicy-swift.struct/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](groupactivitymetadata/lifetimepolicy-swift.struct/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](groupactivitymetadata/lifetimepolicy-swift.struct/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Properties
- [static let automatic: GroupActivityMetadata.LifetimePolicy](groupactivitymetadata/lifetimepolicy-swift.struct/automatic.md)
  The default lifetime policy for a group activity.
- [static let endsWhenInitiatorLeaves: GroupActivityMetadata.LifetimePolicy](groupactivitymetadata/lifetimepolicy-swift.struct/endswheninitiatorleaves.md)
  The activity should end when the initiator of the activity leaves.
### Default Implementations
- [Equatable Implementations](groupactivitymetadata/lifetimepolicy-swift.struct/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupactivitymetadata/lifetimepolicy-swift.struct)*
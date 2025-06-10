# endsWhenInitiatorLeaves

**Framework**: Group Activities  
**Kind**: property

The activity should end when the initiator of the activity leaves.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
static let endsWhenInitiatorLeaves: GroupActivityMetadata.LifetimePolicy
```

#### Discussion

This case should be used in the rare instances where the initiator of the activity owns what is being shared; for example, activities that share photos or slides that exclusively belong to the initiator of the activity would use this so that when they leave the group session, the content will no longer be shared.

> ❗ **Important**: The majority of SharePlay apps should use the [`automatic`](groupactivitymetadata/lifetimepolicy-swift.struct/automatic.md) policy, instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupactivitymetadata/lifetimepolicy-swift.struct/endswheninitiatorleaves)*
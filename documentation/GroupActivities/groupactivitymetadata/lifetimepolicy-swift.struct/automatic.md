# automatic

**Framework**: Group Activities  
**Kind**: property

The default lifetime policy for a group activity.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
static let automatic: GroupActivityMetadata.LifetimePolicy
```

#### Discussion

Initiators and participants will have the option to leave the activity independently or end it for everyone.  When everyone has left the activity, it will end.

This case should be used by most apps and allows activities to continue until all participants leave the activity – regardless of which participant happens to have initiated the activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupactivitymetadata/lifetimepolicy-swift.struct/automatic)*
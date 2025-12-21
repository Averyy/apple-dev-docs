# primary(_:)

**Framework**: Group Activities  
**Kind**: method

A primary association with a SharePlay group activity that is identified by a given string value.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
static func primary(_ identifier: String) -> GroupActivityAssociationKind
```

#### Discussion

When in an active SharePlay activity, the system will annotate the primary associated scene scene as “shared” and use it as the common scene to arrange spatial Personas around. This association between the group activity and a scene in your app creates a shared space for spatial Personas to interact in.

> ❗ **Important**: The identifier provided must match the identifier used for the primary association across all participants in the group activity.

You should pick an identifier that reflects the content of this view. For example: `"in-game"`, `"score-board"`, or `"solar-system-photo.png"`. Synchronizing the identifier used across all participants in the activity allows FaceTime to synchronize the position of the containing scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupactivityassociationkind/primary(_:))*
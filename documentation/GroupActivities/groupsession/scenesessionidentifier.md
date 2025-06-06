# sceneSessionIdentifier

**Framework**: Group Activities  
**Kind**: property

The persistent identifier of the session’s associated scene.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
final var sceneSessionIdentifier: String? { get }
```

#### Discussion

Use this property to determine which of your app’s scenes belongs with this session. You can configure a [`GroupActivity`](groupactivity.md) object with a [`SceneAssociationBehavior`](sceneassociationbehavior.md) type that tells the system how to associate the activity with one of your app’s scenes. After matching the activity to a specific scene, the system places the scene identifier in this property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupsession/scenesessionidentifier)*
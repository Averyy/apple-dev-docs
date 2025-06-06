# none

**Framework**: Group Activities  
**Kind**: property

A behavior that doesn’t match any scenes to the activity.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
static let none: SceneAssociationBehavior
```

## Mentions

- [Adding spatial Persona support to an activity](adding-spatial-persona-support-to-an-activity.md)

#### Discussion

Choose this option when you don’t want the system to associate one of your scenes with the SharePlay activity. You might choose this option when you handle an activity separately from your app’s scenes.

## See Also

- [static let `default`: SceneAssociationBehavior](sceneassociationbehavior/default.md)
  A behavior that matches the activity to a scene using the identifier of your activity object.
- [static func content(String) -> SceneAssociationBehavior](sceneassociationbehavior/content(_:).md)
  A behavior that matches the activity to a scene using a custom string that you supply.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/sceneassociationbehavior/none)*
# default

**Framework**: Group Activities  
**Kind**: property

A behavior that matches the activity to a scene using the identifier of your activity object.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
static let `default`: SceneAssociationBehavior
```

## Mentions

- [Adding spatial Persona support to an activity](adding-spatial-persona-support-to-an-activity.md)

#### Discussion

With this option, the system uses the string in the [`activityIdentifier`](groupactivity/activityidentifier.md) property of your [`GroupActivity`](groupactivity.md) object to locate an appropriate scene. Choose this option if your app has only one scene, or if you always use the same scene to display the intended activity.

## See Also

- [static func content(String) -> SceneAssociationBehavior](sceneassociationbehavior/content(_:).md)
  A behavior that matches the activity to a scene using a custom string that you supply.
- [static let none: SceneAssociationBehavior](sceneassociationbehavior/none.md)
  A behavior that doesn’t match any scenes to the activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/sceneassociationbehavior/default)*
# content(_:)

**Framework**: Group Activities  
**Kind**: method

A behavior that matches the activity to a scene using a custom string that you supply.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
static func content(_ contentIdentifier: String) -> SceneAssociationBehavior
```

## Mentions

- [Adding spatial Persona support to an activity](adding-spatial-persona-support-to-an-activity.md)

#### Return Value

A [`SceneAssociationBehavior`](sceneassociationbehavior.md) type with the specified identifier.

#### Discussion

Use this option when you want more control over the scene-selection process for your [`GroupActivity`](groupactivity.md) object. You might use it to direct the activity to different scenes, or to direct the activity to a specific instance of a scene. For example, a drawing app might direct the activity to the specific canvas someone wants to share, and not to a new or unrelated canvas that uses the same scene type.

## Parameters

- `contentIdentifier`: The string to compare against the scene’s defined   activation conditions. This string has a similar purpose to the     of an   object.

## See Also

- [static let `default`: SceneAssociationBehavior](sceneassociationbehavior/default.md)
  A behavior that matches the activity to a scene using the identifier of your activity object.
- [static let none: SceneAssociationBehavior](sceneassociationbehavior/none.md)
  A behavior that doesn’t match any scenes to the activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/sceneassociationbehavior/content(_:))*
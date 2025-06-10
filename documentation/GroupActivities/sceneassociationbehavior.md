# SceneAssociationBehavior

**Framework**: Group Activities  
**Kind**: struct

A type that tells the system which scene to associate with an incoming group activity.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
struct SceneAssociationBehavior
```

#### Overview

Use a [`SceneAssociationBehavior`](sceneassociationbehavior.md) type to match SharePlay activities to your app’s scenes. The static accessors of this type offer different scene-selection behaviors. For example, you can match each activity type to a specific scene, match scenes dynamically based on the contents of the activity, or prevent matching altogether. Select one of these behaviors and assign the related type to your [`GroupActivity`](groupactivity.md) object’s metadata. On some platforms, the system adds a custom indicator to a scene to let people know that SharePlay is active.

Add activation conditions to your SwiftUI or UIKit scenes to tell the system which activities they support. An activation condition is a custom string that identifies one of your app’s supported activities. You add these strings to your scenes to direct different types of external events to them. In SwiftUI, specify the activation conditions for a scene using the [`handlesExternalEvents(matching:)`](https://developer.apple.com/documentation/SwiftUI/Scene/handlesExternalEvents(matching:)) modifier. In the following example, the scene handles two app-related activities, including a group activity.

```swift
let activationConditions : Set = ["com.mycompany.MySharePlayActivity",
                                  "com.mycompany.MyUserActivity"]
var body: some Scene {
   WindowGroup {
      ContentView()
   }
   .handlesExternalEvents(matching: activationConditions)
```

To handle the same activation condition in a UIKit app, add rules to the [`activationConditions`](https://developer.apple.com/documentation/UIKit/UIScene/activationConditions) property of your [`UIScene`](https://developer.apple.com/documentation/UIKit/UIScene) object. Assign these rules in the [`scene(_:willConnectTo:options:)`](https://developer.apple.com/documentation/UIKit/UISceneDelegate/scene(_:willConnectTo:options:)) method when you first configure your scene for use. Use the [`prefersToActivateForTargetContentIdentifierPredicate`](https://developer.apple.com/documentation/UIKit/UISceneActivationConditions/prefersToActivateForTargetContentIdentifierPredicate) property when the scene is the preferred choice for handling the action. The following example shows how to configure a scene to handle two app-related activities, including a group activity.

```swift
let activationConditions = ["com.example.MySharePlayActivity", "com.example.MyUserActivity"]
func scene(_ scene: UIScene,
           willConnectTo session: UISceneSession,
           options connectionOptions: UIScene.ConnectionOptions) {
   // Specify the activities that this scene prefers to handle.
   scene.activationConditions.prefersToActivateForTargetContentIdentifierPredicate
        = NSPredicate(format: "self in %@", activationConditions)
}
```

## Topics

### Getting the scene-association options
- [static let `default`: SceneAssociationBehavior](sceneassociationbehavior/default.md)
  A behavior that matches the activity to a scene using the identifier of your activity object.
- [static func content(String) -> SceneAssociationBehavior](sceneassociationbehavior/content(_:).md)
  A behavior that matches the activity to a scene using a custom string that you supply.
- [static let none: SceneAssociationBehavior](sceneassociationbehavior/none.md)
  A behavior that doesn’t match any scenes to the activity.
### Operators
- [static func == (SceneAssociationBehavior, SceneAssociationBehavior) -> Bool](sceneassociationbehavior/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Default Implementations
- [Equatable Implementations](sceneassociationbehavior/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var sceneAssociationBehavior: SceneAssociationBehavior](groupactivitymetadata/sceneassociationbehavior.md)
  Criteria the system uses to direct an activity to a specific scene of your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/sceneassociationbehavior)*
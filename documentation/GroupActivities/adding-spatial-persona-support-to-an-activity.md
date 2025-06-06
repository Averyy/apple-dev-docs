# Adding spatial Persona support to an activity

**Framework**: Group Activities

Update your SharePlay activities to support spatial Personas and the shared context when running in visionOS.

#### Overview

A person who participates in SharePlay activities on Apple Vision Pro has the option to participate using their spatial Persona. The system arranges spatial Personas around the activity content, giving each person a clear view of the content and each other. Each person sees the facial expressions of other participants, what they’re looking at, and where they’re pointing. This experience creates the feeling that they’re in the same physical space interacting with shared content and each other.

To maintain the experience when spatial Personas are visible, apps share additional information to maintain the  for the activity. Because participants can see where others are looking, your app’s content must look the same for everyone. Share any additional information you need to keep everyone’s content in sync visually. For example, synchronize your window’s scroll position to ensure everyone sees the same portion of that window.

You don’t need to define new [`GroupActivity`](groupactivity.md) types specifically to support spatial Personas. The system automatically displays spatial Personas for existing activities that take place in a window or volume. However, if you support activities in a Full Space, you need to do additional work to support spatial Personas for your experience. For information about how to define activities in your app, see [`Defining your app’s SharePlay activities`](defining-your-apps-shareplay-activities.md).

##### Associate Shareplay Activities with Your Apps Scenes

You use scenes to manage the content for your app’s windows, volumes, and immersive spaces. You also use scenes to display any activity-related content. When a participant joins an activity, the system selects or opens the scene that supports the activity. If your app has only one scene and one window, the system has only one choice. However, if your app has multiple scenes, you need to help the system choose the correct one.

For each of your app’s scenes, activation conditions tell the system how to handle your app’s SharePlay activities. You also use activation conditions to specify how to handle [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) objects, and other incoming events. To specify activation conditions for one of your scenes:

- For SwiftUI, add the [`handlesExternalEvents(preferring:allowing:)`](https://developer.apple.com/documentation/SwiftUI/View/handlesExternalEvents(preferring:allowing:)) modifier to your scene type.
- For UIKit, configure the scene’s [`activationConditions`](https://developer.apple.com/documentation/UIKit/UIScene/activationConditions) property in the [`scene(_:willConnectTo:options:)`](https://developer.apple.com/documentation/UIKit/UISceneDelegate/scene(_:willConnectTo:options:)) method of your scene delegate.

When you add an activation condition to a scene, you specify a string that uniquely identifies your SharePlay activity. The string can be anything you want, as long as it creates a unique connection between the activity and the specific scene. When there is a one-to-one correspondence between an activity and scene, the string in the [`activityIdentifier`](groupactivity/activityidentifier.md) property of your activity object is a good choice. When there isn’t a one-to-one correspondence between scene and activity, you must create a string that uniquely identifies the scene. For example, in a document-based app, you might specify the name of a document to direct the system to the scene that contains the document.

The following code defines a SwiftUI scene for a window, and associates two activities with that window. Because the app uses the same scene to display content for two different activities, the activation conditions contain the identifiers for the two [`GroupActivity`](groupactivity.md) types. When either activity starts, the system directs the activity to the window containing the scene. If no such window is open, the system launches the app and creates the window as needed.

```swift
let activationConditions : Set = ["com.mycompany.MySharePlayActivity",
                                  "com.mycompany.MyUserActivity"]
var body: some Scene {
    WindowGroup {
        ContentView()
            .handlesExternalEvents(preferring: [], allowing: activationConditions)
    }
```

In addition to configuring your scene, you need to update your activity object’s metadata with the appropriate string. Specify the string using the [`sceneAssociationBehavior`](groupactivitymetadata/sceneassociationbehavior.md) property of your activity object’s [`GroupActivityMetadata`](groupactivitymetadata.md) structure. Assign the [`default`](sceneassociationbehavior/default.md) value to this property if you use the activity identifier as the string. For any custom strings, assign the [`content(_:)`](sceneassociationbehavior/content(_:).md) value and specify your string. To disable scene association for the activity and handle the presentation of activity-related UI yourself, specify the [`none`](sceneassociationbehavior/none.md) value.

##### Configure Your Apps Support for Spatial Personas

The system provides some default behaviors to make it easier for you to adopt spatial Personas in your app. For activities that take place in a window or volume, the system chooses a default arrangement of the spatial Personas around your scene. The system also adorns the scene with a Share menu, which provides a visual indication when sharing is active and contains controls to start activities. The system doesn’t display spatial Personas in a Full Space by default.

To change the default behavior of your app, update the [`SystemCoordinator`](systemcoordinator.md) of your [`GroupSession`](groupsession.md) before you call the session’s [`join()`](groupsession/join().md) method. Use the [`SystemCoordinator`](systemcoordinator.md) to:

- Specify a different arrangement for spatial Personas.
- Specify whether your app supports spatial Personas when a Full Space is visible.

The following example changes the arrangement of spatial Personas to be side by side facing the app’s content. The code also tells the system that the app supports spatial Personas when a Full Space is open.

```swift
if let coordinator = await newSession.systemCoordinator {
    var config = SystemCoordinator.Configuration()
    config.spatialTemplatePreference = .sideBySide.contentExtent(200)
    config.supportsGroupImmersiveSpace = true
    coordinator.configuration = config
}

// Join the session.
newSession.join()
```

Spatial template preferences tell the system whether to arrange participants side by side, in a circle, or in an arrangement that supports conversation. For each template, the system uses the size of your content to determine how far away to place spatial Personas. For example, the system moves them farther away when your content is larger, and brings them closer together when your content is small. To override this distance, add the [`contentExtent(_:)`](spatialtemplatepreference/contentextent(_:).md) modifier to your template preference. That modifier tells the system to use the distance you specify, instead of the content size.

If you enable support for spatial Personas in a Full Space, you must do additional work to support that experience. When an activity moves to a Full Space, the system creates a shared coordinate system for all participants and the content. In this new coordinate system, participants are no longer at the center of the coordinate system, which might require you to update the position of your content. For more information, see [`Place content relative to a participant in an immersive space`](adding-spatial-persona-support-to-an-activity#Place-content-relative-to-a-participant-in-an-immersive-space.md).

##### Synchronize Additional Data When Spatial Personas Are Visible

When spatial Personas are visible, it’s your responsibility to maintain the shared context for your activity. The shared context includes both the content you display and how that content appears to each participant. People can gesture or look at content using their spatial Persona, so it’s important that everyone sees the same thing when that happens. For example, Freeform synchronizes both the page content and the current scroll position to ensure everyone sees the same portion of the page.

When defining an activity, define additional data messages to synchronize any information you need to maintain the shared context. When the current participant shows their spatial Persona, send the extra messages when the participant makes relevant changes to the activity. For example, send them when the person scrolls the activity window. Similarly, receive those messages and incorporate the results into your app when the spatial Persona is visible.

> **Note**: Make sure you separate the messages that all participants require from the ones that only make sense when spatial Personas are visible. Maintaining the shared context is necessary when spatial Personas are visible, but isn’t always necessary at other times. For example, Freeform doesn’t synchronize the scroll position for someone without a spatial Persona.

Make sure you separate the messages that all participants require from the ones that only make sense when spatial Personas are visible. Maintaining the shared context is necessary when spatial Personas are visible, but isn’t always necessary at other times. For example, Freeform doesn’t synchronize the scroll position for someone without a spatial Persona.

To determine when someone’s spatial Persona is visible, monitor the [`localParticipantStates`](systemcoordinator/localparticipantstates.md) of your session’s [`SystemCoordinator`](systemcoordinator.md) object. The [`AsyncSequence`](https://developer.apple.com/documentation/Swift/AsyncSequence) in this property reports participant-related state changes, including changes to the visibility of their spatial Persona. Get the [`isSpatial`](systemcoordinator/participantstate/isspatial.md) property of the returned [`SystemCoordinator.ParticipantState`](systemcoordinator/participantstate.md) structure and use it to configure your app’s behavior. The following example uses a task to update the game state to accommodate spatial Personas. When the current participant is spatial, the game sends additional messages to maintain the shared context.

```swift
Task.detached { @MainActor in
    for await state in coordinator.localParticipantStates {
        if state.isSpatial {
            // Synchronize additional data for the shared context.
            gameModel.isSpatial = true
        } else {
            // Don't synchronize additional data.
            gameModel.isSpatial = false
        }
    }
}
```

##### Update the Immersion Level Automatically for a Full Space

If one participant opens an immersive space as part of an activity, the system doesn’t automatically open the same immersive space for other participants. Making a transition to an immersive space is a significant change, and some participants might not want to make the transition right away. For example, if a participant is on a phone call, they might not want another app to open an immersive space and hide their call. Instead, the system reports when transitions to immersive spaces occur, and lets you decide when to transition other participants automatically.

To determine when any participant transitions to an immersive space, monitor the [`groupImmersionStyle`](systemcoordinator/groupimmersionstyle.md) property of your [`SystemCoordinator`](systemcoordinator.md) object. This property contains an [`AsyncSequence`](https://developer.apple.com/documentation/Swift/AsyncSequence) that reports the most recent immersion style that a participant adopts. When a participant presents an immersive space, or when they change the immersion style of the current space, the system updates the sequence with the new value. The following example shows a task that opens the immersive space with the same style as the group immersion style.

```swift
Task.detached {
    for await immersionStyle in systemCoordinator.groupImmersionStyle {
        if let immersionStyle {
            // Open an immersive space with the same style.
        }
        else {
            // Dismiss the immersive space.
        }
    }
}
```

The system reports `nil` for the immersion style when a participant dismisses their open immersive space. Use that option to dismiss the space for other participants and return to a window or volume.

> **Note**: If a participant presses the Digital Crown while an immersive space is open, the system dismisses the space without notifying the rest of the group. Someone might use this feature to temporarily leave the activity and perform another task. After they perform that task, they can use the system-provided UI to rejoin the activity and return to the group immersive space.

If a participant presses the Digital Crown while an immersive space is open, the system dismisses the space without notifying the rest of the group. Someone might use this feature to temporarily leave the activity and perform another task. After they perform that task, they can use the system-provided UI to rejoin the activity and return to the group immersive space.

##### Place Content Relative to a Participant in an Immersive Space

When an activity takes place in an immersive space, the system creates a shared coordinate system for the participants and content. In this new coordinate space, the origin of the coordinate space is not the same as the origin of any of the participants. If an activity-related window or volume is visible, the system places the window or volume at the new origin. If the activity doesn’t use a window or volume, the system arranges the participants in a circle and sets the origin of the coordinate space to the circle’s center. The following figure shows the origin of the shared coordinate system for a window, volume, and immersive space relative to several spatial Personas.

If you place content directly into your immersive space, you must adjust the position of that content to account for the modified coordinate space. To do that, you first determine the person’s location in the new coordinate system. Read the person’s location in the scene using a [`GeometryProxy3D`](https://developer.apple.com/documentation/SwiftUI/GeometryProxy3D). The proxy for this reader contains a doc://com.apple.documentation/documentation/swiftui/geometryproxy3d/immersivespacedisplacement(in:) method, which you can use to locate the origin of the shared coordinate space. Call the method using the [`global`](https://developer.apple.com/documentation/SwiftUI/CoordinateSpaceProtocol/global) value as a parameter to get the displacement of the coordinate space’s origin, relative to the person’s location. Invert that displacement value to get the location of the participant relative in the new coordinate space. The following example shows how to use a [`GeometryProxy3D`](https://developer.apple.com/documentation/SwiftUI/GeometryProxy3D) to get the offset to the current participant and use that information to place a custom view:

```swift
var body: some Scene {
    ImmersiveSpace(id:"earth") {
        GeometryReader3D { proxy in
            let displacement = 
                proxy.immersiveSpaceDisplacement(in: .global).inverse
                
            CustomView()
                .offset(displacement.position)
                .rotation3DEffect(displacement.rotation)
        }
    }
}
```

The displacement between a person and the origin of the scene doesn’t change during the course of your activity even when the participant moves. The system sets the origin of an immersive space when you first present it, and updates it only once when changing it to a shared coordinate space.

## See Also

- [class SystemCoordinator](systemcoordinator.md)
  A type you use to coordinate your interface’s behavior when an active SharePlay session supports spatial placement of content.
- [SystemCoordinator.ParticipantState](systemcoordinator/participantstate.md)
  A structure that tells you whether a participant supports a shared simulation space for the current activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/adding-spatial-persona-support-to-an-activity)*
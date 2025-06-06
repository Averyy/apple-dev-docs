# requestSceneSessionDestruction(_:options:errorHandler:)

**Framework**: UIKit  
**Kind**: method

Asks the system to dismiss an existing scene and remove it from the app switcher.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func requestSceneSessionDestruction(_ sceneSession: UISceneSession, options: UISceneDestructionRequestOptions?, errorHandler: ((any Error) -> Void)? = nil)
```

#### Discussion

If the specified scene is onscreen, calling this method dismisses it using the specified options. The method sends a disconnect notification to the scene and then calls your app delegate’s [`application(_:didDiscardSceneSessions:)`](uiapplicationdelegate/application(_:diddiscardscenesessions:).md) method.

## Parameters

- `sceneSession`: The session whose scene you want to remove from the screen and app switcher.
- `options`: Information for the system to use when dismissing the scene. For information about how to create this object, see  .
- `errorHandler`: An error handler block to execute if a problem occurs. The method does not execute this block when it successfully dismisses the scene. This block has no return value and has the following parameter:

## See Also

- [func activateSceneSession(for: UISceneSessionActivationRequest, errorHandler: ((any Error) -> Void)?)](uiapplication/activatescenesession(for:errorhandler:).md)
  Asks the system to activate an existing scene or create a new scene and associate it with your app.
- [func requestSceneSessionRefresh(UISceneSession)](uiapplication/requestscenesessionrefresh(_:).md)
  Asks the system to update any system UI associated with the specified scene.
- [struct UISceneSessionActivationRequest](uiscenesessionactivationrequest-swift.struct.md)
  A collection of properties that you use to request activation of a scene.
- [UIScene.ActivationRequestOptions](uiscene/activationrequestoptions.md)
  An object that contains information you want the system to use when activating the session associated with a scene.
- [class UISceneDestructionRequestOptions](uiscenedestructionrequestoptions.md)
  An object you pass to UIKit to permanently remove a scene and its associated session from your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/requestscenesessiondestruction(_:options:errorhandler:))*
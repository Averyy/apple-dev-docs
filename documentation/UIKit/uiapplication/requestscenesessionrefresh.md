# requestSceneSessionRefresh(_:)

**Framework**: UIKit  
**Kind**: method

Asks the system to update any system UI associated with the specified scene.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func requestSceneSessionRefresh(_ sceneSession: UISceneSession)
```

#### Discussion

Call this method when your scene is in the background and any part of your scene’s visible appearance changes. For example, call this method after updating your scene’s content to let the system know your scene’s snapshot requires refreshing. You don’t need to call this method when your scene is running in the foreground.

## Parameters

- `sceneSession`: The session whose scene you want to update.

## See Also

- [func activateSceneSession(for: UISceneSessionActivationRequest, errorHandler: ((any Error) -> Void)?)](uiapplication/activatescenesession(for:errorhandler:).md)
  Asks the system to activate an existing scene or create a new scene and associate it with your app.
- [func requestSceneSessionDestruction(UISceneSession, options: UISceneDestructionRequestOptions?, errorHandler: ((any Error) -> Void)?)](uiapplication/requestscenesessiondestruction(_:options:errorhandler:).md)
  Asks the system to dismiss an existing scene and remove it from the app switcher.
- [struct UISceneSessionActivationRequest](uiscenesessionactivationrequest-swift.struct.md)
  A collection of properties that you use to request activation of a scene.
- [UIScene.ActivationRequestOptions](uiscene/activationrequestoptions.md)
  An object that contains information you want the system to use when activating the session associated with a scene.
- [class UISceneDestructionRequestOptions](uiscenedestructionrequestoptions.md)
  An object you pass to UIKit to permanently remove a scene and its associated session from your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/requestscenesessionrefresh(_:))*
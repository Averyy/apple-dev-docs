# activateSceneSession(for:errorHandler:)

**Framework**: UIKit  
**Kind**: method

Asks the system to activate an existing scene or create a new scene and associate it with your app.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- tvOS 17.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func activateSceneSession(for request: UISceneSessionActivationRequest, errorHandler: ((any Error) -> Void)? = nil)
```

## Parameters

- `request`: The activation request.
- `errorHandler`: A handler to call if the request fails.

## See Also

- [func requestSceneSessionActivation(UISceneSession?, userActivity: NSUserActivity?, options: UIScene.ActivationRequestOptions?, errorHandler: ((any Error) -> Void)?)](uiapplication/requestscenesessionactivation(_:useractivity:options:errorhandler:).md)
  Asks the system to activate an existing scene, or create a new scene and associate it with your app.
- [func requestSceneSessionDestruction(UISceneSession, options: UISceneDestructionRequestOptions?, errorHandler: ((any Error) -> Void)?)](uiapplication/requestscenesessiondestruction(_:options:errorhandler:).md)
  Asks the system to dismiss an existing scene and remove it from the app switcher.
- [func requestSceneSessionRefresh(UISceneSession)](uiapplication/requestscenesessionrefresh(_:).md)
  Asks the system to update any system UI associated with the specified scene.
- [struct UISceneSessionActivationRequest](uiscenesessionactivationrequest-swift.struct.md)
  A collection of properties that you use to request activation of a scene.
- [UIScene.ActivationRequestOptions](uiscene/activationrequestoptions.md)
  An object that contains information you want the system to use when activating the session associated with a scene.
- [class UISceneDestructionRequestOptions](uiscenedestructionrequestoptions.md)
  An object you pass to UIKit to permanently remove a scene and its associated session from your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/activatescenesession(for:errorhandler:))*
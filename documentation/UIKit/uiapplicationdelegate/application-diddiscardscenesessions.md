# application(_:didDiscardSceneSessions:)

**Framework**: UIKit  
**Kind**: method

Tells the delegate that the user closed one or more of the app’s scenes from the app switcher.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func application(_ application: UIApplication, didDiscardSceneSessions sceneSessions: Set<UISceneSession>)
```

#### Discussion

When the user removes a scene from the app switcher, UIKit calls this method before discarding the scene’s associated session object altogether. (UIKit also calls this method to discard scenes that it can no longer display.) If your app isn’t running, UIKit calls this method the next time your app launches.

Use this method to update your app’s data structures and to release any resources associated with the scene. For example, you might use this method to update your app’s interface to incorporate the content associated with the scenes.

UIKit calls this method only when dismissing scenes permanently. It doesn’t call it when the system disconnects a scene to free up memory. Memory reclamation deletes the scene objects, but preserves the sessions associated with those scenes.

## Parameters

- `application`: The singleton app object.
- `sceneSessions`: The session objects associated with the discarded scenes.

## See Also

- [func application(UIApplication, configurationForConnecting: UISceneSession, options: UIScene.ConnectionOptions) -> UISceneConfiguration](uiapplicationdelegate/application(_:configurationforconnecting:options:).md)
  Retrieves the configuration data for UIKit to use when creating a new scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:diddiscardscenesessions:))*
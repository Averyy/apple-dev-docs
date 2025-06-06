# application(_:configurationForConnecting:options:)

**Framework**: UIKit  
**Kind**: method

Retrieves the configuration data for UIKit to use when creating a new scene.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func application(_ application: UIApplication, configurationForConnecting connectingSceneSession: UISceneSession, options: UIScene.ConnectionOptions) -> UISceneConfiguration
```

## Mentions

- [Specifying the scenes your app supports](specifying-the-scenes-your-app-supports.md)

#### Return Value

The configuration object containing the information needed to create the scene.

#### Discussion

Implement this method if you don’t include scene-configuration data in your app’s `Info.plist` file, or if you want to alter the scene configuration data dynamically. UIKit calls this method shortly before creating a new scene. In your implementation, return a [`UISceneConfiguration`](uisceneconfiguration.md) object with the scene details, including the type of scene to create, the delegate object you use to manage the scene, and the storyboard containing the initial view controller to display.

If you don’t implement this method, you must provide scene-configuration data in your app’s `Info.plist` file.

## Parameters

- `application`: The singleton app object.
- `connectingSceneSession`: The session object associated with the scene. This object contains the initial configuration data loaded from the app’s   file, if any.
- `options`: System-specific options for configuring the scene.

## See Also

- [func application(UIApplication, didDiscardSceneSessions: Set<UISceneSession>)](uiapplicationdelegate/application(_:diddiscardscenesessions:).md)
  Tells the delegate that the user closed one or more of the app’s scenes from the app switcher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:configurationforconnecting:options:))*
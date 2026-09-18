# UISceneAppIntent

**Framework**: App Intents  
**Kind**: protocol

An interface you use to direct an app intent to a specific scene in your UIKit app.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
protocol UISceneAppIntent : TargetContentProvidingIntent
```

## Mentions

- [Directing app intents to your app’s scenes](directing-app-intents-to-your-apps-scenes.md)
- [Configuring the runtime behavior of your app intents](configuring-the-runtime-behavior-of-your-app-intents.md)

#### Overview

In a UIKit app, adopt this protocol in an app intent that causes the system to launch your app in the foreground. For example, include this protocol in an app intent that also supports the [`OpenIntent`](openintent.md) protocol. The `UISceneAppIntent` protocol tells the system to deliver the app intent to one of your app’s scenes before calling the app intent’s [`perform()`](appintent/perform().md) method. In your scene code, use the app intent to configure views and prepare your app’s interface for the app intent.

In addition to adopting this protocol in your app intent, update your scene’s delegate object to support the [`AppIntentSceneDelegate`](appintentscenedelegate.md) protocol. The scene uses that protocol to receive the app intent from the system. If you don’t implement that protocol in your scene delegate, you can alternatively use this protocol’s [`performNavigation(forScene:)`](uisceneappintent/performnavigation(forscene:).md) method to configure your scene from your app intent type.

For more information about how to use app intents to configure your app’s interface, see [`Directing app intents to your app’s scenes`](directing-app-intents-to-your-apps-scenes.md).

## Topics

### Getting the UIKit scene
- [var uiScene: UIScene?](uisceneappintent/uiscene.md)
  The scene that is handling the app intent.
### Updating the app’s interface
- [func performNavigation(forScene: UIScene)](uisceneappintent/performnavigation(forscene:).md)
  Tells the app intent that the system is about to show the specified scene.
### Default Implementations
- [TargetContentProvidingIntent Implementations](uisceneappintent/targetcontentprovidingintent-implementations.md)

## Relationships

### Inherits From
- [AppIntent](appintent.md)
- [PersistentlyIdentifiable](persistentlyidentifiable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [TargetContentProvidingIntent](targetcontentprovidingintent.md)

## See Also

- [Directing app intents to your app’s scenes](directing-app-intents-to-your-apps-scenes.md)
  Direct app intents to a specific SwiftUI or UIKit scene and use the app intent to configure the content of the scene.
- [protocol TargetContentProvidingIntent](targetcontentprovidingintent.md)
  An interface that provides a custom identifier for an app intent.
- [protocol AppIntentSceneDelegate](appintentscenedelegate.md)
  The interface a UIKit scene delegate uses to receive an app intent and configure the scene’s views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/uisceneappintent)*
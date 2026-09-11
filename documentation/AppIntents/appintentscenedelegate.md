# AppIntentSceneDelegate

**Framework**: App Intents  
**Kind**: protocol

The interface a UIKit scene delegate uses to receive an app intent and configure the scene’s views.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
protocol AppIntentSceneDelegate : UISceneDelegate
```

## Mentions

- [Directing app intents to your app’s scenes](directing-app-intents-to-your-apps-scenes.md)

#### Overview

Adopt this protocol in your UIKit scene delegate objects to receive incoming app intents and configure your interface in response. When an app intent needs to run in the foreground, the system picks one of your app’s scenes to display. It then uses this protocol to deliver the app intent to the scene so you can configure the scene accordingly. For example, you might update the scene’s views to display an entity or other content referenced by the app intent. The system delivers the app intent to your scene code before it runs the app intent’s [`perform()`](appintent/perform().md) method. If your scene delegate doesn’t implement this protocol, the system gives your app intent an opportunity to configure the scene through the [`UISceneAppIntent`](uisceneappintent.md) protocol.

For more information about how to use app intents to configure your app’s interface, see [`Directing app intents to your app’s scenes`](directing-app-intents-to-your-apps-scenes.md).

## Topics

### Incorporating the app intent
- [func scene(UIScene, willPerformAppIntent: any UISceneAppIntent)](appintentscenedelegate/scene(_:willperformappintent:).md)
  Asks the scene delegate to prepare the scene for the specified app intent.

## Relationships

### Inherits From
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [UISceneDelegate](../uikit/uiscenedelegate.md)

## See Also

- [Directing app intents to your app’s scenes](directing-app-intents-to-your-apps-scenes.md)
  Direct app intents to a specific SwiftUI or UIKit scene and use the app intent to configure the content of the scene.
- [protocol TargetContentProvidingIntent](targetcontentprovidingintent.md)
  An interface that provides a custom identifier for an app intent.
- [protocol UISceneAppIntent](uisceneappintent.md)
  An interface you use to direct an app intent to a specific scene in your UIKit app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintentscenedelegate)*
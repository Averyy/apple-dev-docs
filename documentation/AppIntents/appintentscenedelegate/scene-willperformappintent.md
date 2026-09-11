# scene(_:willPerformAppIntent:)

**Framework**: App Intents  
**Kind**: method  
**Required**: Yes

Asks the scene delegate to prepare the scene for the specified app intent.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func scene(_ scene: UIScene, willPerformAppIntent appIntent: any UISceneAppIntent)
```

## Mentions

- [Directing app intents to your app’s scenes](directing-app-intents-to-your-apps-scenes.md)

#### Discussion

Implement this method in your scene delegate and use it to incorporate the specified app intent into the scene. For example, you might change the views of your scene to display an entity that the app intent contains. The system calls the app intent’s [`perform()`](appintent/perform().md) method after this method returns.

If you don’t implement this method in your scene delegate, the system calls the [`performNavigation(forScene:)`](uisceneappintent/performnavigation(forscene:).md) method of the app intent to configure the scene instead.

## Parameters

- `scene`: The scene that receives the app intent.
- `appIntent`: The app intent that the system is about to perform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintentscenedelegate/scene(_:willperformappintent:))*
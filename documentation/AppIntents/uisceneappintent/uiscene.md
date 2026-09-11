# uiScene

**Framework**: App Intents  
**Kind**: property

The scene that is handling the app intent.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var uiScene: UIScene? { get }
```

## Mentions

- [Directing app intents to your app’s scenes](directing-app-intents-to-your-apps-scenes.md)

#### Discussion

When the system selects a scene for your app intent, it assigns the scene to this property so your app intent can access it. Check the value of this property only in your app intent’s [`perform()`](appintent/perform().md) method. If the system didn’t associate the app intent with a scene, the value of this property is `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/uisceneappintent/uiscene)*
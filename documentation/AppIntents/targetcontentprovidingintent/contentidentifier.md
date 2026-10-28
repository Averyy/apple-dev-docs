# contentIdentifier

**Framework**: App Intents  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A custom string your app uses to identify the app intent.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var contentIdentifier: String { get }
```

## Mentions

- [Directing app intents to your app’s scenes](../directing-app-intents-to-your-apps-scenes.md)

## Discussion

The protocol provides a default implementation of this property and sets its value to the name of the app intent type. You can also reimplement this property to provide a custom value for your app intent.

## Default Implementations

### TargetContentProvidingIntent Implementations
- [var contentIdentifier: String](./contentidentifier-4cvg3.md)
  A custom string your app uses to identify the app intent.
- [var contentIdentifier: String](./contentidentifier-596wr.md)
  A custom string your app uses to identify the app intent.
### UISceneAppIntent Implementations
- [var contentIdentifier: String](../uisceneappintent/contentidentifier.md)
  A custom string your app uses to identify the app intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/targetcontentprovidingintent/contentidentifier)*
# intent

**Framework**: Foundation  
**Kind**: property

Metadata for populating your share extensions interface.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var intent: INIntent? { get }
```

## Mentions

- [Supporting suggestions in your app’s share extension](supporting-suggestions-in-your-app-s-share-extension.md)

#### Discussion

When the user selects an app from the list of suggested apps in iOS’s share sheet, this property contains metadata that you can use to populate your share extensions interface. The source for the metadata is the [`INSendMessageIntent`](https://developer.apple.com/documentation/Intents/INSendMessageIntent) of your messaging app.

This property is `nil` if your app’s share extension wasn’t launched from the list of suggested apps.

> **Note**:  To learn more about adding a share extension to the list of suggested apps, read [`Supporting suggestions in your app’s share extension`](supporting-suggestions-in-your-app-s-share-extension.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsextensioncontext/intent)*
# init(intent:phrases:shortTitle:systemImageName:)

**Framework**: App Intents  
**Kind**: init

Initializes an App Shortcut with phrases that run the app intent, a title, and an image.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
init<Intent>(intent: Intent, phrases: [AppShortcutPhrase<Intent>], shortTitle: LocalizedStringResource, systemImageName: String) where Intent : AppIntent
```

## Mentions

- [Creating your first app intent](creating-your-first-app-intent.md)

#### Discussion

Use this initializer to create an App Shortcut for your app intent that people discover in the Shortcuts app and that they can run using the Action button on supported iPhone models.

## See Also

- [init<Intent, Value, Parameter, ParameterKeyPath>(intent: Intent, phrases: [AppShortcutPhrase<Intent>], shortTitle: LocalizedStringResource, systemImageName: String, parameterPresentation: AppShortcutParameterPresentation<Intent, Value, Parameter, ParameterKeyPath>)](appshortcut/init(intent:phrases:shorttitle:systemimagename:parameterpresentation:).md)
  Initializes an App Shortcut with phrases that run the app intent, a title, an image, and specified parameters.
- [init<Intent>(intent: Intent, phrases: [AppShortcutPhrase<Intent>], shortTitle: LocalizedStringResource?, systemImageName: String?)](appshortcut/init(intent:phrases:shorttitle:systemimagename:)-2hk1x.md)
  Initializes an App Shortcut with phrases that run the app intent, a title, and an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appshortcut/init(intent:phrases:shorttitle:systemimagename:)-8yntq)*
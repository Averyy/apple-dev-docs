# init(intent:phrases:shortTitle:systemImageName:)

**Framework**: App Intents  
**Kind**: init  
**Role**: Initializer

Initializes an App Shortcut with phrases that run the app intent, a title, and an image.

**Availability**:
- iOS 16.0+ - Deprecated in 17.0
- iPadOS 16.0+ - Deprecated in 17.0
- Mac Catalyst 16.0+ - Deprecated in 17.0
- macOS 13.0+ - Deprecated in 14.0
- tvOS 16.0+ - Deprecated in 17.0
- visionOS
- watchOS 9.0+ - Deprecated in 10.0

> **Deprecated**: Please provide a shortTitle and systemImageName

## Declaration

```swift
init<Intent>(intent: Intent, phrases: [AppShortcutPhrase<Intent>], shortTitle: LocalizedStringResource? = nil, systemImageName: String? = nil) where Intent : AppIntent
```

#### Discussion

Use this initializer to create an App Shortcut for your app intent that people discover in the Shortcuts app and that they can run using the Action button on supported iPhone models.

## See Also

### Creating an app shortcut
- [init<Intent>(intent: Intent, phrases: [AppShortcutPhrase<Intent>], shortTitle: LocalizedStringResource, systemImageName: String)](./init%28intent,phrases,shorttitle,systemimagename%29-8yntq.md)
  Initializes an App Shortcut with phrases that run the app intent, a title, and an image.
- [init<Intent, Value, Parameter, ParameterKeyPath>(intent: Intent, phrases: [AppShortcutPhrase<Intent>], shortTitle: LocalizedStringResource, systemImageName: String, parameterPresentation: AppShortcutParameterPresentation<Intent, Value, Parameter, ParameterKeyPath>)](./init%28intent,phrases,shorttitle,systemimagename,parameterpresentation%29.md)
  Initializes an App Shortcut with phrases that run the app intent, a title, an image, and specified parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appshortcut/init(intent:phrases:shorttitle:systemimagename:)-2hk1x)*
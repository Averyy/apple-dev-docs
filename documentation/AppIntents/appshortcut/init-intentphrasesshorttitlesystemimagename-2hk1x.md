# init(intent:phrases:shortTitle:systemImageName:)

**Framework**: App Intents  
**Kind**: init

Initializes an App Shortcut with phrases that run the app intent, a title, and an image.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
init<Intent>(intent: Intent, phrases: [AppShortcutPhrase<Intent>], shortTitle: LocalizedStringResource? = nil, systemImageName: String? = nil) where Intent : AppIntent
```

#### Discussion

Use this initializer to create an App Shortcut for your app intent that people discover in the Shortcuts app and that they can run using the Action button on supported iPhone models.

## See Also

- [init<Intent>(intent: Intent, phrases: [AppShortcutPhrase<Intent>], shortTitle: LocalizedStringResource, systemImageName: String)](appshortcut/init(intent:phrases:shorttitle:systemimagename:)-8yntq.md)
  Initializes an App Shortcut with phrases that run the app intent, a title, and an image.
- [init<Intent, Value, Parameter, ParameterKeyPath>(intent: Intent, phrases: [AppShortcutPhrase<Intent>], shortTitle: LocalizedStringResource, systemImageName: String, parameterPresentation: AppShortcutParameterPresentation<Intent, Value, Parameter, ParameterKeyPath>)](appshortcut/init(intent:phrases:shorttitle:systemimagename:parameterpresentation:).md)
  Initializes an App Shortcut with phrases that run the app intent, a title, an image, and specified parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appshortcut/init(intent:phrases:shorttitle:systemimagename:)-2hk1x)*
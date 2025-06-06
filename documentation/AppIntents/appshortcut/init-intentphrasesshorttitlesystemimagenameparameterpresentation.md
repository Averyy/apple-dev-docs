# init(intent:phrases:shortTitle:systemImageName:parameterPresentation:)

**Framework**: App Intents  
**Kind**: init

Initializes an App Shortcut with phrases that run the app intent, a title, an image, and specified parameters.

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
init<Intent, Value, Parameter, ParameterKeyPath>(intent: Intent, phrases: [AppShortcutPhrase<Intent>], shortTitle: LocalizedStringResource, systemImageName: String, parameterPresentation: AppShortcutParameterPresentation<Intent, Value, Parameter, ParameterKeyPath>) where Intent : AppIntent, Value : _IntentValue, Value : Sendable, Parameter : IntentParameter<Value>, ParameterKeyPath : KeyPath<Intent, Parameter>
```

#### Discussion

Use this initializer to create an App Shortcut for your app intent that people discover in the Shortcuts app and that they can run using the Action button on supported iPhone models.

## Parameters

- `intent`: The   associated with the  .
- `phrases`: An array of   associated with the  .
- `shortTitle`: A   representing the short title of the  .
- `systemImageName`: A   representing the system image name for the  .
- `parameterPresentation`: An   object associated with the  .

## See Also

- [init<Intent>(intent: Intent, phrases: [AppShortcutPhrase<Intent>], shortTitle: LocalizedStringResource, systemImageName: String)](appshortcut/init(intent:phrases:shorttitle:systemimagename:)-8yntq.md)
  Initializes an App Shortcut with phrases that run the app intent, a title, and an image.
- [init<Intent>(intent: Intent, phrases: [AppShortcutPhrase<Intent>], shortTitle: LocalizedStringResource?, systemImageName: String?)](appshortcut/init(intent:phrases:shorttitle:systemimagename:)-2hk1x.md)
  Initializes an App Shortcut with phrases that run the app intent, a title, and an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appshortcut/init(intent:phrases:shorttitle:systemimagename:parameterpresentation:))*
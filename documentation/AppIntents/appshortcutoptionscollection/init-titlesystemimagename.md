# init(_:title:systemImageName:)

**Framework**: App Intents  
**Kind**: init

Initializes a collection of options for App Shortcuts with the specified parameters.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
init(_ dynamicOptionsProvider: Provider, title: LocalizedStringResource, systemImageName: String? = nil)
```

## Parameters

- `dynamicOptionsProvider`: The object that provides the dynamic options   for an App Shortcut.
- `title`: A localized string that represents the title for the collection of dynamic options in the Shortcuts app.
- `systemImageName`: The name of the system image for the collection   of App Shortcuts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appshortcutoptionscollection/init(_:title:systemimagename:))*
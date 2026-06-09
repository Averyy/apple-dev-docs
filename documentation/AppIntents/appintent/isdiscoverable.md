# isDiscoverable

**Framework**: App Intents  
**Kind**: property  
**Required**: Yes

A Boolean value that indicates whether system features can discover this app intent.

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
static var isDiscoverable: Bool { get }
```

## Mentions

- [Creating your first app intent](creating-your-first-app-intent.md)

#### Discussion

When the value of this property is `true`, system features like Siri, Spotlight, and the Shortcuts app can discover and use the app intent. When the value of the property is `false`, you can run the intent from your app’s interface or from a widget, but system features can’t access it. The default value of this property is `true`.

> **Note**: App Shortcuts require this property to be `true` for the app intents they use.

## See Also

- [static var title: LocalizedStringResource](appintent/title.md)
  A short, localized, human-readable string that conveys the app intent’s action.
- [static var description: IntentDescription?](appintent/description.md)
  A localized string that describes what the app intent does.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintent/isdiscoverable)*
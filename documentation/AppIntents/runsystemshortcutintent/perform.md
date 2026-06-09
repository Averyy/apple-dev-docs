# perform()

**Framework**: App Intents  
**Kind**: method

Performs a widget’s configured action, like opening another app or performing an App Shortcut, custom shortcut, or system action.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
func perform() async throws -> IntentResultContainer<Never, Never, Never, Never>
```

#### Discussion

The system only performs the intent if it’s triggered by a button you place in widget. The intent doesn’t have any effect in other contexts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/runsystemshortcutintent/perform())*
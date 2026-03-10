# IntentDeprecation

**Framework**: App Intents  
**Kind**: struct

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
struct IntentDeprecation<ReplacementIntent> where ReplacementIntent : AppIntent
```

## Topics

### Initializers
- [init(message: LocalizedStringResource)](intentdeprecation/init(message:).md)
- [init(message: LocalizedStringResource, replacedBy: ReplacementIntent.Type?)](intentdeprecation/init(message:replacedby:).md)
- [init(replacedBy: ReplacementIntent.Type)](intentdeprecation/init(replacedby:).md)
### Instance Properties
- [var message: LocalizedStringResource](intentdeprecation/message.md)
  A short, localized, human-readable string that describes the deprecation of this intent using sentence case and followed by a period.
- [var replacedBy: ReplacementIntent.Type?](intentdeprecation/replacedby.md)
  Optionally, the AppIntent that replaces this one. Note: This is used by the Shortcuts app to help the user find the new AppIntent to use.

## See Also

- [struct IntentSystemContext](intentsystemcontext.md)
  Information that the system makes available to an app intent while it performs its action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentdeprecation)*
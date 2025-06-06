# IntentDeprecation

**Framework**: App Intents  
**Kind**: struct

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

- [protocol AppIntentsPackage](appintentspackage.md)
  A type that describes app intent definitions that aren’t part of an app bundle and their dependencies.
- [struct IntentDescription](intentdescription.md)
  The human-readable description and metadata for an app intent.
- [struct IntentDialog](intentdialog.md)
  The text you want the system to display, or speak, when requesting a value, asking for disambiguation, or confirming an action.
- [class IntentProjection](intentprojection.md)
  Projections for an app intent that returns non-optional values for parameters.
- [struct IntentSystemContext](intentsystemcontext.md)
  Information that the system makes available to an app intent while it performs its action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentdeprecation)*
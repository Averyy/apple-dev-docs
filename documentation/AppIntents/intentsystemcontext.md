# IntentSystemContext

**Framework**: App Intents  
**Kind**: struct

Contextual information that the system provides while it performs an app intent.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
struct IntentSystemContext
```

#### Overview

Access information that the system provides to your app intent while it performs its action in its [`perform()`](appintent/perform().md) implementation. The available information varies by platform. For example, in watchOS, the intent system context includes a precise timestamp when a person starts the app intent’s action using the Action button on Apple Watch Ultra.

## Topics

### Instance Properties
- [var currentMode: IntentModes.Current](intentsystemcontext/currentmode.md)
  A value that indicates the foreground and background behavior for app intent’s action.
- [var isVoiceOnly: Bool](intentsystemcontext/isvoiceonly.md)
  A Boolean value that indicates whether the system performs the app intent in a voice-only context.
- [var locale: Locale](intentsystemcontext/locale.md)
  The locale in which the system performs the app intent.
- [var preciseTimestamp: Date?](intentsystemcontext/precisetimestamp.md)
  A precise timestamp for the performed action.

## See Also

- [struct IntentModes](intentmodes.md)
  A set of options you use to configure the runtime behavior of an app intent.
- [struct IntentDescription](intentdescription.md)
  The human-readable description and metadata for an app intent.
- [struct IntentDialog](intentdialog.md)
  The text you want the system to display, or speak, when requesting a value, asking for disambiguation, or confirming an action.
- [struct IntentDeprecation](intentdeprecation.md)
- [class IntentProjection](intentprojection.md)
  Projections for an app intent that returns non-optional values for parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentsystemcontext)*
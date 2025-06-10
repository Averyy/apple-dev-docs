# AppShortcutParameterPresentationSummary

**Framework**: App Intents  
**Kind**: struct

The summary of the presentation of an App Shortcut parameter.

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
struct AppShortcutParameterPresentationSummary<Intent, Value, Parameter, ParameterKeyPath> where Intent : AppIntent, Value : _IntentValue, Value : Sendable, Parameter : IntentParameter<Value>, ParameterKeyPath : KeyPath<Intent, Parameter>
```

#### Overview

Make sure to provide a summary string that includes the parameter in the interpolation; for example, `"Call \(\.$person)"`.

## Topics

### Initializers
- [init(AppShortcutParameterPresentationSummaryString<Intent, Value, Parameter, ParameterKeyPath>, table: StaticString?)](appshortcutparameterpresentationsummary/init(_:table:).md)
  Initializes a presentation summary with the specified parameters.

## See Also

- [struct AppShortcutParameterPresentation](appshortcutparameterpresentation.md)
  Describes the presentation of an App Shortcut  for the provided parameter.
- [struct AppShortcutParameterPresentationSummaryString](appshortcutparameterpresentationsummarystring.md)
- [struct AppShortcutParameterPresentationTitle](appshortcutparameterpresentationtitle.md)
  A struct that represents the title of the presentation of an App Shortcut.
- [struct AppShortcutParameterPresentationTitleString](appshortcutparameterpresentationtitlestring.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appshortcutparameterpresentationsummary)*
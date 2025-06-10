# AppShortcutParameterPresentationTitle

**Framework**: App Intents  
**Kind**: struct

A struct that represents the title of the presentation of an App Shortcut.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+
- Unknown ?+ - Deprecated
- Mac Catalyst ?+

## Declaration

```swift
struct AppShortcutParameterPresentationTitle<Intent, Value, Parameter, ParameterKeyPath> where Intent : AppIntent, Value : _IntentValue, Value : Sendable, Parameter : IntentParameter<Value>, ParameterKeyPath : KeyPath<Intent, Parameter>
```

#### Overview

Provide a specific and a generic title. The specific title should include the parameter in the interpolation. For example provide `"Call \(\.$person)"` as a specific title that includes the parameter and a simple string that doesn’t have the parameter specified, e.g. `"Call Person..."`.

## Topics

### Initializers
- [init(specific: AppShortcutParameterPresentationTitleString<Intent, Value, Parameter, ParameterKeyPath>, generic: StaticString, table: StaticString?)](appshortcutparameterpresentationtitle/init(specific:generic:table:).md)
  Initializes an `AppShortcutParameterPresentationTitle` with the specified parameters.

## See Also

- [struct AppShortcutParameterPresentation](appshortcutparameterpresentation.md)
  Describes the presentation of an App Shortcut  for the provided parameter.
- [struct AppShortcutParameterPresentationSummary](appshortcutparameterpresentationsummary.md)
  The summary of the presentation of an App Shortcut parameter.
- [struct AppShortcutParameterPresentationSummaryString](appshortcutparameterpresentationsummarystring.md)
- [struct AppShortcutParameterPresentationTitleString](appshortcutparameterpresentationtitlestring.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appshortcutparameterpresentationtitle)*
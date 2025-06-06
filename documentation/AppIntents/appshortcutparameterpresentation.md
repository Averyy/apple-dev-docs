# AppShortcutParameterPresentation

**Framework**: App Intents  
**Kind**: struct

Describes the presentation of an App Shortcut  for the provided parameter.

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
struct AppShortcutParameterPresentation<Intent, Value, Parameter, ParameterKeyPath> where Intent : AppIntent, Value : _IntentValue, Value : Sendable, Parameter : IntentParameter<Value>, ParameterKeyPath : KeyPath<Intent, Parameter>
```

## Topics

### Initializers
- [init(for: ParameterKeyPath, summary: AppShortcutParameterPresentationSummary<Intent, Value, Parameter, ParameterKeyPath>, optionsCollections: () -> some AppShortcutOptionsCollectionSpecification<Value.UnwrappedType>)](appshortcutparameterpresentation/init(for:summary:optionscollections:).md)
  Creates an object that represents the App Shortcut with the specified parameters.

## See Also

- [struct AppShortcutParameterPresentationSummary](appshortcutparameterpresentationsummary.md)
  The summary of the presentation of an App Shortcut parameter.
- [struct AppShortcutParameterPresentationSummaryString](appshortcutparameterpresentationsummarystring.md)
- [struct AppShortcutParameterPresentationTitle](appshortcutparameterpresentationtitle.md)
  A struct that represents the title of the presentation of an App Shortcut.
- [struct AppShortcutParameterPresentationTitleString](appshortcutparameterpresentationtitlestring.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appshortcutparameterpresentation)*
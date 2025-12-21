# AppShortcutParameterPresentationSummaryString

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
struct AppShortcutParameterPresentationSummaryString<Intent, Value, Parameter, ParameterKeyPath> where Intent : AppIntent, Value : _IntentValue, Value : Sendable, Parameter : IntentParameter<Value>, ParameterKeyPath : KeyPath<Intent, Parameter>
```

## Topics

### Initializers
- [init(String)](appshortcutparameterpresentationsummarystring/init(_:).md)

## Relationships

### Conforms To
- [ExpressibleByExtendedGraphemeClusterLiteral](../Swift/ExpressibleByExtendedGraphemeClusterLiteral.md)
- [ExpressibleByStringInterpolation](../Swift/ExpressibleByStringInterpolation.md)
- [ExpressibleByStringLiteral](../Swift/ExpressibleByStringLiteral.md)
- [ExpressibleByUnicodeScalarLiteral](../Swift/ExpressibleByUnicodeScalarLiteral.md)

## See Also

- [struct AppShortcutParameterPresentation](appshortcutparameterpresentation.md)
  Describes the presentation of an App Shortcut  for the provided parameter.
- [struct AppShortcutParameterPresentationSummary](appshortcutparameterpresentationsummary.md)
  The summary of the presentation of an App Shortcut parameter.
- [struct AppShortcutParameterPresentationTitle](appshortcutparameterpresentationtitle.md)
  A struct that represents the title of the presentation of an App Shortcut.
- [struct AppShortcutParameterPresentationTitleString](appshortcutparameterpresentationtitlestring.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appshortcutparameterpresentationsummarystring)*
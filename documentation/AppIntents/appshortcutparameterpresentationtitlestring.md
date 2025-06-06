# AppShortcutParameterPresentationTitleString

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
- Unknown ?+ - Deprecated

## Declaration

```swift
struct AppShortcutParameterPresentationTitleString<Intent, Value, Parameter, ParameterKeyPath> where Intent : AppIntent, Value : _IntentValue, Value : Sendable, Parameter : IntentParameter<Value>, ParameterKeyPath : KeyPath<Intent, Parameter>
```

## Topics

### Structures
- [AppShortcutParameterPresentationTitleString.StringInterpolation](appshortcutparameterpresentationtitlestring/stringinterpolation.md)
  The type each segment of a string literal containing interpolations should be appended to.
### Initializers
- [init(String)](appshortcutparameterpresentationtitlestring/init(_:).md)
- [init(stringInterpolation: AppShortcutParameterPresentationTitleString<Intent, Value, Parameter, ParameterKeyPath>.StringInterpolation)](appshortcutparameterpresentationtitlestring/init(stringinterpolation:).md)
  Creates an instance from a string interpolation.
- [init(stringLiteral: String)](appshortcutparameterpresentationtitlestring/init(stringliteral:).md)
  Creates an instance initialized to the given string value.
### Type Aliases
- [AppShortcutParameterPresentationTitleString.ExtendedGraphemeClusterLiteralType](appshortcutparameterpresentationtitlestring/extendedgraphemeclusterliteraltype.md)
  A type that represents an extended grapheme cluster literal.
- [AppShortcutParameterPresentationTitleString.StringLiteralType](appshortcutparameterpresentationtitlestring/stringliteraltype.md)
  A type that represents a string literal.
- [AppShortcutParameterPresentationTitleString.UnicodeScalarLiteralType](appshortcutparameterpresentationtitlestring/unicodescalarliteraltype.md)
  A type that represents a Unicode scalar literal.
### Default Implementations
- [ExpressibleByExtendedGraphemeClusterLiteral Implementations](appshortcutparameterpresentationtitlestring/expressiblebyextendedgraphemeclusterliteral-implementations.md)
- [ExpressibleByStringLiteral Implementations](appshortcutparameterpresentationtitlestring/expressiblebystringliteral-implementations.md)

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
- [struct AppShortcutParameterPresentationSummaryString](appshortcutparameterpresentationsummarystring.md)
- [struct AppShortcutParameterPresentationTitle](appshortcutparameterpresentationtitle.md)
  A struct that represents the title of the presentation of an App Shortcut.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appshortcutparameterpresentationtitlestring)*
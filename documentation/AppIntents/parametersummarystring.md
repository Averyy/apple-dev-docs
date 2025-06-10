# ParameterSummaryString

**Framework**: App Intents  
**Kind**: struct

A human-readable string that interpolates parameter key paths to provide user-configurable placeholders in the Shortcuts app.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
struct ParameterSummaryString<Intent> where Intent : AppIntent
```

## Topics

### Creating the summary string
- [init(String)](parametersummarystring/init(_:).md)
- [init(stringLiteral: String)](parametersummarystring/init(stringliteral:).md)
  Creates an instance initialized to the given string value.
- [init(stringInterpolation: ParameterSummaryString<Intent>.StringInterpolation)](parametersummarystring/init(stringinterpolation:).md)
  Creates an instance from a string interpolation.
- [ParameterSummaryString.StringInterpolation](parametersummarystring/stringinterpolation.md)
  The type each segment of a string literal containing interpolations should be appended to.
### Type Aliases
- [ParameterSummaryString.ExtendedGraphemeClusterLiteralType](parametersummarystring/extendedgraphemeclusterliteraltype.md)
  A type that represents an extended grapheme cluster literal.
- [ParameterSummaryString.StringLiteralType](parametersummarystring/stringliteraltype.md)
  A type that represents a string literal.
- [ParameterSummaryString.UnicodeScalarLiteralType](parametersummarystring/unicodescalarliteraltype.md)
  A type that represents a Unicode scalar literal.
### Default Implementations
- [ExpressibleByExtendedGraphemeClusterLiteral Implementations](parametersummarystring/expressiblebyextendedgraphemeclusterliteral-implementations.md)
- [ExpressibleByStringLiteral Implementations](parametersummarystring/expressiblebystringliteral-implementations.md)

## Relationships

### Conforms To
- [ExpressibleByExtendedGraphemeClusterLiteral](../Swift/ExpressibleByExtendedGraphemeClusterLiteral.md)
- [ExpressibleByStringInterpolation](../Swift/ExpressibleByStringInterpolation.md)
- [ExpressibleByStringLiteral](../Swift/ExpressibleByStringLiteral.md)
- [ExpressibleByUnicodeScalarLiteral](../Swift/ExpressibleByUnicodeScalarLiteral.md)

## See Also

- [protocol ParameterSummary](parametersummary.md)
  An interface for defining the visual representation of an app intent’s parameters.
- [struct IntentParameterSummary](intentparametersummary.md)
  A type that describes the user interface configuration of an app intent’s parameters.
- [struct ParameterSummaryWhenCondition](parametersummarywhencondition.md)
  A type that represents a conditional statement in a parameter summary.
- [struct ParameterSummarySwitchCondition](parametersummaryswitchcondition.md)
  A type that represents a switch statement in a parameter summary.
- [struct ParameterSummaryCaseCondition](parametersummarycasecondition.md)
  A type that represents an individual case of a switch statement in a parameter summary.
- [struct ParameterSummaryDefaultCaseCondition](parametersummarydefaultcasecondition.md)
  A type that represents the default case of a switch statement in a parameter summary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/parametersummarystring)*
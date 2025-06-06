# IntentDialog

**Framework**: App Intents  
**Kind**: struct

The text you want the system to display, or speak, when requesting a value, asking for disambiguation, or confirming an action.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct IntentDialog
```

## Topics

### Creating a dialog
- [init(LocalizedStringResource)](intentdialog/init(_:).md)
  The text you want the system to display, or speak, when requesting a value, asking for disambiguation, or confirming an action.
- [init(stringLiteral: String)](intentdialog/init(stringliteral:).md)
  Creates an instance initialized to the given string value.
- [init(stringInterpolation: String.LocalizationValue.StringInterpolation)](intentdialog/init(stringinterpolation:).md)
  Creates an instance from a string interpolation.
- [init(full: LocalizedStringResource, supporting: LocalizedStringResource)](intentdialog/init(full:supporting:).md)
  The text you want the system to display, or speak, when requesting a value, asking for disambiguation, or confirming an action.
### Initializers
- [init(full: LocalizedStringResource, supporting: LocalizedStringResource, systemImageName: String)](intentdialog/init(full:supporting:systemimagename:).md)
  The text you want the system to display, or speak, when requesting a value, asking for disambiguation, or confirming an action.
- [init(full: LocalizedStringResource, systemImageName: String)](intentdialog/init(full:systemimagename:).md)
  The text you want the system to display, or speak, when requesting a value, asking for disambiguation, or confirming an action.
### Type Aliases
- [IntentDialog.ExtendedGraphemeClusterLiteralType](intentdialog/extendedgraphemeclusterliteraltype.md)
  A type that represents an extended grapheme cluster literal.
- [IntentDialog.StringInterpolation](intentdialog/stringinterpolation.md)
  The type each segment of a string literal containing interpolations should be appended to.
- [IntentDialog.StringLiteralType](intentdialog/stringliteraltype.md)
  A type that represents a string literal.
- [IntentDialog.UnicodeScalarLiteralType](intentdialog/unicodescalarliteraltype.md)
  A type that represents a Unicode scalar literal.
### Default Implementations
- [ExpressibleByExtendedGraphemeClusterLiteral Implementations](intentdialog/expressiblebyextendedgraphemeclusterliteral-implementations.md)
- [ExpressibleByStringLiteral Implementations](intentdialog/expressiblebystringliteral-implementations.md)

## Relationships

### Conforms To
- [ExpressibleByExtendedGraphemeClusterLiteral](../Swift/ExpressibleByExtendedGraphemeClusterLiteral.md)
- [ExpressibleByStringInterpolation](../Swift/ExpressibleByStringInterpolation.md)
- [ExpressibleByStringLiteral](../Swift/ExpressibleByStringLiteral.md)
- [ExpressibleByUnicodeScalarLiteral](../Swift/ExpressibleByUnicodeScalarLiteral.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [protocol AppIntentsPackage](appintentspackage.md)
  A type that describes app intent definitions that aren’t part of an app bundle and their dependencies.
- [struct IntentDescription](intentdescription.md)
  The human-readable description and metadata for an app intent.
- [struct IntentDeprecation](intentdeprecation.md)
- [class IntentProjection](intentprojection.md)
  Projections for an app intent that returns non-optional values for parameters.
- [struct IntentSystemContext](intentsystemcontext.md)
  Information that the system makes available to an app intent while it performs its action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentdialog)*
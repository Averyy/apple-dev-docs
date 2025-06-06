# AttributedString.FormattingOptions

**Framework**: Foundation  
**Kind**: struct

Options that affect the handling of attributes.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct FormattingOptions
```

## Topics

### Creating Formatting Options
- [init()](attributedstring/init.md)
  Creates an empty attributed string.
- [init(NSAttributedString)](attributedstring/init(_:)-1fru0.md)
  Creates a value-type attributed string from a reference type.
- [init(AttributedSubstring)](attributedstring/init(_:)-8tnoq.md)
  Creates an attributed string from an attributed substring.
### Using Defined Formatting Options
- [static let applyReplacementIndexAttribute: AttributedString.FormattingOptions](attributedstring/formattingoptions/applyreplacementindexattribute.md)
  An option to add an attribute that marks replacements in localized strings.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [init(localized: String.LocalizationValue, options: AttributedString.FormattingOptions, table: String?, bundle: Bundle?, locale: Locale?, comment: StaticString?)](attributedstring/init(localized:options:table:bundle:locale:comment:)-8dlnl.md)
  Creates an attributed string by looking up a localized string from the app’s bundle.
- [init<S>(localized: String.LocalizationValue, options: AttributedString.FormattingOptions, table: String?, bundle: Bundle?, locale: Locale?, comment: StaticString?, including: S.Type)](attributedstring/init(localized:options:table:bundle:locale:comment:including:)-8uknv.md)
  Creates an attributed string by looking up a localized string from the app’s bundle, including an attribute scope.
- [init<S>(localized: String.LocalizationValue, options: AttributedString.FormattingOptions, table: String?, bundle: Bundle?, locale: Locale?, comment: StaticString?, including: KeyPath<AttributeScopes, S.Type>)](attributedstring/init(localized:options:table:bundle:locale:comment:including:)-5jzpg.md)
  Creates an attributed string by looking up a localized string from the app’s bundle, including an attribute scope that a key path identifies.
- [String.LocalizationValue](../Swift/String/LocalizationValue.md)
  A reference to a localizable string, with optional string interpolation.
- [init(localized: LocalizedStringResource)](attributedstring/init(localized:).md)
  Creates a localized attributed string from a localized string resource.
- [init<S>(localized: LocalizedStringResource, including: S.Type)](attributedstring/init(localized:including:)-2xebo.md)
  Creates a localized attributed string from a localized string resource, including an attribute scope.
- [init<S>(localized: LocalizedStringResource, including: KeyPath<AttributeScopes, S.Type>)](attributedstring/init(localized:including:)-15xc5.md)
  Creates a localized attributed string from a localized string resource, including an attribute scope that a key path identifies.
- [struct LocalizedStringResource](localizedstringresource.md)
  A reference to a localizable string, accessible from another process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/formattingoptions)*
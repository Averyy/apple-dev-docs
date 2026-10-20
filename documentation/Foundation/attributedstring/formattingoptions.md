# AttributedString.FormattingOptions

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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
- [init()](./init%28%29.md)
  Creates an empty attributed string.
- [init(NSAttributedString)](./init%28_%29-1fru0.md)
  Creates a value-type attributed string from a reference type.
- [init(AttributedSubstring)](./init%28_%29-8tnoq.md)
  Creates an attributed string from an attributed substring.
### Using Defined Formatting Options
- [static let applyReplacementIndexAttribute: AttributedString.FormattingOptions](./formattingoptions/applyreplacementindexattribute.md)
  An option to add an attribute that marks replacements in localized strings.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Creating a Localized Attributed String
- [init(localized: String.LocalizationValue, options: AttributedString.FormattingOptions, table: String?, bundle: Bundle?, locale: Locale?, comment: StaticString?)](./init%28localized,options,table,bundle,locale,comment%29-8dlnl.md)
  Creates an attributed string by looking up a localized string from the app’s bundle.
- [init<S>(localized: String.LocalizationValue, options: AttributedString.FormattingOptions, table: String?, bundle: Bundle?, locale: Locale?, comment: StaticString?, including: S.Type)](./init%28localized,options,table,bundle,locale,comment,including%29-8uknv.md)
  Creates an attributed string by looking up a localized string from the app’s bundle, including an attribute scope.
- [init<S>(localized: String.LocalizationValue, options: AttributedString.FormattingOptions, table: String?, bundle: Bundle?, locale: Locale?, comment: StaticString?, including: KeyPath<AttributeScopes, S.Type>)](./init%28localized,options,table,bundle,locale,comment,including%29-5jzpg.md)
  Creates an attributed string by looking up a localized string from the app’s bundle, including an attribute scope that a key path identifies.
- [String.LocalizationValue](../../Swift/string/localizationvalue.md)
  A reference to a localizable string, with optional string interpolation.
- [init(localized: LocalizedStringResource)](./init%28localized%29.md)
  Creates a localized attributed string from a localized string resource.
- [init<S>(localized: LocalizedStringResource, including: S.Type)](./init%28localized,including%29-2xebo.md)
  Creates a localized attributed string from a localized string resource, including an attribute scope.
- [init<S>(localized: LocalizedStringResource, including: KeyPath<AttributeScopes, S.Type>)](./init%28localized,including%29-15xc5.md)
  Creates a localized attributed string from a localized string resource, including an attribute scope that a key path identifies.
- [struct LocalizedStringResource](../localizedstringresource.md)
  A reference to a localizable string, accessible from another process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/formattingoptions)*
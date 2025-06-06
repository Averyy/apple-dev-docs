# init(localized:including:)

**Framework**: Foundation  
**Kind**: init

Creates a localized attributed string from a localized string resource, including an attribute scope.

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
init<S>(localized resource: LocalizedStringResource, including scope: S.Type) where S : AttributeScope
```

#### Discussion

Call this initializer to look up the localization indicated by `resource`. Alter the resource’s [`locale`](localizedstringresource/locale.md) prior to calling this method if you want to localize this string in a different locale than the process that created the [`LocalizedStringResource`](localizedstringresource.md).

The attributed string contains attributes of type [`AttributeScopes.FoundationAttributes.LocalizedStringArgumentAttributes`](attributescopes/foundationattributes/localizedstringargumentattributes-swift.struct.md) to indicate runs containing formatted text, such as localized numbers or dates. Access these attributes with the attribute key [`localizedNumericArgument`](attributescopes/foundationattributes/localizedstringargumentattributes-swift.struct/localizednumericargument.md) or [`localizedDateArgument`](attributescopes/foundationattributes/localizedstringargumentattributes-swift.struct/localizeddateargument.md).

## Parameters

- `resource`: A   that provides the localization key, table, bundle, and locale.
- `scope`: An attribute scope to associate with the attributed string.

## See Also

- [init(localized: String.LocalizationValue, options: AttributedString.FormattingOptions, table: String?, bundle: Bundle?, locale: Locale?, comment: StaticString?)](attributedstring/init(localized:options:table:bundle:locale:comment:)-8dlnl.md)
  Creates an attributed string by looking up a localized string from the app’s bundle.
- [init<S>(localized: String.LocalizationValue, options: AttributedString.FormattingOptions, table: String?, bundle: Bundle?, locale: Locale?, comment: StaticString?, including: S.Type)](attributedstring/init(localized:options:table:bundle:locale:comment:including:)-8uknv.md)
  Creates an attributed string by looking up a localized string from the app’s bundle, including an attribute scope.
- [init<S>(localized: String.LocalizationValue, options: AttributedString.FormattingOptions, table: String?, bundle: Bundle?, locale: Locale?, comment: StaticString?, including: KeyPath<AttributeScopes, S.Type>)](attributedstring/init(localized:options:table:bundle:locale:comment:including:)-5jzpg.md)
  Creates an attributed string by looking up a localized string from the app’s bundle, including an attribute scope that a key path identifies.
- [String.LocalizationValue](../Swift/String/LocalizationValue.md)
  A reference to a localizable string, with optional string interpolation.
- [AttributedString.FormattingOptions](attributedstring/formattingoptions.md)
  Options that affect the handling of attributes.
- [init(localized: LocalizedStringResource)](attributedstring/init(localized:).md)
  Creates a localized attributed string from a localized string resource.
- [init<S>(localized: LocalizedStringResource, including: KeyPath<AttributeScopes, S.Type>)](attributedstring/init(localized:including:)-15xc5.md)
  Creates a localized attributed string from a localized string resource, including an attribute scope that a key path identifies.
- [struct LocalizedStringResource](localizedstringresource.md)
  A reference to a localizable string, accessible from another process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/init(localized:including:)-2xebo)*
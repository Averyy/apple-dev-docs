# init(localized:options:table:bundle:locale:comment:including:)

**Framework**: Foundation  
**Kind**: init

Creates an attributed string by looking up a localized string from the app’s bundle, including an attribute scope that a key path identifies.

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
init<S>(localized key: String.LocalizationValue, options: AttributedString.FormattingOptions = [], table: String? = nil, bundle: Bundle? = nil, locale: Locale? = nil, comment: StaticString? = nil, including scope: KeyPath<AttributeScopes, S.Type>) where S : AttributeScope
```

#### Discussion

To create localizable attributed strings, use Markdown syntax in your strings files. The following example shows a string from a Spanish localization:

```other
"_Please visit our [website](https://www.example.com)._" = "_Visita nuestro [sitio web](https://www.example.com)._";
```

You load this string with one of the initializers that takes `localized` as its first parameter, like the following:

```swift
let visitString = AttributedString(localized: "_Please visit our [website](https://www.example.com)._")
```

The resulting attributed string contains an [`inlinePresentationIntent`](attributescopes/foundationattributes/inlinepresentationintent.md) attribute to apply the [`emphasized`](inlinepresentationintent/emphasized.md) presentation intent over the entire string. It also applies the [`link`](attributescopes/foundationattributes/link.md) attribute to the text `sitio web`. User interface frameworks like SwiftUI and UIKit can then use these attributes when presenting the text to the user.

##### Applying Automatic Grammar Agreement

To apply the automatic grammar agreement feature when loading a localized string, use Apple’s Markdown extension syntax: `^[text to inflect](inflect: true)`. The following example shows a format string with a Spanish localization for a food-ordering app.

```other
"_Please visit our [website](https://www.example.com)._" = "_Visita nuestro [sitio web](https://www.example.com)._";
```

You load and localize this string as follows:

```swift
let orderString = AttributedString(
     localized: "Add ^[\(quantity) \(foodSizeSelection.localizedName) \(food.localizedName)](inflect: true) to your order")
// "Añadir 2 ensaladas grandes a tu pedido."
```

When the string loads, the automatic grammar agreement feature adjusts the text for `foodSizeSelection` and `food` to match the number and gender of the sentence.

## Parameters

- `key`: The key for a string in the table that   identifies.
- `options`: Options that affect the handling of attributes.
- `table`: The bundle’s string table to search. If   is   or is an empty string, the method attempts to use the table in  . The default is  .
- `bundle`: The bundle to use for looking up strings. If  , an app searches its main bundle. The default is  .
- `locale`: The locale of the localized string to retrieve. If  , this initializer uses the current locale. The default is  .
- `comment`: The comment to place above the key-value pair in the strings file. This parameter provides the translator with some context about the localized string’s presentation to the user.
- `scope`: An   key path that identifies an attribute scope to associate with the attributed string.

## See Also

- [init(localized: String.LocalizationValue, options: AttributedString.FormattingOptions, table: String?, bundle: Bundle?, locale: Locale?, comment: StaticString?)](attributedstring/init(localized:options:table:bundle:locale:comment:)-8dlnl.md)
  Creates an attributed string by looking up a localized string from the app’s bundle.
- [init<S>(localized: String.LocalizationValue, options: AttributedString.FormattingOptions, table: String?, bundle: Bundle?, locale: Locale?, comment: StaticString?, including: S.Type)](attributedstring/init(localized:options:table:bundle:locale:comment:including:)-8uknv.md)
  Creates an attributed string by looking up a localized string from the app’s bundle, including an attribute scope.
- [String.LocalizationValue](../Swift/String/LocalizationValue.md)
  A reference to a localizable string, with optional string interpolation.
- [AttributedString.FormattingOptions](attributedstring/formattingoptions.md)
  Options that affect the handling of attributes.
- [init(localized: LocalizedStringResource)](attributedstring/init(localized:).md)
  Creates a localized attributed string from a localized string resource.
- [init<S>(localized: LocalizedStringResource, including: S.Type)](attributedstring/init(localized:including:)-2xebo.md)
  Creates a localized attributed string from a localized string resource, including an attribute scope.
- [init<S>(localized: LocalizedStringResource, including: KeyPath<AttributeScopes, S.Type>)](attributedstring/init(localized:including:)-15xc5.md)
  Creates a localized attributed string from a localized string resource, including an attribute scope that a key path identifies.
- [struct LocalizedStringResource](localizedstringresource.md)
  A reference to a localizable string, accessible from another process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/init(localized:options:table:bundle:locale:comment:including:)-5jzpg)*
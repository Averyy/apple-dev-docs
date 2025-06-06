# init(localized:defaultValue:options:table:bundle:locale:comment:including:)

**Framework**: Foundation  
**Kind**: init

Creates an attributed string by looking up a localized string from the app’s bundle, including an attribute scope, using a default value if necessary.

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
init<S>(localized key: StaticString, defaultValue: String.LocalizationValue, options: AttributedString.FormattingOptions = [], table: String? = nil, bundle: Bundle? = nil, locale: Locale? = nil, comment: StaticString? = nil, including scope: S.Type) where S : AttributeScope
```

#### Discussion

Use this initializer instead of [`init(localized:options:table:bundle:locale:comment:including:)`](attributedstring/init(localized:options:table:bundle:locale:comment:including:)-8uknv.md) if you prefer to use a symbolic string key, rather than use the development language’s string as the key.

## Parameters

- `key`: The key for a string in the table that   identifies.
- `defaultValue`: The localized string for the development locale. For other locales, the string uses this value if a localized string for   isn’t found in the table.
- `options`: Options that affect the handling of attributes.
- `table`: The bundle’s string table to search. If   is   or is an empty string, the method attempts to use the table in  . The default is  .
- `bundle`: The bundle to use for looking up strings. If  , an app searches its main bundle. The default is  .
- `locale`: The locale of the localized string to retrieve. If  , this initializer uses the current locale. The default is  .
- `comment`: The comment to place above the key-value pair in the strings file. This parameter provides the translator with some context about the localized string’s presentation to the user.
- `scope`: An attribute scope to associate with the attributed string.

## See Also

- [init(localized: StaticString, defaultValue: String.LocalizationValue, options: AttributedString.FormattingOptions, table: String?, bundle: Bundle?, locale: Locale?, comment: StaticString?)](attributedstring/init(localized:defaultvalue:options:table:bundle:locale:comment:)-4n8e2.md)
  Creates an attributed string by looking up a localized string from the app’s bundle, using a default value if necessary.
- [init<S>(localized: StaticString, defaultValue: String.LocalizationValue, options: AttributedString.FormattingOptions, table: String?, bundle: Bundle?, locale: Locale?, comment: StaticString?, including: KeyPath<AttributeScopes, S.Type>)](attributedstring/init(localized:defaultvalue:options:table:bundle:locale:comment:including:)-9gjtg.md)
  Creates an attributed string by looking up a localized string from the app’s bundle, including an attribute scope that a key path identifies, using a default value if necessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/init(localized:defaultvalue:options:table:bundle:locale:comment:including:)-2elmp)*
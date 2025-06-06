# init(localized:table:bundle:locale:comment:)

**Framework**: Swift  
**Kind**: init

Creates a localized string from an interpolated string.

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
init(localized keyAndValue: String.LocalizationValue, table: String? = nil, bundle: Bundle? = nil, locale: Locale = .current, comment: StaticString? = nil)
```

#### Discussion

Use this initializer when the development-language string serves as your localization key. You can use a fixed string for the key or a string that the system interpolates from values you provide at runtime. For example, if your app’s strings catalog contains a localizable entry for ` “Hello, %@.”`, you create a localized string like the following:

```swift
// Assume the strings file or catalog contains "Hello, %@." for English
// and "Bonjour, %@." for French.
let userName = "Juan"
let greeting = String(localized: "Hello, \(userName).")
// greeting == "Hello, Juan." in en locale, "Bonjour, Juan." in fr locale.
```

If you prefer to use an arbitrary localization key rather than the localized string in the development language, use [`init(localized:defaultValue:table:bundle:locale:comment:)`](string/init(localized:defaultvalue:table:bundle:locale:comment:).md). If you need to provide localized strings to another process that might be using a different locale, use [`init(localized:)`](string/init(localized:).md).

## Parameters

- `keyAndValue`: A   that provides the localization key to look up. This parameter also serves as the default value if the system can’t find a localized string.
- `table`: The bundle’s string table to search. If   is   or is an empty string, the method attempts to use the table named  . The default is  .
- `bundle`: The bundle to use for looking up strings. If  , an app searches its main bundle. The default is  .
- `locale`: The locale to use when localizing interpolated values, such as numbers. This doesn’t change which locale the system uses to look up the localized string. If  , this initializer uses the current locale. The default is  .
- `comment`: The comment to place above the key-value pair in the strings file. This parameter provides the translator with some context about the localized string’s presentation to the user.

## See Also

- [init(localized: String.LocalizationValue, options: String.LocalizationOptions, table: String?, bundle: Bundle?, locale: Locale, comment: StaticString?)](string/init(localized:options:table:bundle:locale:comment:).md)
  Creates a localized string from an interpolated string, applying the specified options.
- [String.LocalizationValue](string/localizationvalue.md)
  A reference to a localizable string, with optional string interpolation.
- [String.LocalizationOptions](string/localizationoptions.md)
  Options to apply when initializing a localized string.
- [init(localized: StaticString, defaultValue: String.LocalizationValue, table: String?, bundle: Bundle?, locale: Locale, comment: StaticString?)](string/init(localized:defaultvalue:table:bundle:locale:comment:).md)
  Creates a localized string from an arbitrary static string key.
- [init(localized: StaticString, defaultValue: String.LocalizationValue, options: String.LocalizationOptions, table: String?, bundle: Bundle?, locale: Locale, comment: StaticString?)](string/init(localized:defaultvalue:options:table:bundle:locale:comment:).md)
  Creates a localized string from an arbitrary static string key, applying the specified options.
- [init(localized: LocalizedStringResource)](string/init(localized:).md)
  Creates a localized string from a localized string resource.
- [init(localized: LocalizedStringResource, options: String.LocalizationOptions)](string/init(localized:options:).md)
  Creates a localized string from a localized string resource, applying the specified options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/init(localized:table:bundle:locale:comment:))*
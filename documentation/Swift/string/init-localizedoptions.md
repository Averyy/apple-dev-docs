# init(localized:options:)

**Framework**: Swift  
**Kind**: init

Creates a localized string from a localized string resource, applying the specified options.

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
init(localized resource: LocalizedStringResource, options: String.LocalizationOptions)
```

#### Discussion

Call this initializer to look up the localization that `resource` indicates from a string catalog or `strings` file in your app bundle. Alter the resource’s `locale` prior to calling this method if you want to localize this string in a different locale than the process that creates the `LocalizedStringResource`.

```swift
// Assume the string catalog contains "Hello, world!" for English
// and "Bonjour, le monde!" for French.
var localizable = LocalizedStringResource("Hello, world!")
// Potentially using localizable in another process…
localizable.locale = Locale(identifier: "en")
let enLocalized = String(localized: localizable)
localizable.locale = Locale(identifier: "fr")
let frLocalized = String(localized: localizable)
// enLocalized == "Hello, world!"
// frLocalized == "Bonjour, le monde!"
```

Use the `options` parameter to include any replacement values to insert into the localized formatted string. The formatted string uses the syntax `\(placeholder: TYPE)` to strongly type replacement values. The following example shows how to insert strongly typed replacement values into a string:

```swift
// Assume the strings file or catalog contains "Position in queue: %lld."
// for English and "Position dans la file d’attente: %lld." for French.
var localizable = LocalizedStringResource("Position in queue: \(placeholder: .int).")
// Potentially using localizable in another process…
var options = String.LocalizationOptions()
options.replacements = [12]
localizable.locale = Locale(identifier: "en")
let enLocalized = String (localized: localizable, options: options)
localizable.locale = Locale(identifier: "fr")
let frLocalized = String (localized: localizable, options: options)
// enLocalized == "Position in queue: 12."
// frLocalized == "Position dans la file d’attente: 12."
```

If you don’t need the deferred-loading behavior of `LocalizedStringResource`, use [`init(localized:options:table:bundle:locale:comment:)`](string/init(localized:options:table:bundle:locale:comment:).md) instead. If you prefer to use an arbitrary localization key rather than the localized string in the development language, use [`init(localized:defaultValue:options:table:bundle:locale:comment:)`](string/init(localized:defaultvalue:options:table:bundle:locale:comment:).md).

## Parameters

- `resource`: A   that provides the localization key, table, bundle, and locale.
- `options`: A localization options instance that specifies localization options to apply, such as replacement values for formatted strings.

## See Also

- [init(localized: String.LocalizationValue, table: String?, bundle: Bundle?, locale: Locale, comment: StaticString?)](string/init(localized:table:bundle:locale:comment:).md)
  Creates a localized string from an interpolated string.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/init(localized:options:))*
# init(localized:)

**Framework**: Swift  
**Kind**: init  
**Role**: Initializer

Creates a localized string from a localized string resource.

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
init(localized resource: LocalizedStringResource)
```

## Discussion

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

If you don’t need the deferred-loading behavior of `LocalizedStringResource`, use [`init(localized:table:bundle:locale:comment:)`](./init%28localized,table,bundle,locale,comment%29.md) instead. If you prefer to use an arbitrary localization key rather than the localized string in the development language, use [`init(localized:defaultValue:table:bundle:locale:comment:)`](./init%28localized,defaultvalue,table,bundle,locale,comment%29.md).

## Parameters

- `resource`: A `LocalizedStringResource` that provides the localization key, table, bundle, and locale.

## See Also

### Creating a Localized String
- [init(localized: String.LocalizationValue, table: String?, bundle: Bundle?, locale: Locale, comment: StaticString?)](./init%28localized,table,bundle,locale,comment%29.md)
  Creates a localized string from an interpolated string.
- [init(localized: String.LocalizationValue, options: String.LocalizationOptions, table: String?, bundle: Bundle?, locale: Locale, comment: StaticString?)](./init%28localized,options,table,bundle,locale,comment%29.md)
  Creates a localized string from an interpolated string, applying the specified options.
- [String.LocalizationValue](./localizationvalue.md)
  A reference to a localizable string, with optional string interpolation.
- [String.LocalizationOptions](./localizationoptions.md)
  Options to apply when initializing a localized string.
- [init(localized: StaticString, defaultValue: String.LocalizationValue, table: String?, bundle: Bundle?, locale: Locale, comment: StaticString?)](./init%28localized,defaultvalue,table,bundle,locale,comment%29.md)
  Creates a localized string from an arbitrary static string key.
- [init(localized: StaticString, defaultValue: String.LocalizationValue, options: String.LocalizationOptions, table: String?, bundle: Bundle?, locale: Locale, comment: StaticString?)](./init%28localized,defaultvalue,options,table,bundle,locale,comment%29.md)
  Creates a localized string from an arbitrary static string key, applying the specified options.
- [init(localized: LocalizedStringResource, options: String.LocalizationOptions)](./init%28localized,options%29.md)
  Creates a localized string from a localized string resource, applying the specified options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/init(localized:))*
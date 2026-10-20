# String.LocalizationOptions

**Framework**: Swift  
**Kind**: struct  
**Role**: Structure

Options to apply when initializing a localized string.

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
struct LocalizationOptions
```

#### Overview

Use this type to configure how the system localizes strings. You can use the [`replacements`](./localizationoptions/replacements.md) property to provide replacement values for localizable strings that use the `\(placeholder:)` syntax.

## Topics

### Specifying localization behavior
- [var replacements: [any CVarArg]?](./localizationoptions/replacements.md)
  An array of replacement options.
### Initializers
- [init()](./localizationoptions/init%28%29.md)

## See Also

### Creating a Localized String
- [init(localized: String.LocalizationValue, table: String?, bundle: Bundle?, locale: Locale, comment: StaticString?)](./init%28localized,table,bundle,locale,comment%29.md)
  Creates a localized string from an interpolated string.
- [init(localized: String.LocalizationValue, options: String.LocalizationOptions, table: String?, bundle: Bundle?, locale: Locale, comment: StaticString?)](./init%28localized,options,table,bundle,locale,comment%29.md)
  Creates a localized string from an interpolated string, applying the specified options.
- [String.LocalizationValue](./localizationvalue.md)
  A reference to a localizable string, with optional string interpolation.
- [init(localized: StaticString, defaultValue: String.LocalizationValue, table: String?, bundle: Bundle?, locale: Locale, comment: StaticString?)](./init%28localized,defaultvalue,table,bundle,locale,comment%29.md)
  Creates a localized string from an arbitrary static string key.
- [init(localized: StaticString, defaultValue: String.LocalizationValue, options: String.LocalizationOptions, table: String?, bundle: Bundle?, locale: Locale, comment: StaticString?)](./init%28localized,defaultvalue,options,table,bundle,locale,comment%29.md)
  Creates a localized string from an arbitrary static string key, applying the specified options.
- [init(localized: LocalizedStringResource)](./init%28localized%29.md)
  Creates a localized string from a localized string resource.
- [init(localized: LocalizedStringResource, options: String.LocalizationOptions)](./init%28localized,options%29.md)
  Creates a localized string from a localized string resource, applying the specified options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/localizationoptions)*
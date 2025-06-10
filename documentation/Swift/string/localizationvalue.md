# String.LocalizationValue

**Framework**: Swift  
**Kind**: struct

A reference to a localizable string, with optional string interpolation.

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
struct LocalizationValue
```

#### Overview

Use this type when the localization key is the localized string value in the development language.  This type also supports creating localized strings that depend on a value you provide at runtime. For example, if your app’s strings catalog contains a localizable entry for `"Hello, \(userName)."`, you create a localized string like the following:

```swift
    let greeting = String(localized: "Hello, \(userName).")
```

If you want to use an arbitary string as your localization key, use [`String`](string.md) initializers that take a [`StaticString`](staticstring.md) and a `defaultValue` parameter, like [`init(localized:defaultValue:table:bundle:locale:comment:)`](string/init(localized:defaultvalue:table:bundle:locale:comment:).md) and [`init(localized:defaultValue:options:table:bundle:locale:comment:)`](string/init(localized:defaultvalue:options:table:bundle:locale:comment:).md).

If you need to provide localized strings to another process that might be using a different locale, initialize with a `LocalizedStringResource`, using [`init(localized:)`](string/init(localized:).md) or [`init(localized:options:)`](string/init(localized:options:).md).

## Topics

### Creating a string localization value instance
- [init(String)](string/localizationvalue/init(_:).md)
  Creates a localization value instance.
### Supporting types
- [String.LocalizationValue.Placeholder](string/localizationvalue/placeholder.md)
  An enumeration of types that can appear as a placeholder in a string interpolation.

## Relationships

### Conforms To
- [Copyable](copyable.md)
- [Decodable](decodable.md)
- [Encodable](encodable.md)
- [Equatable](equatable.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](expressiblebyextendedgraphemeclusterliteral.md)
- [ExpressibleByStringInterpolation](expressiblebystringinterpolation.md)
- [ExpressibleByStringLiteral](expressiblebystringliteral.md)
- [ExpressibleByUnicodeScalarLiteral](expressiblebyunicodescalarliteral.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)

## See Also

- [init(localized: String.LocalizationValue, table: String?, bundle: Bundle?, locale: Locale, comment: StaticString?)](string/init(localized:table:bundle:locale:comment:).md)
  Creates a localized string from an interpolated string.
- [init(localized: String.LocalizationValue, options: String.LocalizationOptions, table: String?, bundle: Bundle?, locale: Locale, comment: StaticString?)](string/init(localized:options:table:bundle:locale:comment:).md)
  Creates a localized string from an interpolated string, applying the specified options.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/localizationvalue)*
# LocalizedStringResource

**Framework**: Foundation  
**Kind**: struct

A reference to a localizable string, accessible from another process.

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
struct LocalizedStringResource
```

#### Overview

Use [`LocalizedStringResource`](localizedstringresource.md) to provide localizable strings with lookups you defer to a later time.

When you create a localized string or a localized attributed string with an initializer that takes [`String.LocalizationValue`](https://developer.apple.com/documentation/Swift/String/LocalizationValue), those initializers lookup the localized string immediately. If you want to perform the lookup at a later time, use this [`LocalizedStringResource`](localizedstringresource.md) type to refer to the localizable strings. Then, when you need to perform localization, create a [`String`](https://developer.apple.com/documentation/Swift/String) or [`AttributedString`](attributedstring.md) from an initializer that takes a [`LocalizedStringResource`](localizedstringresource.md) parameter, such as:

- [`String`](https://developer.apple.com/documentation/Swift/String): [`init(localized:)`](https://developer.apple.com/documentation/Swift/String/init(localized:)) or [`init(localized:options:)`](https://developer.apple.com/documentation/Swift/String/init(localized:options:)).
- [`AttributedString`](attributedstring.md): [`init(localized:)`](attributedstring/init(localized:).md), [`init(localized:including:)`](attributedstring/init(localized:including:)-2xebo.md), or [`init(localized:including:)`](attributedstring/init(localized:including:)-15xc5.md).

This approach allows you to provide localizable strings to an entirely separate process, which may use a different locale. For example, consider an app with a data model type called `UserAction` that uses [`LocalizedStringResource`](localizedstringresource.md) rather than strings for its `title` and `description` properties.

```swift
public protocol UserAction {
    static var title: LocalizedStringResource { get }
    static var description: LocalizedStringResource { get }
}
```

This app (or one of its embedded frameworks) then uses these [`LocalizedStringResource`](localizedstringresource.md) members to defer looking up localized strings. Typically, this happens when calling out to another process over XPC.

```swift
public func perform(action: UserAction) {
    ...
    // Send text to another process via XPC or similar.
    performActionOutOfProcess(title: action.title, description: action.description)
}
```

Then, when the other process receives the call, it can alter the [`locale`](localizedstringresource/locale.md) in the [`LocalizedStringResource`](localizedstringresource.md), prior to resolving the localized strings.

```swift
func performActionOutOfProcess(title: LocalizedStringResource,
                               description: LocalizedStringResource) {
    // Set resource locales to match the current locale
    // of the separate process.
    var fixedTitle = title
    fixedTitle.locale = .current
    var fixedDescription = description
    fixedDescription.locale = .current
    
    // Look up localized strings.
    let titleString = String(localized: fixedTitle)
    let descriptionString = String(localized: fixedDescription)
        
    // Use a correctly localized title/description.
}
```

The [`App Intents`](https://developer.apple.com/documentation/AppIntents) framework uses [`LocalizedStringResource`](localizedstringresource.md) to perform a late resolution of localized strings. This allows the Siri UI to potentially use different localization preferences than the app providing the intent.

## Topics

### Creating a localized string resource
- [init(String.LocalizationValue, table: String?, locale: Locale, bundle: LocalizedStringResource.BundleDescription, comment: StaticString?)](localizedstringresource/init(_:table:locale:bundle:comment:).md)
  Creates a localized string resource from a localization key and its bundle properties.
- [init(StaticString, defaultValue: String.LocalizationValue, table: String?, locale: Locale, bundle: LocalizedStringResource.BundleDescription, comment: StaticString?)](localizedstringresource/init(_:defaultvalue:table:locale:bundle:comment:).md)
  Creates a localized string resource from a static string and its bundle properties.
### Accessing resource properties
- [let key: String](localizedstringresource/key.md)
  The key to use to look up a localized string.
- [let defaultValue: String.LocalizationValue](localizedstringresource/defaultvalue.md)
  The resource’s default value.
- [let table: String?](localizedstringresource/table.md)
  The name of the table containing the key-value pairs.
- [var bundle: LocalizedStringResource.BundleDescription](localizedstringresource/bundle.md)
  The bundle containing the table’s strings file.
- [LocalizedStringResource.BundleDescription](localizedstringresource/bundledescription.md)
  The location of a bundle to use for looking up localized strings, such as the main bundle, or a bundle at a specific file URL.
- [var locale: Locale](localizedstringresource/locale.md)
  The locale to use to look up the localized string from the string resource.

## Relationships

### Conforms To
- [CustomLocalizedStringResourceConvertible](customlocalizedstringresourceconvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](../Swift/ExpressibleByExtendedGraphemeClusterLiteral.md)
- [ExpressibleByStringInterpolation](../Swift/ExpressibleByStringInterpolation.md)
- [ExpressibleByStringLiteral](../Swift/ExpressibleByStringLiteral.md)
- [ExpressibleByUnicodeScalarLiteral](../Swift/ExpressibleByUnicodeScalarLiteral.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct Locale](locale.md)
  Information about linguistic, cultural, and technological conventions for use in formatting data for presentation.
- [class NSOrthography](nsorthography.md)
  A description of the linguistic content of natural language text, typically used for spelling and grammar checking.
- [func NSLocalizedString(String, tableName: String?, bundle: Bundle, value: String, comment: String) -> String](nslocalizedstring(_:tablename:bundle:value:comment:).md)
  Returns a localized string from a table that Xcode generates for you when exporting localizations.
- [protocol CustomLocalizedStringResourceConvertible](customlocalizedstringresourceconvertible.md)
  A type that provides an out-of-process localizable description.
- [struct URLResource](urlresource.md)
  A resource located at a particular file URL within a bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/localizedstringresource)*
# init(_:table:locale:bundle:comment:)

**Framework**: Foundation  
**Kind**: init

Creates a localized string resource from a localization key and its bundle properties.

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
init(_ keyAndValue: String.LocalizationValue, table: String? = nil, locale: Locale = .current, bundle: LocalizedStringResource.BundleDescription = .main, comment: StaticString? = nil)
```

## Parameters

- `keyAndValue`: The key for an entry in the specified table.
- `table`: The name of the table containing the key-value pairs. If not provided,  , or an empty string, this value defaults to 
- `locale`: The locale for the resource to use. By default, the resource uses  .
- `bundle`: A   that indicates where to locate the table’s strings file. By default, the resource uses the main bundle.
- `comment`: The comment to place above the key-value pair in the strings file. This parameter provides the translator with some context about the localized string’s presentation to the user.

## See Also

- [init(StaticString, defaultValue: String.LocalizationValue, table: String?, locale: Locale, bundle: LocalizedStringResource.BundleDescription, comment: StaticString?)](localizedstringresource/init(_:defaultvalue:table:locale:bundle:comment:).md)
  Creates a localized string resource from a static string and its bundle properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/localizedstringresource/init(_:table:locale:bundle:comment:))*
# locale

**Framework**: Foundation  
**Kind**: property

The locale to use to look up the localized string from the string resource.

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
var locale: Locale
```

#### Discussion

To perform localization in a different locale, change this value before passing it to a [`String`](https://developer.apple.com/documentation/Swift/String) or [`AttributedString`](attributedstring.md) initializer that takes a [`LocalizedStringResource`](localizedstringresource.md).

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/localizedstringresource/locale)*
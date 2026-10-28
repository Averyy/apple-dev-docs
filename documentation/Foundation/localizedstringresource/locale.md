# locale

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

## Discussion

To perform localization in a different locale, change this value before passing it to a [`String`](../../Swift/string.md) or [`AttributedString`](../attributedstring.md) initializer that takes a [`LocalizedStringResource`](../localizedstringresource.md).

## See Also

### Accessing resource properties
- [let key: String](./key.md)
  The key to use to look up a localized string.
- [let defaultValue: String.LocalizationValue](./defaultvalue.md)
  The resource’s default value.
- [let table: String?](./table.md)
  The name of the table containing the key-value pairs.
- [var bundle: LocalizedStringResource.BundleDescription](./bundle.md)
  The bundle containing the table’s strings file.
- [LocalizedStringResource.BundleDescription](./bundledescription.md)
  The location of a bundle to use for looking up localized strings, such as the main bundle, or a bundle at a specific file URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/localizedstringresource/locale)*
# LocalizedStringResource.BundleDescription

**Framework**: Foundation  
**Kind**: enum

The location of a bundle to use for looking up localized strings, such as the main bundle, or a bundle at a specific file URL.

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
enum BundleDescription
```

## Topics

### Bundle descriptions
- [LocalizedStringResource.BundleDescription.main](localizedstringresource/bundledescription/main.md)
  The app’s main bundle.
- [LocalizedStringResource.BundleDescription.atURL(_:)](localizedstringresource/bundledescription/aturl(_:).md)
  A bundle located at a specific file URL.
- [LocalizedStringResource.BundleDescription.forClass(_:)](localizedstringresource/bundledescription/forclass(_:).md)
  The bundle for a specific class.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [let key: String](localizedstringresource/key.md)
  The key to use to look up a localized string.
- [let defaultValue: String.LocalizationValue](localizedstringresource/defaultvalue.md)
  The resource’s default value.
- [let table: String?](localizedstringresource/table.md)
  The name of the table containing the key-value pairs.
- [var bundle: LocalizedStringResource.BundleDescription](localizedstringresource/bundle.md)
  The bundle containing the table’s strings file.
- [var locale: Locale](localizedstringresource/locale.md)
  The locale to use to look up the localized string from the string resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/localizedstringresource/bundledescription)*
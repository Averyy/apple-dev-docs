# bundle

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The bundle containing the table’s strings file.

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
var bundle: LocalizedStringResource.BundleDescription { get }
```

## See Also

### Accessing resource properties
- [let key: String](./key.md)
  The key to use to look up a localized string.
- [let defaultValue: String.LocalizationValue](./defaultvalue.md)
  The resource’s default value.
- [let table: String?](./table.md)
  The name of the table containing the key-value pairs.
- [LocalizedStringResource.BundleDescription](./bundledescription.md)
  The location of a bundle to use for looking up localized strings, such as the main bundle, or a bundle at a specific file URL.
- [var locale: Locale](./locale.md)
  The locale to use to look up the localized string from the string resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/localizedstringresource/bundle)*
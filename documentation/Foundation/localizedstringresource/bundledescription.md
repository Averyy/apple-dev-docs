# LocalizedStringResource.BundleDescription

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

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
- [LocalizedStringResource.BundleDescription.main](./bundledescription/main.md)
  The app’s main bundle.
- [LocalizedStringResource.BundleDescription.atURL(_:)](./bundledescription/aturl%28_%29.md)
  A bundle located at a specific file URL.
- [LocalizedStringResource.BundleDescription.forClass(_:)](./bundledescription/forclass%28_%29.md)
  The bundle for a specific class.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

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
- [var locale: Locale](./locale.md)
  The locale to use to look up the localized string from the string resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/localizedstringresource/bundledescription)*
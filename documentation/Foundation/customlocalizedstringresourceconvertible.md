# CustomLocalizedStringResourceConvertible

**Framework**: Foundation  
**Kind**: protocol

A type that provides an out-of-process localizable description.

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
protocol CustomLocalizedStringResourceConvertible
```

#### Overview

Similar to [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible), types that conform to [`CustomLocalizedStringResourceConvertible`](customlocalizedstringresourceconvertible.md) provide their own representation when converting to a string instance. Whereas [`CustomStringConvertible`](https://developer.apple.com/documentation/Swift/CustomStringConvertible) provides a [`description`](https://developer.apple.com/documentation/Swift/CustomStringConvertible/description) string, this type offers a [`LocalizedStringResource`](localizedstringresource.md). This allows out-of-process callers to create a localized description from the resource, possibly in a different locale than the current process uses.

## Topics

### Describing a resource
- [var localizedStringResource: LocalizedStringResource](customlocalizedstringresourceconvertible/localizedstringresource.md)
  A resource that helps provide a description of this instance.

## Relationships

### Conforming Types
- [LocalizedStringResource](localizedstringresource.md)

## See Also

- [struct Locale](locale.md)
  Information about linguistic, cultural, and technological conventions for use in formatting data for presentation.
- [class NSOrthography](nsorthography.md)
  A description of the linguistic content of natural language text, typically used for spelling and grammar checking.
- [func NSLocalizedString(String, tableName: String?, bundle: Bundle, value: String, comment: String) -> String](nslocalizedstring(_:tablename:bundle:value:comment:).md)
  Returns a localized string from a table that Xcode generates for you when exporting localizations.
- [struct LocalizedStringResource](localizedstringresource.md)
  A reference to a localizable string, accessible from another process.
- [struct URLResource](urlresource.md)
  A resource located at a particular file URL within a bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/customlocalizedstringresourceconvertible)*
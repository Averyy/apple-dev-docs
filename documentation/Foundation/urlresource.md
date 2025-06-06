# URLResource

**Framework**: Foundation  
**Kind**: struct

A resource located at a particular file URL within a bundle.

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
struct URLResource
```

#### Overview

This type is similar to [`LocalizedStringResource`](localizedstringresource.md) in its ability to provide access to a resource in a bundle, possibly from another process. Use the [`URL`](url.md) initializer [`init(resource:)`](url/init(resource:).md) to resolve the resource.

## Topics

### Creating a URL resource
- [init(name: String, subdirectory: String?, locale: Locale, bundle: Bundle)](urlresource/init(name:subdirectory:locale:bundle:).md)
  Creates a URL resource from the given bundle, name, and subdirectory, optionally specifying a locale.
### Accessing resource properties
- [let bundle: Bundle](urlresource/bundle.md)
  The bundle containing the resource.
- [let name: String](urlresource/name.md)
  The name of the resource in the bundle.
- [let subdirectory: String?](urlresource/subdirectory.md)
  The subdirectory, if any, of the resource.
- [var locale: Locale](urlresource/locale.md)
  The bundle containing the resource.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct Locale](locale.md)
  Information about linguistic, cultural, and technological conventions for use in formatting data for presentation.
- [class NSOrthography](nsorthography.md)
  A description of the linguistic content of natural language text, typically used for spelling and grammar checking.
- [func NSLocalizedString(String, tableName: String?, bundle: Bundle, value: String, comment: String) -> String](nslocalizedstring(_:tablename:bundle:value:comment:).md)
  Returns a localized string from a table that Xcode generates for you when exporting localizations.
- [struct LocalizedStringResource](localizedstringresource.md)
  A reference to a localizable string, accessible from another process.
- [protocol CustomLocalizedStringResourceConvertible](customlocalizedstringresourceconvertible.md)
  A type that provides an out-of-process localizable description.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlresource)*
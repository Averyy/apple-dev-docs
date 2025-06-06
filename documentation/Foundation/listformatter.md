# ListFormatter

**Framework**: Foundation  
**Kind**: class

An object that provides locale-correct formatting of a list of items using the appropriate separator and conjunction.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class ListFormatter
```

#### Overview

The list formatter isn’t aware of the context where the formatted string will be used and doesn’t provide capitalization customization of the list items. The formatted result may not be grammatically correct if placed in a sentence, and it should only be used in a standalone manner.

## Topics

### Converting Arrays to Formatted Lists
- [func string(from: [Any]) -> String?](listformatter/string(from:).md)
  Creates a formatted string for an array of items.
- [func string(for: Any?) -> String?](listformatter/string(for:).md)
  Creates a formatted string for an array of items.
- [class func localizedString(byJoining: [String]) -> String](listformatter/localizedstring(byjoining:).md)
  Constructs a formatted string from an array of strings that uses the list format specific to the current locale.
### Configuring Formatter Options
- [var itemFormatter: Formatter?](listformatter/itemformatter.md)
  An object that formats each item in the list.
- [var locale: Locale!](listformatter/locale.md)
  The locale to use when formatting items in the list.

## Relationships

### Inherits From
- [Formatter](formatter.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](nscoding.md)
- [NSCopying](nscopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/listformatter)*
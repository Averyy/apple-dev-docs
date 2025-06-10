# ByteCountFormatter

**Framework**: Foundation  
**Kind**: class

A formatter that converts a byte count value into a localized description that is formatted with the appropriate byte modifier (KB, MB, GB and so on).

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class ByteCountFormatter
```

#### Overview

> 💡 **Tip**:  In Swift, you can use [`ByteCountFormatStyle`](bytecountformatstyle.md) or [`Measurement.FormatStyle.ByteCount`](measurement/formatstyle/bytecount.md) rather than [`ByteCountFormatter`](bytecountformatter.md). The [`FormatStyle`](formatstyle.md) API offers a declarative idiom for customizing the formatting of various types. Also, Foundation caches identical [`FormatStyle`](formatstyle.md) instances, so you don’t need to pass them around your app, or risk wasting memory with duplicate formatters.

## Topics

### Creating Strings from Byte Count
- [class func string(fromByteCount: Int64, countStyle: ByteCountFormatter.CountStyle) -> String](bytecountformatter/string(frombytecount:countstyle:).md)
  Converts a byte count into the specified string format without creating an `NSNumber` object.
- [func string(fromByteCount: Int64) -> String](bytecountformatter/string(frombytecount:).md)
  Converts a byte count into a string without creating an `NSNumber` object.
### Setting Formatting Styles
- [var formattingContext: Formatter.Context](bytecountformatter/formattingcontext.md)
  Specify the formatting context for the formatted string.
- [var countStyle: ByteCountFormatter.CountStyle](bytecountformatter/countstyle-swift.property.md)
  Specify the number of bytes to be used for kilobytes.
- [var allowsNonnumericFormatting: Bool](bytecountformatter/allowsnonnumericformatting.md)
  Determines whether to allow more natural display of some values.
- [var includesActualByteCount: Bool](bytecountformatter/includesactualbytecount.md)
  Determines whether to include the number of bytes after the formatted string.
- [var isAdaptive: Bool](bytecountformatter/isadaptive.md)
  Determines the display style of the size representation.
- [var allowedUnits: ByteCountFormatter.Units](bytecountformatter/allowedunits.md)
  Specify the units that can be used in the output.
- [var includesCount: Bool](bytecountformatter/includescount.md)
  Determines whether to include the count in the resulting formatted string.
- [var includesUnit: Bool](bytecountformatter/includesunit.md)
  Determines whether to include the units in the resulting formatted string.
- [var zeroPadsFractionDigits: Bool](bytecountformatter/zeropadsfractiondigits.md)
  Determines whether to zero pad fraction digits so a consistent number of characters is displayed in a representation.
### Constants
- [ByteCountFormatter.Units](bytecountformatter/units.md)
  Specifies the units appropriate for the formatter to display. Specifying any units explicitly causes just those units to be used in showing the number.
- [ByteCountFormatter.CountStyle](bytecountformatter/countstyle-swift.enum.md)
  Specifies display of file or storage byte counts. The display style is platform specific.
### Instance Methods
- [func string(for: Any?) -> String?](bytecountformatter/string(for:).md)
- [func string(from: Measurement<UnitInformationStorage>) -> String](bytecountformatter/string(from:).md)
### Type Methods
- [class func string(from: Measurement<UnitInformationStorage>, countStyle: ByteCountFormatter.CountStyle) -> String](bytecountformatter/string(from:countstyle:).md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bytecountformatter)*
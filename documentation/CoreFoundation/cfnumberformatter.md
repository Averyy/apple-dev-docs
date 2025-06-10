# CFNumberFormatter

**Framework**: Core Foundation  
**Kind**: class

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class CFNumberFormatter
```

#### Overview

CFNumberFormatter objects format the textual representations of CFNumber objects, and convert textual representations of numbers into CFNumber objects. The representation encompasses integers, floats, and doubles; floats and doubles can be formatted to a specified decimal position. You specify how strings are formatted and parsed by setting a format string and other properties of a CFNumberFormatter object.

The format of the format string is defined by Unicode Technical Standard #35; the version of the standard used varies with release of the operating system, and is described in [`Introduction to Data Formatting Programming Guide For Cocoa`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DataFormatting/DataFormatting.html#//apple_ref/doc/uid/10000029).

> ❗ **Important**:  `CFNumberFormatter` is not thread-safe.  Do not use a single instance from multiple threads.

Unlike some other Core Foundation opaque types with names similar to a corresponding Cocoa Foundation class (such as CFString and `NSString`), CFNumberFormatter objects cannot be cast (“toll-free bridged”) to `NSNumberFormatter` objects.

## Topics

### Creating a Number Formatter
- [func CFNumberFormatterCreate(CFAllocator!, CFLocale!, CFNumberFormatterStyle) -> CFNumberFormatter!](cfnumberformattercreate(_:_:_:).md)
  Creates a new CFNumberFormatter object, localized to the given locale, which will format numbers to the given style.
### Configuring a Number Formatter
- [func CFNumberFormatterSetFormat(CFNumberFormatter!, CFString!)](cfnumberformattersetformat(_:_:).md)
  Sets the format string of a number formatter.
- [func CFNumberFormatterSetProperty(CFNumberFormatter!, CFNumberFormatterKey!, CFTypeRef!)](cfnumberformattersetproperty(_:_:_:).md)
  Sets a number formatter property using a key-value pair.
### Formatting Values
- [func CFNumberFormatterCreateNumberFromString(CFAllocator!, CFNumberFormatter!, CFString!, UnsafeMutablePointer<CFRange>!, CFOptionFlags) -> CFNumber!](cfnumberformattercreatenumberfromstring(_:_:_:_:_:).md)
  Returns a number object representing a given string.
- [func CFNumberFormatterCreateStringWithNumber(CFAllocator!, CFNumberFormatter!, CFNumber!) -> CFString!](cfnumberformattercreatestringwithnumber(_:_:_:).md)
  Returns a string representation of the given number using the specified number formatter.
- [func CFNumberFormatterCreateStringWithValue(CFAllocator!, CFNumberFormatter!, CFNumberType, UnsafeRawPointer!) -> CFString!](cfnumberformattercreatestringwithvalue(_:_:_:_:).md)
  Returns a string representation of the given number or value using the specified number formatter.
- [func CFNumberFormatterGetDecimalInfoForCurrencyCode(CFString!, UnsafeMutablePointer<Int32>!, UnsafeMutablePointer<Double>!) -> Bool](cfnumberformattergetdecimalinfoforcurrencycode(_:_:_:).md)
  Returns the number of fraction digits that should be displayed, and the rounding increment, for a given currency.
- [func CFNumberFormatterGetValueFromString(CFNumberFormatter!, CFString!, UnsafeMutablePointer<CFRange>!, CFNumberType, UnsafeMutableRawPointer!) -> Bool](cfnumberformattergetvaluefromstring(_:_:_:_:_:).md)
  Returns a number or value representing a given string.
### Examining a Number Formatter
- [func CFNumberFormatterCopyProperty(CFNumberFormatter!, CFNumberFormatterKey!) -> CFTypeRef!](cfnumberformattercopyproperty(_:_:).md)
  Returns a copy of a number formatter’s value for a given key.
- [func CFNumberFormatterGetFormat(CFNumberFormatter!) -> CFString!](cfnumberformattergetformat(_:).md)
  Returns a format string for the given number formatter object.
- [func CFNumberFormatterGetLocale(CFNumberFormatter!) -> CFLocale!](cfnumberformattergetlocale(_:).md)
  Returns the locale object used to create the given number formatter object.
- [func CFNumberFormatterGetStyle(CFNumberFormatter!) -> CFNumberFormatterStyle](cfnumberformattergetstyle(_:).md)
  Returns the number style used to create the given number formatter object.
### Getting the CFNumberFormatter Type ID
- [func CFNumberFormatterGetTypeID() -> CFTypeID](cfnumberformattergettypeid().md)
  Returns the type identifier for the `CFNumberFormatter` opaque type.
### Data Types
- [enum CFNumberFormatterStyle](cfnumberformatterstyle.md)
  Type for constants specifying a formatter style.
- [struct CFNumberFormatterOptionFlags](cfnumberformatteroptionflags.md)
  Type for constants specifying how numbers should be parsed.
- [enum CFNumberFormatterPadPosition](cfnumberformatterpadposition.md)
  Type for constants specifying how numbers should be padded.
### Constants
- [Number Formatter Styles](number-formatter-styles.md)
  Predefined number format styles.
- [Number Formatter Property Keys](number-formatter-property-keys.md)
  The keys used in key-value pairs to specify the value of number formatter properties.
- [Number Format Options](number_format_options.md)
  These constants are used to specify how numbers should be parsed.
- [enum CFNumberFormatterRoundingMode](cfnumberformatterroundingmode.md)
  These constants are used to specify how numbers should be rounded.
- [Padding Positions](padding-positions.md)
  These constants are used to specify how numbers should be padded.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [Data Formatting Guide for Core Foundation](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDataFormatting/Articles/CFDataFormatting.html#//apple_ref/doc/uid/10000176i)
- [class CFAllocator](cfallocator.md)
- [class CFArray](cfarray.md)
- [class CFAttributedString](cfattributedstring.md)
- [class CFBag](cfbag.md)
- [class CFBinaryHeap](cfbinaryheap.md)
- [class CFBitVector](cfbitvector.md)
- [class CFBoolean](cfboolean.md)
- [class CFBundle](cfbundle.md)
- [class CFCalendar](cfcalendar.md)
- [class CFCharacterSet](cfcharacterset.md)
- [class CFData](cfdata.md)
- [class CFDate](cfdate.md)
- [class CFDateFormatter](cfdateformatter.md)
- [class CFDictionary](cfdictionary.md)
- [class CFError](cferror.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfnumberformatter)*
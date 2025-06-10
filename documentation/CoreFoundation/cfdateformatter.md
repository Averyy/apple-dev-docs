# CFDateFormatter

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
class CFDateFormatter
```

#### Overview

CFDateFormatter objects format the textual representations of CFDate and CFAbsoluteTime objects, and convert textual representations of dates and times into CFDate and CFAbsoluteTime objects. You can express the representation of dates and times very flexibly, for example “Thu 22 Dec 1994” is just as acceptable as “12/22/94.” You specify how strings are formatted and parsed by setting a format string and other properties of a CFDateFomatter object.

The format of the format string itself is defined by Unicode Technical Standard #35; the version of the standard used varies with release of the operating system, and is described in [`Introduction to Data Formatting Programming Guide For Cocoa`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DataFormatting/DataFormatting.html#//apple_ref/doc/uid/10000029).

> **Note**:  CFDateFormatter is not thread safe, so you must not mutate a given date formatter simultaneously from multiple threads.

## Topics

### Creating a Date Formatter
- [func CFDateFormatterCreate(CFAllocator!, CFLocale!, CFDateFormatterStyle, CFDateFormatterStyle) -> CFDateFormatter!](cfdateformattercreate(_:_:_:_:).md)
  Creates a new CFDateFormatter object, localized to the given locale, which will format dates to the given date and time styles.
### Configuring a Date Formatter
- [func CFDateFormatterSetFormat(CFDateFormatter!, CFString!)](cfdateformattersetformat(_:_:).md)
  Sets the format string of the given date formatter to the specified value.
- [func CFDateFormatterSetProperty(CFDateFormatter!, CFString!, CFTypeRef!)](cfdateformattersetproperty(_:_:_:).md)
  Sets a date formatter property using a key-value pair.
### Parsing Strings
- [func CFDateFormatterCreateDateFromString(CFAllocator!, CFDateFormatter!, CFString!, UnsafeMutablePointer<CFRange>!) -> CFDate!](cfdateformattercreatedatefromstring(_:_:_:_:).md)
  Returns a date object representing a given string.
- [func CFDateFormatterGetAbsoluteTimeFromString(CFDateFormatter!, CFString!, UnsafeMutablePointer<CFRange>!, UnsafeMutablePointer<CFAbsoluteTime>!) -> Bool](cfdateformattergetabsolutetimefromstring(_:_:_:_:).md)
  Returns an absolute time object representing a given string.
### Creating Strings From Data
- [func CFDateFormatterCreateStringWithAbsoluteTime(CFAllocator!, CFDateFormatter!, CFAbsoluteTime) -> CFString!](cfdateformattercreatestringwithabsolutetime(_:_:_:).md)
  Returns a string representation of the given absolute time using the specified date formatter.
- [func CFDateFormatterCreateStringWithDate(CFAllocator!, CFDateFormatter!, CFDate!) -> CFString!](cfdateformattercreatestringwithdate(_:_:_:).md)
  Returns a string representation of the given date using the specified date formatter.
- [func CFDateFormatterCreateDateFormatFromTemplate(CFAllocator!, CFString!, CFOptionFlags, CFLocale!) -> CFString!](cfdateformattercreatedateformatfromtemplate(_:_:_:_:).md)
  Returns a localized date format string representing the given date format components arranged appropriately for the specified locale.
### Getting Information About a Date Formatter
- [func CFDateFormatterCopyProperty(CFDateFormatter!, CFDateFormatterKey!) -> CFTypeRef!](cfdateformattercopyproperty(_:_:).md)
  Returns a copy of a date formatter’s value for a given key.
- [func CFDateFormatterGetDateStyle(CFDateFormatter!) -> CFDateFormatterStyle](cfdateformattergetdatestyle(_:).md)
  Returns the date style used to create the given date formatter object.
- [func CFDateFormatterGetFormat(CFDateFormatter!) -> CFString!](cfdateformattergetformat(_:).md)
  Returns a format string for the given date formatter object.
- [func CFDateFormatterGetLocale(CFDateFormatter!) -> CFLocale!](cfdateformattergetlocale(_:).md)
  Returns the locale object used to create the given date formatter object.
- [func CFDateFormatterGetTimeStyle(CFDateFormatter!) -> CFDateFormatterStyle](cfdateformattergettimestyle(_:).md)
  Returns the time style used to create the given date formatter object.
### Getting the CFDateFormatter Type ID
- [func CFDateFormatterGetTypeID() -> CFTypeID](cfdateformattergettypeid().md)
  Returns the type identifier for CFDateFormatter.
### Data Types
- [enum CFDateFormatterStyle](cfdateformatterstyle.md)
  Data type for predefined date and time format styles.
### Constants
- [Date Formatter Styles](date_formatter_styles.md)
  Predefined date and time format styles.
- [Date Formatter Property Keys](date-formatter-property-keys.md)
  Keys used in key-value pairs to discover and specify the value of date formatter properties—used in conjunction with [`CFDateFormatterCopyProperty(_:_:)`](cfdateformattercopyproperty(_:_:).md) and [`CFDateFormatterSetProperty(_:_:_:)`](cfdateformattersetproperty(_:_:_:).md).
- [Calendar Names](calendar-names.md)
  Calendar names used by CFDateFormatter.

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
- [class CFDictionary](cfdictionary.md)
- [class CFError](cferror.md)
- [class CFFileDescriptor](cffiledescriptor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdateformatter)*
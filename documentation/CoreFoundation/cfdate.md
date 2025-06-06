# CFDate

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
class CFDate
```

#### Overview

`CFDate` objects store dates and times that can be compared to other dates and times. `CFDate` objects are immutable—there is no mutable counterpart for this opaque type.

`CFDate` provides functions for creating dates, comparing dates, and computing intervals. You use the [`CFDateCreate(_:_:)`](cfdatecreate(_:_:).md) function to create `CFDate` objects. You use the [`CFDateCompare(_:_:_:)`](cfdatecompare(_:_:_:).md) function to compare two dates, and the [`CFDateGetTimeIntervalSinceDate(_:_:)`](cfdategettimeintervalsincedate(_:_:).md) function to compute a time interval. Additional functions for managing dates and times are described in [`Time Utilities`](time-utilities.md)

`CFDate` is “toll-free bridged” with its Cocoa Foundation counterpart, [`NSDate`](https://developer.apple.com/documentation/Foundation/NSDate). What this means is that the Core Foundation type is interchangeable in function or method calls with the bridged Foundation object. In other words, in a method where you see an `NSDate *` parameter, you can pass in a `CFDateRef`, and in a function where you see a `CFDateRef` parameter, you can pass in an `NSDate` instance. This also applies to concrete subclasses of `NSDate`. See Interchangeable Data Types for more information on toll-free bridging.

## Topics

### CFDate Miscellaneous Functions
- [func CFDateCompare(CFDate!, CFDate!, UnsafeMutableRawPointer!) -> CFComparisonResult](cfdatecompare(_:_:_:).md)
  Compares two `CFDate` objects and returns a comparison result.
- [func CFDateCreate(CFAllocator!, CFAbsoluteTime) -> CFDate!](cfdatecreate(_:_:).md)
  Creates a `CFDate` object given an absolute time.
- [func CFDateGetAbsoluteTime(CFDate!) -> CFAbsoluteTime](cfdategetabsolutetime(_:).md)
  Returns a `CFDate` object’s absolute time.
- [func CFDateGetTimeIntervalSinceDate(CFDate!, CFDate!) -> CFTimeInterval](cfdategettimeintervalsincedate(_:_:).md)
  Returns the number of elapsed seconds between the given `CFDate` objects.
- [func CFDateGetTypeID() -> CFTypeID](cfdategettypeid().md)
  Returns the type identifier for the `CFDate` opaque type.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [Property List Programming Topics for Core Foundation](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFPropertyLists/CFPropertyLists.html#//apple_ref/doc/uid/10000130i)
- [Date and Time Programming Guide for Core Foundation](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDatesAndTimes/CFDatesAndTimes.html#//apple_ref/doc/uid/10000125i)
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
- [class CFDateFormatter](cfdateformatter.md)
- [class CFDictionary](cfdictionary.md)
- [class CFError](cferror.md)
- [class CFFileDescriptor](cffiledescriptor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfdate)*
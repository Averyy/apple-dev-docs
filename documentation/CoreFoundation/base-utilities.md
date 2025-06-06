# Base Utilities

**Framework**: Core Foundation

#### Overview

Core Foundation defines a number of miscellaneous symbols that are either used by many different opaque types, such as [`CFIndex`](cfindex.md), or apply to Core Foundation as a whole, such as [`kCFCoreFoundationVersionNumber`](kcfcorefoundationversionnumber.md). These symbols are collected together and documented here.

## Topics

### Core Foundation Base Utilities Miscellaneous Functions
- [func CFRangeMake(CFIndex, CFIndex) -> CFRange](cfrangemake(_:_:).md)
  Declares and initializes a `CFRange` structure.
### Callbacks
- [typealias CFComparatorFunction](cfcomparatorfunction.md)
  Callback function that compares two values. You provide a pointer to this callback in certain Core Foundation sorting functions.
### Data Types
- [typealias CFIndex](cfindex.md)
  Priority values used for kAXPriorityKey
- [typealias CFOptionFlags](cfoptionflags.md)
  A bitfield used for passing special allocation and other requests into Core Foundation functions.
- [struct CFRange](cfrange.md)
  A structure representing a range of sequential items in a container, such as characters in a buffer or elements in a collection.
### Constants
- [enum CFComparisonResult](cfcomparisonresult.md)
  Constants returned by comparison functions, indicating whether a value is equal to, less than, or greater than another value.
- [Value Not Found](value-not-found.md)
  Special value returned when a Core Foundation function cannot locate a requested value.
- [Current Framework Version Number](current-framework-version-number.md)
  Current version number of the Core Foundation framework.
- [Framework Version Numbers](framework-version-numbers.md)
  Version numbers of the Core Foundation framework.

## See Also

- [Core Foundation Design Concepts](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDesignConcepts/CFDesignConcepts.html#//apple_ref/doc/uid/10000122i)
- [Byte-Order Utilities](byte-order-utilities.md)
- [Core Foundation URL Access Utilities](core-foundation-url-access-utilities.md)
- [Preferences Utilities](preferences-utilities.md)
- [Socket Name Server Utilities](socket-name-server-utilities.md)
- [Time Utilities](time-utilities.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/base-utilities)*
# CFNumber

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
class CFNumber
```

#### Overview

CFNumber encapsulates C scalar (numeric) types. It provides functions for setting and accessing the value as any basic C type. It also provides a compare function to determine the ordering of two CFNumber objects. CFNumber objects are used to wrap numerical values for use in Core Foundation property lists and collections.

CFNumber objects are not intended as a replacement for C scalar values and should not be used in APIs or implementations where scalar values are more appropriate and efficient.

> **Note**:  In order to improve performance, some commonly-used numbers (such as `0` and `1`) are uniqued. You should not expect that allocating multiple CFNumber instances will necessarily result in distinct objects.

 In order to improve performance, some commonly-used numbers (such as `0` and `1`) are uniqued. You should not expect that allocating multiple CFNumber instances will necessarily result in distinct objects.

CFNumber is “toll-free bridged” with its Cocoa Foundation counterpart, [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber). This means that the Core Foundation type is interchangeable in function or method calls with the bridged Foundation object. Therefore, in a method where you see an `NSNumber *` parameter, you can pass in a `CFNumberRef`, and in a function where you see a `CFNumberRef` parameter, you can pass in an NSNumber instance. This fact also applies to concrete subclasses of NSNumber. See [`Toll-Free Bridged Types`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDesignConcepts/Articles/tollFreeBridgedTypes.html#//apple_ref/doc/uid/TP40010677) for more information on toll-free bridging.

## Topics

### Creating a Number
- [func CFNumberCreate(CFAllocator!, CFNumberType, UnsafeRawPointer!) -> CFNumber!](cfnumbercreate(_:_:_:).md)
  Creates a CFNumber object using a specified value.
### Getting Information About Numbers
- [func CFNumberGetByteSize(CFNumber!) -> CFIndex](cfnumbergetbytesize(_:).md)
  Returns the number of bytes used by a CFNumber object to store its value.
- [func CFNumberGetType(CFNumber!) -> CFNumberType](cfnumbergettype(_:).md)
  Returns the type used by a CFNumber object to store its value.
- [func CFNumberGetValue(CFNumber!, CFNumberType, UnsafeMutableRawPointer!) -> Bool](cfnumbergetvalue(_:_:_:).md)
  Obtains the value of a CFNumber object cast to a specified type.
- [func CFNumberIsFloatType(CFNumber!) -> Bool](cfnumberisfloattype(_:).md)
  Determines whether a CFNumber object contains a value stored as one of the defined floating point types.
### Comparing Numbers
- [func CFNumberCompare(CFNumber!, CFNumber!, UnsafeMutableRawPointer!) -> CFComparisonResult](cfnumbercompare(_:_:_:).md)
  Compares two CFNumber objects and returns a comparison result.
### Getting the CFNumber Type ID
- [func CFNumberGetTypeID() -> CFTypeID](cfnumbergettypeid().md)
  Returns the type identifier for the CFNumber opaque type.
### Constants
- [enum CFNumberType](cfnumbertype.md)
  Flags used by CFNumber to indicate the data type of a value.
- [Predefined Values](predefined-values.md)
  CFNumber provides some predefined number values.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [Property List Programming Topics for Core Foundation](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFPropertyLists/CFPropertyLists.html#//apple_ref/doc/uid/10000130i)
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

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfnumber)*
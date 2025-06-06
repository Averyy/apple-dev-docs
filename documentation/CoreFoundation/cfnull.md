# CFNull

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
class CFNull
```

#### Overview

The CFNull opaque type defines a unique object used to represent null values in collection objects (which don’t allow `NULL` values). CFNull objects are neither created nor destroyed. Instead, a single CFNull constant object—[`kCFNull`](kcfnull.md)—is defined and is used wherever a null value is needed.

The CFNull opaque type is available in macOS 10.2 and later.

## Topics

### CFNull Miscellaneous Functions
- [func CFNullGetTypeID() -> CFTypeID](cfnullgettypeid().md)
  Returns the type identifier for the CFNull opaque type.
### Constants
- [Predefined Value](predefined-value.md)
  Predefined CFNull object.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [Collections Programming Topics for Core Foundation](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFCollections/CFCollections.html#//apple_ref/doc/uid/10000124i)
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

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfnull)*
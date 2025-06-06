# CFBitVector

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
class CFBitVector
```

#### Overview

CFBitVector and its derived mutable type, [`CFMutableBitVector`](cfmutablebitvector.md), manage ordered collections of bit values, which are either `0` or `1`. CFBitVector creates static bit vectors and CFMutableBitVector creates dynamic bit vectors.

## Topics

### Creating a Bit Vector
- [func CFBitVectorCreate(CFAllocator!, UnsafePointer<UInt8>!, CFIndex) -> CFBitVector!](cfbitvectorcreate(_:_:_:).md)
  Creates an immutable bit vector from a block of memory.
- [func CFBitVectorCreateCopy(CFAllocator!, CFBitVector!) -> CFBitVector!](cfbitvectorcreatecopy(_:_:).md)
  Creates an immutable bit vector that is a copy of another bit vector.
### Getting Information About a Bit Vector
- [func CFBitVectorContainsBit(CFBitVector!, CFRange, CFBit) -> Bool](cfbitvectorcontainsbit(_:_:_:).md)
  Returns whether a bit vector contains a particular bit value.
- [func CFBitVectorGetBitAtIndex(CFBitVector!, CFIndex) -> CFBit](cfbitvectorgetbitatindex(_:_:).md)
  Returns the bit value at a given index in a bit vector.
- [func CFBitVectorGetBits(CFBitVector!, CFRange, UnsafeMutablePointer<UInt8>!)](cfbitvectorgetbits(_:_:_:).md)
  Returns the bit values in a range of indices in a bit vector.
- [func CFBitVectorGetCount(CFBitVector!) -> CFIndex](cfbitvectorgetcount(_:).md)
  Returns the number of bit values in a bit vector.
- [func CFBitVectorGetCountOfBit(CFBitVector!, CFRange, CFBit) -> CFIndex](cfbitvectorgetcountofbit(_:_:_:).md)
  Counts the number of times a certain bit value occurs within a range of bits in a bit vector.
- [func CFBitVectorGetFirstIndexOfBit(CFBitVector!, CFRange, CFBit) -> CFIndex](cfbitvectorgetfirstindexofbit(_:_:_:).md)
  Locates the first occurrence of a certain bit value within a range of bits in a bit vector.
- [func CFBitVectorGetLastIndexOfBit(CFBitVector!, CFRange, CFBit) -> CFIndex](cfbitvectorgetlastindexofbit(_:_:_:).md)
  Locates the last occurrence of a certain bit value within a range of bits in a bit vector.
### Getting the CFBitVector Type ID
- [func CFBitVectorGetTypeID() -> CFTypeID](cfbitvectorgettypeid().md)
  Returns the type identifier for the CFBitVector opaque type.
### Data Types
- [typealias CFBit](cfbit.md)
  A binary value of either `0` or `1`.

## Relationships

### Inherited By
- [CFMutableBitVector](cfmutablebitvector.md)
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
- [class CFBoolean](cfboolean.md)
- [class CFBundle](cfbundle.md)
- [class CFCalendar](cfcalendar.md)
- [class CFCharacterSet](cfcharacterset.md)
- [class CFData](cfdata.md)
- [class CFDate](cfdate.md)
- [class CFDateFormatter](cfdateformatter.md)
- [class CFDictionary](cfdictionary.md)
- [class CFError](cferror.md)
- [class CFFileDescriptor](cffiledescriptor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbitvector)*
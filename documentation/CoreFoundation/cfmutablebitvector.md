# CFMutableBitVector

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
class CFMutableBitVector
```

#### Overview

CFMutableBitVector objects manage dynamic bit vectors. The basic interface for managing bit vectors is provided by [`CFBitVector`](cfbitvector.md). CFMutableBitVector adds functions to modify the contents of a bit vector.

You create a mutable bit vector object using either the [`CFBitVectorCreateMutable(_:_:)`](cfbitvectorcreatemutable(_:_:).md) or [`CFBitVectorCreateMutableCopy(_:_:_:)`](cfbitvectorcreatemutablecopy(_:_:_:).md) function. You add to and remove from a bit vector by altering the size of the bit vector with the [`CFBitVectorSetCount(_:_:)`](cfbitvectorsetcount(_:_:).md) function

## Topics

### Creating a CFMutableBitVector Object
- [func CFBitVectorCreateMutable(CFAllocator!, CFIndex) -> CFMutableBitVector!](cfbitvectorcreatemutable(_:_:).md)
  Creates a mutable bit vector.
- [func CFBitVectorCreateMutableCopy(CFAllocator!, CFIndex, CFBitVector!) -> CFMutableBitVector!](cfbitvectorcreatemutablecopy(_:_:_:).md)
  Creates a new mutable bit vector from a pre-existing bit vector.
### Modifying a Bit Vector
- [func CFBitVectorFlipBitAtIndex(CFMutableBitVector!, CFIndex)](cfbitvectorflipbitatindex(_:_:).md)
  Flips a bit value in a bit vector.
- [func CFBitVectorFlipBits(CFMutableBitVector!, CFRange)](cfbitvectorflipbits(_:_:).md)
  Flips a range of bit values in a bit vector.
- [func CFBitVectorSetAllBits(CFMutableBitVector!, CFBit)](cfbitvectorsetallbits(_:_:).md)
  Sets all bits in a bit vector to a particular value.
- [func CFBitVectorSetBitAtIndex(CFMutableBitVector!, CFIndex, CFBit)](cfbitvectorsetbitatindex(_:_:_:).md)
  Sets the value of a particular bit in a bit vector.
- [func CFBitVectorSetBits(CFMutableBitVector!, CFRange, CFBit)](cfbitvectorsetbits(_:_:_:).md)
  Sets a range of bits in a bit vector to a particular value.
- [func CFBitVectorSetCount(CFMutableBitVector!, CFIndex)](cfbitvectorsetcount(_:_:).md)
  Changes the size of a mutable bit vector.

## Relationships

### Inherits From
- [CFBitVector](cfbitvector.md)
### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

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

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfmutablebitvector)*
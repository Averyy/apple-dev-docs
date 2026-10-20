# CFBitVectorGetBits(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the bit values in a range of indices in a bit vector.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func CFBitVectorGetBits(_ bv: CFBitVector!, _ range: CFRange, _ bytes: UnsafeMutablePointer<UInt8>!)
```

```c
extern void CFBitVectorGetBits(CFBitVectorRef bv, CFRange range, UInt8 *bytes);
```

## Parameters

- `bv`: The bit vector to examine.
- `range`: The range of bit values to return.
- `bytes`: On return, contains the requested bit values from `bv`. This argument must point to enough memory to hold the number of bits requested. The requested bits are left-aligned with the first requested bit stored in the left-most, or most-significant, bit of the byte stream.

## See Also

### Getting Information About a Bit Vector
- [func CFBitVectorContainsBit(CFBitVector!, CFRange, CFBit) -> Bool](./cfbitvectorcontainsbit%28_,_,_%29.md)
  Returns whether a bit vector contains a particular bit value.
- [func CFBitVectorGetBitAtIndex(CFBitVector!, CFIndex) -> CFBit](./cfbitvectorgetbitatindex%28_,_%29.md)
  Returns the bit value at a given index in a bit vector.
- [func CFBitVectorGetCount(CFBitVector!) -> CFIndex](./cfbitvectorgetcount%28_%29.md)
  Returns the number of bit values in a bit vector.
- [func CFBitVectorGetCountOfBit(CFBitVector!, CFRange, CFBit) -> CFIndex](./cfbitvectorgetcountofbit%28_,_,_%29.md)
  Counts the number of times a certain bit value occurs within a range of bits in a bit vector.
- [func CFBitVectorGetFirstIndexOfBit(CFBitVector!, CFRange, CFBit) -> CFIndex](./cfbitvectorgetfirstindexofbit%28_,_,_%29.md)
  Locates the first occurrence of a certain bit value within a range of bits in a bit vector.
- [func CFBitVectorGetLastIndexOfBit(CFBitVector!, CFRange, CFBit) -> CFIndex](./cfbitvectorgetlastindexofbit%28_,_,_%29.md)
  Locates the last occurrence of a certain bit value within a range of bits in a bit vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbitvectorgetbits(_:_:_:))*
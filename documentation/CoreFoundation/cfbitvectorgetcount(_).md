# CFBitVectorGetCount(_:)

**Framework**: Core Foundation  
**Kind**: func

Returns the number of bit values in a bit vector.

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
func CFBitVectorGetCount(_ bv: CFBitVector!) -> CFIndex
```

#### Return Value

The current size of `bv`.

## Parameters

- `bv`: The bit vector to examine.

## See Also

- [func CFBitVectorContainsBit(CFBitVector!, CFRange, CFBit) -> Bool](cfbitvectorcontainsbit(_:_:_:).md)
  Returns whether a bit vector contains a particular bit value.
- [func CFBitVectorGetBitAtIndex(CFBitVector!, CFIndex) -> CFBit](cfbitvectorgetbitatindex(_:_:).md)
  Returns the bit value at a given index in a bit vector.
- [func CFBitVectorGetBits(CFBitVector!, CFRange, UnsafeMutablePointer<UInt8>!)](cfbitvectorgetbits(_:_:_:).md)
  Returns the bit values in a range of indices in a bit vector.
- [func CFBitVectorGetCountOfBit(CFBitVector!, CFRange, CFBit) -> CFIndex](cfbitvectorgetcountofbit(_:_:_:).md)
  Counts the number of times a certain bit value occurs within a range of bits in a bit vector.
- [func CFBitVectorGetFirstIndexOfBit(CFBitVector!, CFRange, CFBit) -> CFIndex](cfbitvectorgetfirstindexofbit(_:_:_:).md)
  Locates the first occurrence of a certain bit value within a range of bits in a bit vector.
- [func CFBitVectorGetLastIndexOfBit(CFBitVector!, CFRange, CFBit) -> CFIndex](cfbitvectorgetlastindexofbit(_:_:_:).md)
  Locates the last occurrence of a certain bit value within a range of bits in a bit vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbitvectorgetcount(_:))*
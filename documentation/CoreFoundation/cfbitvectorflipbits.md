# CFBitVectorFlipBits(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Flips a range of bit values in a bit vector.

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
func CFBitVectorFlipBits(_ bv: CFMutableBitVector!, _ range: CFRange)
```

## Parameters

- `bv`: The bit vector to modify.
- `range`: The range of bit values in   to flip. The range must not exceed  , where   is the count of the vector.

## See Also

- [func CFBitVectorGetCount(CFBitVector!) -> CFIndex](cfbitvectorgetcount(_:).md)
  Returns the number of bit values in a bit vector.
- [func CFBitVectorFlipBitAtIndex(CFMutableBitVector!, CFIndex)](cfbitvectorflipbitatindex(_:_:).md)
  Flips a bit value in a bit vector.
- [func CFBitVectorSetAllBits(CFMutableBitVector!, CFBit)](cfbitvectorsetallbits(_:_:).md)
  Sets all bits in a bit vector to a particular value.
- [func CFBitVectorSetBitAtIndex(CFMutableBitVector!, CFIndex, CFBit)](cfbitvectorsetbitatindex(_:_:_:).md)
  Sets the value of a particular bit in a bit vector.
- [func CFBitVectorSetBits(CFMutableBitVector!, CFRange, CFBit)](cfbitvectorsetbits(_:_:_:).md)
  Sets a range of bits in a bit vector to a particular value.
- [func CFBitVectorSetCount(CFMutableBitVector!, CFIndex)](cfbitvectorsetcount(_:_:).md)
  Changes the size of a mutable bit vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbitvectorflipbits(_:_:))*
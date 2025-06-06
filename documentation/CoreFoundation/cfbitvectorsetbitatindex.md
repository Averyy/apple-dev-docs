# CFBitVectorSetBitAtIndex(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Sets the value of a particular bit in a bit vector.

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
func CFBitVectorSetBitAtIndex(_ bv: CFMutableBitVector!, _ idx: CFIndex, _ value: CFBit)
```

## Parameters

- `bv`: The bit vector to modify.
- `idx`: The index of the bit value to set. The index must be in the range  , where   is the count of the vector.
- `value`: The bit value to which to set the bit at index  .

## See Also

- [func CFBitVectorGetCount(CFBitVector!) -> CFIndex](cfbitvectorgetcount(_:).md)
  Returns the number of bit values in a bit vector.
- [func CFBitVectorFlipBitAtIndex(CFMutableBitVector!, CFIndex)](cfbitvectorflipbitatindex(_:_:).md)
  Flips a bit value in a bit vector.
- [func CFBitVectorFlipBits(CFMutableBitVector!, CFRange)](cfbitvectorflipbits(_:_:).md)
  Flips a range of bit values in a bit vector.
- [func CFBitVectorSetAllBits(CFMutableBitVector!, CFBit)](cfbitvectorsetallbits(_:_:).md)
  Sets all bits in a bit vector to a particular value.
- [func CFBitVectorSetBits(CFMutableBitVector!, CFRange, CFBit)](cfbitvectorsetbits(_:_:_:).md)
  Sets a range of bits in a bit vector to a particular value.
- [func CFBitVectorSetCount(CFMutableBitVector!, CFIndex)](cfbitvectorsetcount(_:_:).md)
  Changes the size of a mutable bit vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbitvectorsetbitatindex(_:_:_:))*
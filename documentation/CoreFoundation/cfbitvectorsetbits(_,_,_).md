# CFBitVectorSetBits(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Sets a range of bits in a bit vector to a particular value.

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
func CFBitVectorSetBits(_ bv: CFMutableBitVector!, _ range: CFRange, _ value: CFBit)
```

```c
extern void CFBitVectorSetBits(CFMutableBitVectorRef bv, CFRange range, CFBit value);
```

## Parameters

- `bv`: The bit vector to modify.
- `range`: The range of bits to set. The range must not exceed `0…N-1`, where `N` is the count of the vector.
- `value`: The bit value to which to set the range of bits.

## See Also

### Related Documentation
- [func CFBitVectorGetCount(CFBitVector!) -> CFIndex](./cfbitvectorgetcount%28_%29.md)
  Returns the number of bit values in a bit vector.
### Modifying a Bit Vector
- [func CFBitVectorFlipBitAtIndex(CFMutableBitVector!, CFIndex)](./cfbitvectorflipbitatindex%28_,_%29.md)
  Flips a bit value in a bit vector.
- [func CFBitVectorFlipBits(CFMutableBitVector!, CFRange)](./cfbitvectorflipbits%28_,_%29.md)
  Flips a range of bit values in a bit vector.
- [func CFBitVectorSetAllBits(CFMutableBitVector!, CFBit)](./cfbitvectorsetallbits%28_,_%29.md)
  Sets all bits in a bit vector to a particular value.
- [func CFBitVectorSetBitAtIndex(CFMutableBitVector!, CFIndex, CFBit)](./cfbitvectorsetbitatindex%28_,_,_%29.md)
  Sets the value of a particular bit in a bit vector.
- [func CFBitVectorSetCount(CFMutableBitVector!, CFIndex)](./cfbitvectorsetcount%28_,_%29.md)
  Changes the size of a mutable bit vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbitvectorsetbits(_:_:_:))*
# CFBitVectorFlipBitAtIndex(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Flips a bit value in a bit vector.

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
func CFBitVectorFlipBitAtIndex(_ bv: CFMutableBitVector!, _ idx: CFIndex)
```

```c
extern void CFBitVectorFlipBitAtIndex(CFMutableBitVectorRef bv, CFIndex idx);
```

## Parameters

- `bv`: The bit vector to modify.
- `idx`: The index of the bit value to flip. The index must be in the range `0…N-1`, where `N` is the count of the vector.

## See Also

### Related Documentation
- [func CFBitVectorGetCount(CFBitVector!) -> CFIndex](./cfbitvectorgetcount%28_%29.md)
  Returns the number of bit values in a bit vector.
### Modifying a Bit Vector
- [func CFBitVectorFlipBits(CFMutableBitVector!, CFRange)](./cfbitvectorflipbits%28_,_%29.md)
  Flips a range of bit values in a bit vector.
- [func CFBitVectorSetAllBits(CFMutableBitVector!, CFBit)](./cfbitvectorsetallbits%28_,_%29.md)
  Sets all bits in a bit vector to a particular value.
- [func CFBitVectorSetBitAtIndex(CFMutableBitVector!, CFIndex, CFBit)](./cfbitvectorsetbitatindex%28_,_,_%29.md)
  Sets the value of a particular bit in a bit vector.
- [func CFBitVectorSetBits(CFMutableBitVector!, CFRange, CFBit)](./cfbitvectorsetbits%28_,_,_%29.md)
  Sets a range of bits in a bit vector to a particular value.
- [func CFBitVectorSetCount(CFMutableBitVector!, CFIndex)](./cfbitvectorsetcount%28_,_%29.md)
  Changes the size of a mutable bit vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbitvectorflipbitatindex(_:_:))*
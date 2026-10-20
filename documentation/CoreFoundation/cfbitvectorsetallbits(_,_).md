# CFBitVectorSetAllBits(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Sets all bits in a bit vector to a particular value.

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
func CFBitVectorSetAllBits(_ bv: CFMutableBitVector!, _ value: CFBit)
```

```c
extern void CFBitVectorSetAllBits(CFMutableBitVectorRef bv, CFBit value);
```

## Parameters

- `bv`: The bit vector to modify.
- `value`: The bit value to which to set all bits in `bv`.

## See Also

### Modifying a Bit Vector
- [func CFBitVectorFlipBitAtIndex(CFMutableBitVector!, CFIndex)](./cfbitvectorflipbitatindex%28_,_%29.md)
  Flips a bit value in a bit vector.
- [func CFBitVectorFlipBits(CFMutableBitVector!, CFRange)](./cfbitvectorflipbits%28_,_%29.md)
  Flips a range of bit values in a bit vector.
- [func CFBitVectorSetBitAtIndex(CFMutableBitVector!, CFIndex, CFBit)](./cfbitvectorsetbitatindex%28_,_,_%29.md)
  Sets the value of a particular bit in a bit vector.
- [func CFBitVectorSetBits(CFMutableBitVector!, CFRange, CFBit)](./cfbitvectorsetbits%28_,_,_%29.md)
  Sets a range of bits in a bit vector to a particular value.
- [func CFBitVectorSetCount(CFMutableBitVector!, CFIndex)](./cfbitvectorsetcount%28_,_%29.md)
  Changes the size of a mutable bit vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbitvectorsetallbits(_:_:))*
# CFBitVectorSetAllBits(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Sets all bits in a bit vector to a particular value.

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
func CFBitVectorSetAllBits(_ bv: CFMutableBitVector!, _ value: CFBit)
```

## Parameters

- `bv`: The bit vector to modify.
- `value`: The bit value to which to set all bits in  .

## See Also

- [func CFBitVectorFlipBitAtIndex(CFMutableBitVector!, CFIndex)](cfbitvectorflipbitatindex(_:_:).md)
  Flips a bit value in a bit vector.
- [func CFBitVectorFlipBits(CFMutableBitVector!, CFRange)](cfbitvectorflipbits(_:_:).md)
  Flips a range of bit values in a bit vector.
- [func CFBitVectorSetBitAtIndex(CFMutableBitVector!, CFIndex, CFBit)](cfbitvectorsetbitatindex(_:_:_:).md)
  Sets the value of a particular bit in a bit vector.
- [func CFBitVectorSetBits(CFMutableBitVector!, CFRange, CFBit)](cfbitvectorsetbits(_:_:_:).md)
  Sets a range of bits in a bit vector to a particular value.
- [func CFBitVectorSetCount(CFMutableBitVector!, CFIndex)](cfbitvectorsetcount(_:_:).md)
  Changes the size of a mutable bit vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbitvectorsetallbits(_:_:))*
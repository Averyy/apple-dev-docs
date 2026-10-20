# CFBitVectorSetCount(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Changes the size of a mutable bit vector.

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
func CFBitVectorSetCount(_ bv: CFMutableBitVector!, _ count: CFIndex)
```

```c
extern void CFBitVectorSetCount(CFMutableBitVectorRef bv, CFIndex count);
```

#### Discussion

If `bv` was created with a fixed capacity, you cannot increase its size beyond that capacity.

## Parameters

- `bv`: The bit vector to modify.
- `count`: The new size for `bv`. If `count` is greater than the current size of `bv`, the additional bit values are set to `0`.

## See Also

### Related Documentation
- [func CFBitVectorCreateMutable(CFAllocator!, CFIndex) -> CFMutableBitVector!](./cfbitvectorcreatemutable%28_,_%29.md)
  Creates a mutable bit vector.
- [func CFBitVectorCreateMutableCopy(CFAllocator!, CFIndex, CFBitVector!) -> CFMutableBitVector!](./cfbitvectorcreatemutablecopy%28_,_,_%29.md)
  Creates a new mutable bit vector from a pre-existing bit vector.
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
- [func CFBitVectorSetBits(CFMutableBitVector!, CFRange, CFBit)](./cfbitvectorsetbits%28_,_,_%29.md)
  Sets a range of bits in a bit vector to a particular value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbitvectorsetcount(_:_:))*
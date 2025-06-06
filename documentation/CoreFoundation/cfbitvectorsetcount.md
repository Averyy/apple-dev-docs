# CFBitVectorSetCount(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Changes the size of a mutable bit vector.

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
func CFBitVectorSetCount(_ bv: CFMutableBitVector!, _ count: CFIndex)
```

#### Discussion

If `bv` was created with a fixed capacity, you cannot increase its size beyond that capacity.

## Parameters

- `bv`: The bit vector to modify.
- `count`: The new size for  . If   is greater than the current size of  , the additional bit values are set to  .

## See Also

- [func CFBitVectorCreateMutable(CFAllocator!, CFIndex) -> CFMutableBitVector!](cfbitvectorcreatemutable(_:_:).md)
  Creates a mutable bit vector.
- [func CFBitVectorCreateMutableCopy(CFAllocator!, CFIndex, CFBitVector!) -> CFMutableBitVector!](cfbitvectorcreatemutablecopy(_:_:_:).md)
  Creates a new mutable bit vector from a pre-existing bit vector.
- [func CFBitVectorGetCount(CFBitVector!) -> CFIndex](cfbitvectorgetcount(_:).md)
  Returns the number of bit values in a bit vector.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbitvectorsetcount(_:_:))*
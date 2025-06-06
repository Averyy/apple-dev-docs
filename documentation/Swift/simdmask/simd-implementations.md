# SIMD Implementations

**Framework**: Swift

## Topics

### Operators
- [static func .!= (Self.Scalar, Self) -> SIMDMask<Self.MaskStorage>](simdmask/'.!=(_:_:)-4o6ac.md)
  Returns a vector mask with the result of a pointwise inequality comparison.
- [static func .!= (Self, Self) -> SIMDMask<Self.MaskStorage>](simdmask/'.!=(_:_:)-5cnom.md)
  A vector mask with the result of a pointwise inequality comparison.
- [static func .!= (Self, Self.Scalar) -> SIMDMask<Self.MaskStorage>](simdmask/'.!=(_:_:)-94n12.md)
  Returns a vector mask with the result of a pointwise inequality comparison.
- [static func .== (Self.Scalar, Self) -> SIMDMask<Self.MaskStorage>](simdmask/'.==(_:_:)-4l749.md)
  Returns a vector mask with the result of a pointwise equality comparison.
- [static func .== (Self, Self.Scalar) -> SIMDMask<Self.MaskStorage>](simdmask/'.==(_:_:)-6aq3z.md)
  Returns a vector mask with the result of a pointwise equality comparison.
- [static func .== (Self, Self) -> SIMDMask<Self.MaskStorage>](simdmask/'.==(_:_:)-8vdyh.md)
  A vector mask with the result of a pointwise equality comparison.
- [static func == (Self, Self) -> Bool](simdmask/==(_:_:).md)
  Returns a Boolean value indicating whether two vectors are equal.
### Initializers
- [init<S>(S)](simdmask/init(_:).md)
  Creates a vector from the given sequence.
- [init(arrayLiteral: Self.Scalar...)](simdmask/init(arrayliteral:).md)
  Creates a vector from the specified elements.
- [init(from: any Decoder) throws](simdmask/init(from:).md)
  Creates a new vector by decoding scalars from the given decoder.
- [init(repeating: Self.Scalar)](simdmask/init(repeating:).md)
  A vector with the specified value in all lanes.
### Instance Properties
- [var description: String](simdmask/description.md)
  A textual description of the vector.
- [var indices: Range<Int>](simdmask/indices.md)
  The valid indices for subscripting the vector.
### Instance Methods
- [func encode(to: any Encoder) throws](simdmask/encode(to:).md)
  Encodes the scalars of this vector into the given encoder in an unkeyed container.
- [func hash(into: inout Hasher)](simdmask/hash(into:).md)
  Hashes the elements of the vector using the given hasher.
- [func replace(with: Self.Scalar, where: SIMDMask<Self.MaskStorage>)](simdmask/replace(with:where:)-6wonx.md)
  Replaces elements of this vector with `other` in the lanes where `mask` is `true`.
- [func replace(with: Self, where: SIMDMask<Self.MaskStorage>)](simdmask/replace(with:where:)-7bhx.md)
  Replaces elements of this vector with elements of `other` in the lanes where `mask` is `true`.
- [func replacing(with: Self, where: SIMDMask<Self.MaskStorage>) -> Self](simdmask/replacing(with:where:)-2gka4.md)
  Returns a copy of this vector, with elements replaced by elements of `other` in the lanes where `mask` is `true`.
- [func replacing(with: Self.Scalar, where: SIMDMask<Self.MaskStorage>) -> Self](simdmask/replacing(with:where:)-3lyjl.md)
  Returns a copy of this vector, with elements `other` in the lanes where `mask` is `true`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/simdmask/simd-implementations)*
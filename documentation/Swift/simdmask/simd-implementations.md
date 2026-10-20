# SIMD Implementations

**Framework**: Swift  
**Role**: API Collection

## Topics

### Operators
- [static func .!= (Self.Scalar, Self) -> SIMDMask<Self.MaskStorage>](./dotnoteq%28_,_%29-4o6ac.md)
  Returns a vector mask with the result of a pointwise inequality comparison.
- [static func .!= (Self, Self) -> SIMDMask<Self.MaskStorage>](./dotnoteq%28_,_%29-5cnom.md)
  A vector mask with the result of a pointwise inequality comparison.
- [static func .!= (Self, Self.Scalar) -> SIMDMask<Self.MaskStorage>](./dotnoteq%28_,_%29-94n12.md)
  Returns a vector mask with the result of a pointwise inequality comparison.
- [static func .== (Self.Scalar, Self) -> SIMDMask<Self.MaskStorage>](./doteqeq%28_,_%29-4l749.md)
  Returns a vector mask with the result of a pointwise equality comparison.
- [static func .== (Self, Self.Scalar) -> SIMDMask<Self.MaskStorage>](./doteqeq%28_,_%29-6aq3z.md)
  Returns a vector mask with the result of a pointwise equality comparison.
- [static func .== (Self, Self) -> SIMDMask<Self.MaskStorage>](./doteqeq%28_,_%29-8vdyh.md)
  A vector mask with the result of a pointwise equality comparison.
- [static func == (Self, Self) -> Bool](./eqeq%28_,_%29.md)
  Returns a Boolean value indicating whether two vectors are equal.
### Initializers
- [init<S>(S)](./init%28_%29.md)
  Creates a vector from the given sequence.
- [init(arrayLiteral: Self.Scalar...)](./init%28arrayliteral%29.md)
  Creates a vector from the specified elements.
- [init(from: any Decoder) throws](./init%28from%29.md)
  Creates a new vector by decoding scalars from the given decoder.
- [init(repeating: Self.Scalar)](./init%28repeating%29-5pwub.md)
  A vector with the specified scalar in all lanes.
### Instance Properties
- [var description: String](./description.md)
  A textual description of the vector.
- [var indices: Range<Int>](./indices.md)
  The valid indices for subscripting the vector.
### Instance Methods
- [func encode(to: any Encoder) throws](./encode%28to%29.md)
  Encodes the scalars of this vector into the given encoder in an unkeyed container.
- [func hash(into: inout Hasher)](./hash%28into%29.md)
  Hashes the elements of the vector using the given hasher.
- [func replace(with: Self.Scalar, where: SIMDMask<Self.MaskStorage>)](./replace%28with,where%29-6wonx.md)
  Replaces elements of this vector with `other` in the lanes where `mask` is `true`.
- [func replace(with: Self, where: SIMDMask<Self.MaskStorage>)](./replace%28with,where%29-7bhx.md)
  Replaces elements of this vector with elements of `other` in the lanes where `mask` is `true`.
- [func replacing(with: Self, where: SIMDMask<Self.MaskStorage>) -> Self](./replacing%28with,where%29-2gka4.md)
  Returns a copy of this vector, with elements replaced by elements of `other` in the lanes where `mask` is `true`.
- [func replacing(with: Self.Scalar, where: SIMDMask<Self.MaskStorage>) -> Self](./replacing%28with,where%29-3lyjl.md)
  Returns a copy of this vector, with elements `other` in the lanes where `mask` is `true`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/simdmask/simd-implementations)*
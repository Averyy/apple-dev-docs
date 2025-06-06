# SIMD Implementations

**Framework**: Swift

## Topics

### Operators
- [static func & (Self, Self) -> Self](simd64/&(_:_:)-48kwh.md)
- [static func & (Self, Self.Scalar) -> Self](simd64/&(_:_:)-5sdoy.md)
- [static func & (Self.Scalar, Self) -> Self](simd64/&(_:_:)-659cg.md)
- [static func &* (Self.Scalar, Self) -> Self](simd64/&*(_:_:)-3k94q.md)
- [static func &* (Self, Self.Scalar) -> Self](simd64/&*(_:_:)-7amwd.md)
- [static func &* (Self, Self) -> Self](simd64/&*(_:_:)-rfmc.md)
- [static func &*= (inout Self, Self)](simd64/&*=(_:_:)-2qjaa.md)
- [static func &*= (inout Self, Self.Scalar)](simd64/&*=(_:_:)-551ly.md)
- [static func &+ (Self.Scalar, Self) -> Self](simd64/&+(_:_:)-31fpl.md)
- [static func &+ (Self, Self.Scalar) -> Self](simd64/&+(_:_:)-69btx.md)
- [static func &+ (Self, Self) -> Self](simd64/&+(_:_:)-6m447.md)
- [static func &+= (inout Self, Self)](simd64/&+=(_:_:)-1s4xc.md)
- [static func &+= (inout Self, Self.Scalar)](simd64/&+=(_:_:)-5gvtu.md)
- [static func &- (Self, Self.Scalar) -> Self](simd64/&-(_:_:)-1oiep.md)
- [static func &- (Self.Scalar, Self) -> Self](simd64/&-(_:_:)-4gmrm.md)
- [static func &- (Self, Self) -> Self](simd64/&-(_:_:)-8b6pz.md)
- [static func &-= (inout Self, Self.Scalar)](simd64/&-=(_:_:)-4ygnj.md)
- [static func &-= (inout Self, Self)](simd64/&-=(_:_:)-67jym.md)
- [static func &= (inout Self, Self.Scalar)](simd64/&=(_:_:)-5wpkl.md)
- [static func &= (inout Self, Self)](simd64/&=(_:_:)-98sr1.md)
- [static func &<< (Self, Self.Scalar) -> Self](simd64/&__(_:_:)-1ri1r.md)
- [static func &>> (Self.Scalar, Self) -> Self](simd64/&__(_:_:)-3zzo0.md)
- [static func &<< (Self.Scalar, Self) -> Self](simd64/&__(_:_:)-7iub3.md)
- [static func &>> (Self, Self.Scalar) -> Self](simd64/&__(_:_:)-7j9fy.md)
- [static func &>> (Self, Self) -> Self](simd64/&__(_:_:)-8keg3.md)
- [static func &<< (Self, Self) -> Self](simd64/&__(_:_:)-9rxgq.md)
- [static func &>>= (inout Self, Self.Scalar)](simd64/&__=(_:_:)-3sibz.md)
- [static func &>>= (inout Self, Self)](simd64/&__=(_:_:)-6veiv.md)
- [static func &<<= (inout Self, Self)](simd64/&__=(_:_:)-8i87o.md)
- [static func &<<= (inout Self, Self.Scalar)](simd64/&__=(_:_:)-8rzj9.md)
- [static func * (Self.Scalar, Self) -> Self](simd64/*(_:_:)-38y62.md)
- [static func * (Self, Self.Scalar) -> Self](simd64/*(_:_:)-3kbvd.md)
- [static func * (Self, Self.Scalar) -> Self](simd64/*(_:_:)-4mjjh.md)
- [static func * (Self, Self) -> Self](simd64/*(_:_:)-7agrf.md)
- [static func * (Self.Scalar, Self) -> Self](simd64/*(_:_:)-80pyw.md)
- [static func * (Self, Self) -> Self](simd64/*(_:_:)-99vn7.md)
- [static func *= (inout Self, Self)](simd64/*=(_:_:)-1z3id.md)
- [static func *= (inout Self, Self)](simd64/*=(_:_:)-3ntoe.md)
- [static func *= (inout Self, Self.Scalar)](simd64/*=(_:_:)-3vpxk.md)
- [static func *= (inout Self, Self.Scalar)](simd64/*=(_:_:)-8vgob.md)
- [static func + (Self.Scalar, Self) -> Self](simd64/+(_:_:)-27h1w.md)
- [static func + (Self, Self) -> Self](simd64/+(_:_:)-3wpa7.md)
- [static func + (Self, Self.Scalar) -> Self](simd64/+(_:_:)-4ff09.md)
- [static func + (Self.Scalar, Self) -> Self](simd64/+(_:_:)-5r8e2.md)
- [static func + (Self, Self.Scalar) -> Self](simd64/+(_:_:)-69rpi.md)
- [static func + (Self, Self) -> Self](simd64/+(_:_:)-jka1.md)
- [static func += (inout Self, Self.Scalar)](simd64/+=(_:_:)-26hfp.md)
- [static func += (inout Self, Self.Scalar)](simd64/+=(_:_:)-2kbw8.md)
- [static func += (inout Self, Self)](simd64/+=(_:_:)-5sues.md)
- [static func += (inout Self, Self)](simd64/+=(_:_:)-9gmka.md)
- [static func - (Self) -> Self](simd64/-(_:).md)
- [static func - (Self, Self) -> Self](simd64/-(_:_:)-1q4hs.md)
- [static func - (Self.Scalar, Self) -> Self](simd64/-(_:_:)-2pwx9.md)
- [static func - (Self, Self) -> Self](simd64/-(_:_:)-7ar0m.md)
- [static func - (Self, Self.Scalar) -> Self](simd64/-(_:_:)-8nctl.md)
- [static func - (Self, Self.Scalar) -> Self](simd64/-(_:_:)-fbas.md)
- [static func - (Self.Scalar, Self) -> Self](simd64/-(_:_:)-tcjo.md)
- [static func -= (inout Self, Self)](simd64/-=(_:_:)-117zm.md)
- [static func -= (inout Self, Self)](simd64/-=(_:_:)-20ca5.md)
- [static func -= (inout Self, Self.Scalar)](simd64/-=(_:_:)-4lsxo.md)
- [static func -= (inout Self, Self.Scalar)](simd64/-=(_:_:)-7bdez.md)
- [static func .!= (Self.Scalar, Self) -> SIMDMask<Self.MaskStorage>](simd64/'.!=(_:_:)-2c3lu.md)
  Returns a vector mask with the result of a pointwise inequality comparison.
- [static func .!= (Self, Self.Scalar) -> SIMDMask<Self.MaskStorage>](simd64/'.!=(_:_:)-5wk7u.md)
  Returns a vector mask with the result of a pointwise inequality comparison.
- [static func .!= (Self, Self) -> SIMDMask<Self.MaskStorage>](simd64/'.!=(_:_:)-8woo1.md)
  A vector mask with the result of a pointwise inequality comparison.
- [static func .== (Self, Self) -> SIMDMask<Self.MaskStorage>](simd64/'.==(_:_:)-68z13.md)
  A vector mask with the result of a pointwise equality comparison.
- [static func .== (Self.Scalar, Self) -> SIMDMask<Self.MaskStorage>](simd64/'.==(_:_:)-75g24.md)
  Returns a vector mask with the result of a pointwise equality comparison.
- [static func .== (Self, Self.Scalar) -> SIMDMask<Self.MaskStorage>](simd64/'.==(_:_:)-99k0t.md)
  Returns a vector mask with the result of a pointwise equality comparison.
- [static func .< (Self, Self) -> SIMDMask<Self.MaskStorage>](simd64/'._(_:_:)-1s0b9.md)
  Returns a vector mask with the result of a pointwise less than comparison.
- [static func .> (Self.Scalar, Self) -> SIMDMask<Self.MaskStorage>](simd64/'._(_:_:)-3tla5.md)
  Returns a vector mask with the result of a pointwise greater than comparison.
- [static func .> (Self, Self) -> SIMDMask<Self.MaskStorage>](simd64/'._(_:_:)-6n0pt.md)
  Returns a vector mask with the result of a pointwise greater than comparison.
- [static func .< (Self, Self.Scalar) -> SIMDMask<Self.MaskStorage>](simd64/'._(_:_:)-6yfx0.md)
  Returns a vector mask with the result of a pointwise less than comparison.
- [static func .> (Self, Self.Scalar) -> SIMDMask<Self.MaskStorage>](simd64/'._(_:_:)-7smbh.md)
  Returns a vector mask with the result of a pointwise greater than comparison.
- [static func .< (Self.Scalar, Self) -> SIMDMask<Self.MaskStorage>](simd64/'._(_:_:)-7srs5.md)
  Returns a vector mask with the result of a pointwise less than comparison.
- [static func .>= (Self, Self.Scalar) -> SIMDMask<Self.MaskStorage>](simd64/'._=(_:_:)-1v69f.md)
  Returns a vector mask with the result of a pointwise greater than or equal comparison.
- [static func .<= (Self.Scalar, Self) -> SIMDMask<Self.MaskStorage>](simd64/'._=(_:_:)-34q4.md)
  Returns a vector mask with the result of a pointwise less than or equal comparison.
- [static func .>= (Self, Self) -> SIMDMask<Self.MaskStorage>](simd64/'._=(_:_:)-4b5ol.md)
  Returns a vector mask with the result of a pointwise greater than or equal comparison.
- [static func .<= (Self, Self.Scalar) -> SIMDMask<Self.MaskStorage>](simd64/'._=(_:_:)-4y5lb.md)
  Returns a vector mask with the result of a pointwise less than or equal comparison.
- [static func .<= (Self, Self) -> SIMDMask<Self.MaskStorage>](simd64/'._=(_:_:)-4zn9d.md)
  Returns a vector mask with the result of a pointwise less than or equal comparison.
- [static func .>= (Self.Scalar, Self) -> SIMDMask<Self.MaskStorage>](simd64/'._=(_:_:)-6dy5p.md)
  Returns a vector mask with the result of a pointwise greater than or equal comparison.
- [static func == (Self, Self) -> Bool](simd64/==(_:_:).md)
  Returns a Boolean value indicating whether two vectors are equal.
- [static func | (Self, Self.Scalar) -> Self](simd64/_(_:_:)-3e53o.md)
- [static func | (Self.Scalar, Self) -> Self](simd64/_(_:_:)-3mmse.md)
- [static func % (Self, Self) -> Self](simd64/_(_:_:)-3mrhw.md)
- [static func ^ (Self, Self) -> Self](simd64/_(_:_:)-3rknz.md)
- [static func / (Self.Scalar, Self) -> Self](simd64/_(_:_:)-4b85p.md)
- [static func ^ (Self, Self.Scalar) -> Self](simd64/_(_:_:)-4p1dd.md)
- [static func / (Self, Self) -> Self](simd64/_(_:_:)-53v87.md)
- [static func | (Self, Self) -> Self](simd64/_(_:_:)-5axk6.md)
- [static func / (Self, Self) -> Self](simd64/_(_:_:)-5bfge.md)
- [static func / (Self, Self.Scalar) -> Self](simd64/_(_:_:)-5tz1l.md)
- [static func ^ (Self.Scalar, Self) -> Self](simd64/_(_:_:)-6f021.md)
- [static func % (Self.Scalar, Self) -> Self](simd64/_(_:_:)-7xkx0.md)
- [static func / (Self.Scalar, Self) -> Self](simd64/_(_:_:)-8y8tm.md)
- [static func % (Self, Self.Scalar) -> Self](simd64/_(_:_:)-9p4bu.md)
- [static func / (Self, Self.Scalar) -> Self](simd64/_(_:_:)-f4mg.md)
- [static func %= (inout Self, Self)](simd64/_=(_:_:)-1d41k.md)
- [static func /= (inout Self, Self.Scalar)](simd64/_=(_:_:)-2haal.md)
- [static func |= (inout Self, Self)](simd64/_=(_:_:)-2nqna.md)
- [static func /= (inout Self, Self)](simd64/_=(_:_:)-2opf0.md)
- [static func /= (inout Self, Self)](simd64/_=(_:_:)-2z9yb.md)
- [static func ^= (inout Self, Self.Scalar)](simd64/_=(_:_:)-3rd8x.md)
- [static func /= (inout Self, Self.Scalar)](simd64/_=(_:_:)-6hdyq.md)
- [static func %= (inout Self, Self.Scalar)](simd64/_=(_:_:)-98nne.md)
- [static func ^= (inout Self, Self)](simd64/_=(_:_:)-9mati.md)
- [static func |= (inout Self, Self.Scalar)](simd64/_=(_:_:)-r1oc.md)
- [static func ~ (Self) -> Self](simd64/~(_:).md)
### Initializers
- [init<S>(S)](simd64/init(_:)-6l6bn.md)
  Creates a vector from the given sequence.
- [init(arrayLiteral: Self.Scalar...)](simd64/init(arrayliteral:).md)
  Creates a vector from the specified elements.
- [init(from: any Decoder) throws](simd64/init(from:).md)
  Creates a new vector by decoding scalars from the given decoder.
- [init(repeating: Self.Scalar)](simd64/init(repeating:).md)
  A vector with the specified value in all lanes.
### Instance Properties
- [var description: String](simd64/description.md)
  A textual description of the vector.
- [var indices: Range<Int>](simd64/indices.md)
  The valid indices for subscripting the vector.
- [var leadingZeroBitCount: Self](simd64/leadingzerobitcount.md)
- [var nonzeroBitCount: Self](simd64/nonzerobitcount.md)
- [var trailingZeroBitCount: Self](simd64/trailingzerobitcount.md)
### Instance Methods
- [func addProduct(Self.Scalar, Self)](simd64/addproduct(_:_:)-2v9r3.md)
- [func addProduct(Self, Self)](simd64/addproduct(_:_:)-6gitz.md)
- [func addProduct(Self, Self.Scalar)](simd64/addproduct(_:_:)-94bac.md)
- [func addingProduct(Self, Self.Scalar) -> Self](simd64/addingproduct(_:_:)-8bwvm.md)
- [func addingProduct(Self.Scalar, Self) -> Self](simd64/addingproduct(_:_:)-99pn7.md)
- [func addingProduct(Self, Self) -> Self](simd64/addingproduct(_:_:)-ivsx.md)
- [func clamp(lowerBound: Self, upperBound: Self)](simd64/clamp(lowerbound:upperbound:)-ac6p.md)
- [func clamp(lowerBound: Self, upperBound: Self)](simd64/clamp(lowerbound:upperbound:)-wuiq.md)
- [func clamped(lowerBound: Self, upperBound: Self) -> Self](simd64/clamped(lowerbound:upperbound:)-3qdwo.md)
- [func clamped(lowerBound: Self, upperBound: Self) -> Self](simd64/clamped(lowerbound:upperbound:)-5ot5h.md)
- [func encode(to: any Encoder) throws](simd64/encode(to:).md)
  Encodes the scalars of this vector into the given encoder in an unkeyed container.
- [func formSquareRoot()](simd64/formsquareroot.md)
- [func hash(into: inout Hasher)](simd64/hash(into:).md)
  Hashes the elements of the vector using the given hasher.
- [func max() -> Self.Scalar](simd64/max-3n69z.md)
  The greatest scalar in the vector.
- [func max() -> Self.Scalar](simd64/max-9irq5.md)
  The greatest element in the vector.
- [func min() -> Self.Scalar](simd64/min-52hug.md)
  The least element in the vector.
- [func min() -> Self.Scalar](simd64/min-9s02d.md)
  The least scalar in the vector.
- [func replace(with: Self, where: SIMDMask<Self.MaskStorage>)](simd64/replace(with:where:)-7685a.md)
  Replaces elements of this vector with elements of `other` in the lanes where `mask` is `true`.
- [func replace(with: Self.Scalar, where: SIMDMask<Self.MaskStorage>)](simd64/replace(with:where:)-99fgt.md)
  Replaces elements of this vector with `other` in the lanes where `mask` is `true`.
- [func replacing(with: Self, where: SIMDMask<Self.MaskStorage>) -> Self](simd64/replacing(with:where:)-3ecx2.md)
  Returns a copy of this vector, with elements replaced by elements of `other` in the lanes where `mask` is `true`.
- [func replacing(with: Self.Scalar, where: SIMDMask<Self.MaskStorage>) -> Self](simd64/replacing(with:where:)-xwqn.md)
  Returns a copy of this vector, with elements `other` in the lanes where `mask` is `true`.
- [func round(FloatingPointRoundingRule)](simd64/round(_:).md)
- [func rounded(FloatingPointRoundingRule) -> Self](simd64/rounded(_:).md)
  A vector formed by rounding each lane of the source vector to an integral value according to the specified rounding `rule`.
- [func squareRoot() -> Self](simd64/squareroot.md)
- [func sum() -> Self.Scalar](simd64/sum.md)
  The sum of the scalars in the vector.
- [func wrappedSum() -> Self.Scalar](simd64/wrappedsum.md)
  Returns the sum of the scalars in the vector, computed with wrapping addition.
### Type Properties
- [static var one: Self](simd64/one-1lpug.md)
  A vector with one in all lanes.
- [static var one: Self](simd64/one-44mp3.md)
  A vector with one in all lanes.
- [static var zero: Self](simd64/zero-2faik.md)
  A vector with zero in all lanes.
- [static var zero: Self](simd64/zero-3vf97.md)
  A vector with zero in all lanes.
### Type Methods
- [static func random(in: ClosedRange<Self.Scalar>) -> Self](simd64/random(in:)-46u2s.md)
  Returns a vector with random values from within the specified range in all lanes.
- [static func random(in: Range<Self.Scalar>) -> Self](simd64/random(in:)-8do2i.md)
  Returns a vector with random values from within the specified range in all lanes.
- [static func random<T>(in: Range<Self.Scalar>, using: inout T) -> Self](simd64/random(in:using:)-7qbkk.md)
  Returns a vector with random values from within the specified range in all lanes, using the given generator as a source for randomness.
- [static func random<T>(in: ClosedRange<Self.Scalar>, using: inout T) -> Self](simd64/random(in:using:)-8863m.md)
  Returns a vector with random values from within the specified range in all lanes, using the given generator as a source for randomness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/simd64/simd-implementations)*
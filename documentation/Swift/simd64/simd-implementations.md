# SIMD Implementations

**Framework**: Swift  
**Role**: API Collection

## Topics

### Operators
- [static func & (Self, Self) -> Self](./amp%28_,_%29-48kwh.md)
- [static func & (Self, Self.Scalar) -> Self](./amp%28_,_%29-5sdoy.md)
- [static func & (Self.Scalar, Self) -> Self](./amp%28_,_%29-659cg.md)
- [static func &* (Self.Scalar, Self) -> Self](./ampstar%28_,_%29-3k94q.md)
- [static func &* (Self, Self.Scalar) -> Self](./ampstar%28_,_%29-7amwd.md)
- [static func &* (Self, Self) -> Self](./ampstar%28_,_%29-rfmc.md)
- [static func &*= (inout Self, Self)](./ampstareq%28_,_%29-2qjaa.md)
- [static func &*= (inout Self, Self.Scalar)](./ampstareq%28_,_%29-551ly.md)
- [static func &+ (Self.Scalar, Self) -> Self](./ampplus%28_,_%29-31fpl.md)
- [static func &+ (Self, Self.Scalar) -> Self](./ampplus%28_,_%29-69btx.md)
- [static func &+ (Self, Self) -> Self](./ampplus%28_,_%29-6m447.md)
- [static func &+= (inout Self, Self)](./amppluseq%28_,_%29-1s4xc.md)
- [static func &+= (inout Self, Self.Scalar)](./amppluseq%28_,_%29-5gvtu.md)
- [static func &- (Self, Self.Scalar) -> Self](./ampminus%28_,_%29-1oiep.md)
- [static func &- (Self.Scalar, Self) -> Self](./ampminus%28_,_%29-4gmrm.md)
- [static func &- (Self, Self) -> Self](./ampminus%28_,_%29-8b6pz.md)
- [static func &-= (inout Self, Self.Scalar)](./ampminuseq%28_,_%29-4ygnj.md)
- [static func &-= (inout Self, Self)](./ampminuseq%28_,_%29-67jym.md)
- [static func &= (inout Self, Self.Scalar)](./ampeq%28_,_%29-5wpkl.md)
- [static func &= (inout Self, Self)](./ampeq%28_,_%29-98sr1.md)
- [static func &<< (Self, Self.Scalar) -> Self](./ampopop%28_,_%29-1ri1r.md)
- [static func &>> (Self.Scalar, Self) -> Self](./ampopop%28_,_%29-3zzo0.md)
- [static func &<< (Self.Scalar, Self) -> Self](./ampopop%28_,_%29-7iub3.md)
- [static func &>> (Self, Self.Scalar) -> Self](./ampopop%28_,_%29-7j9fy.md)
- [static func &>> (Self, Self) -> Self](./ampopop%28_,_%29-8keg3.md)
- [static func &<< (Self, Self) -> Self](./ampopop%28_,_%29-9rxgq.md)
- [static func &>>= (inout Self, Self.Scalar)](./ampopopeq%28_,_%29-3sibz.md)
- [static func &>>= (inout Self, Self)](./ampopopeq%28_,_%29-6veiv.md)
- [static func &<<= (inout Self, Self)](./ampopopeq%28_,_%29-8i87o.md)
- [static func &<<= (inout Self, Self.Scalar)](./ampopopeq%28_,_%29-8rzj9.md)
- [static func * (Self.Scalar, Self) -> Self](./star%28_,_%29-38y62.md)
- [static func * (Self, Self.Scalar) -> Self](./star%28_,_%29-3kbvd.md)
- [static func * (Self, Self.Scalar) -> Self](./star%28_,_%29-4mjjh.md)
- [static func * (Self, Self) -> Self](./star%28_,_%29-7agrf.md)
- [static func * (Self.Scalar, Self) -> Self](./star%28_,_%29-80pyw.md)
- [static func * (Self, Self) -> Self](./star%28_,_%29-99vn7.md)
- [static func *= (inout Self, Self)](./stareq%28_,_%29-1z3id.md)
- [static func *= (inout Self, Self)](./stareq%28_,_%29-3ntoe.md)
- [static func *= (inout Self, Self.Scalar)](./stareq%28_,_%29-3vpxk.md)
- [static func *= (inout Self, Self.Scalar)](./stareq%28_,_%29-8vgob.md)
- [static func + (Self.Scalar, Self) -> Self](./plus%28_,_%29-27h1w.md)
- [static func + (Self, Self) -> Self](./plus%28_,_%29-3wpa7.md)
- [static func + (Self, Self.Scalar) -> Self](./plus%28_,_%29-4ff09.md)
- [static func + (Self.Scalar, Self) -> Self](./plus%28_,_%29-5r8e2.md)
- [static func + (Self, Self.Scalar) -> Self](./plus%28_,_%29-69rpi.md)
- [static func + (Self, Self) -> Self](./plus%28_,_%29-jka1.md)
- [static func += (inout Self, Self.Scalar)](./pluseq%28_,_%29-26hfp.md)
- [static func += (inout Self, Self.Scalar)](./pluseq%28_,_%29-2kbw8.md)
- [static func += (inout Self, Self)](./pluseq%28_,_%29-5sues.md)
- [static func += (inout Self, Self)](./pluseq%28_,_%29-9gmka.md)
- [static func - (Self) -> Self](./minus%28_%29.md)
- [static func - (Self, Self) -> Self](./minus%28_,_%29-1q4hs.md)
- [static func - (Self.Scalar, Self) -> Self](./minus%28_,_%29-2pwx9.md)
- [static func - (Self, Self) -> Self](./minus%28_,_%29-7ar0m.md)
- [static func - (Self, Self.Scalar) -> Self](./minus%28_,_%29-8nctl.md)
- [static func - (Self, Self.Scalar) -> Self](./minus%28_,_%29-fbas.md)
- [static func - (Self.Scalar, Self) -> Self](./minus%28_,_%29-tcjo.md)
- [static func -= (inout Self, Self)](./minuseq%28_,_%29-117zm.md)
- [static func -= (inout Self, Self)](./minuseq%28_,_%29-20ca5.md)
- [static func -= (inout Self, Self.Scalar)](./minuseq%28_,_%29-4lsxo.md)
- [static func -= (inout Self, Self.Scalar)](./minuseq%28_,_%29-7bdez.md)
- [static func .!= (Self.Scalar, Self) -> SIMDMask<Self.MaskStorage>](./dotnoteq%28_,_%29-2c3lu.md)
  Returns a vector mask with the result of a pointwise inequality comparison.
- [static func .!= (Self, Self.Scalar) -> SIMDMask<Self.MaskStorage>](./dotnoteq%28_,_%29-5wk7u.md)
  Returns a vector mask with the result of a pointwise inequality comparison.
- [static func .!= (Self, Self) -> SIMDMask<Self.MaskStorage>](./dotnoteq%28_,_%29-8woo1.md)
  A vector mask with the result of a pointwise inequality comparison.
- [static func .== (Self, Self) -> SIMDMask<Self.MaskStorage>](./doteqeq%28_,_%29-68z13.md)
  A vector mask with the result of a pointwise equality comparison.
- [static func .== (Self.Scalar, Self) -> SIMDMask<Self.MaskStorage>](./doteqeq%28_,_%29-75g24.md)
  Returns a vector mask with the result of a pointwise equality comparison.
- [static func .== (Self, Self.Scalar) -> SIMDMask<Self.MaskStorage>](./doteqeq%28_,_%29-99k0t.md)
  Returns a vector mask with the result of a pointwise equality comparison.
- [static func .< (Self, Self) -> SIMDMask<Self.MaskStorage>](./dotop%28_,_%29-1s0b9.md)
  Returns a vector mask with the result of a pointwise less than comparison.
- [static func .> (Self.Scalar, Self) -> SIMDMask<Self.MaskStorage>](./dotop%28_,_%29-3tla5.md)
  Returns a vector mask with the result of a pointwise greater than comparison.
- [static func .> (Self, Self) -> SIMDMask<Self.MaskStorage>](./dotop%28_,_%29-6n0pt.md)
  Returns a vector mask with the result of a pointwise greater than comparison.
- [static func .< (Self, Self.Scalar) -> SIMDMask<Self.MaskStorage>](./dotop%28_,_%29-6yfx0.md)
  Returns a vector mask with the result of a pointwise less than comparison.
- [static func .> (Self, Self.Scalar) -> SIMDMask<Self.MaskStorage>](./dotop%28_,_%29-7smbh.md)
  Returns a vector mask with the result of a pointwise greater than comparison.
- [static func .< (Self.Scalar, Self) -> SIMDMask<Self.MaskStorage>](./dotop%28_,_%29-7srs5.md)
  Returns a vector mask with the result of a pointwise less than comparison.
- [static func .>= (Self, Self.Scalar) -> SIMDMask<Self.MaskStorage>](./dotopeq%28_,_%29-1v69f.md)
  Returns a vector mask with the result of a pointwise greater than or equal comparison.
- [static func .<= (Self.Scalar, Self) -> SIMDMask<Self.MaskStorage>](./dotopeq%28_,_%29-34q4.md)
  Returns a vector mask with the result of a pointwise less than or equal comparison.
- [static func .>= (Self, Self) -> SIMDMask<Self.MaskStorage>](./dotopeq%28_,_%29-4b5ol.md)
  Returns a vector mask with the result of a pointwise greater than or equal comparison.
- [static func .<= (Self, Self.Scalar) -> SIMDMask<Self.MaskStorage>](./dotopeq%28_,_%29-4y5lb.md)
  Returns a vector mask with the result of a pointwise less than or equal comparison.
- [static func .<= (Self, Self) -> SIMDMask<Self.MaskStorage>](./dotopeq%28_,_%29-4zn9d.md)
  Returns a vector mask with the result of a pointwise less than or equal comparison.
- [static func .>= (Self.Scalar, Self) -> SIMDMask<Self.MaskStorage>](./dotopeq%28_,_%29-6dy5p.md)
  Returns a vector mask with the result of a pointwise greater than or equal comparison.
- [static func == (Self, Self) -> Bool](./eqeq%28_,_%29.md)
  Returns a Boolean value indicating whether two vectors are equal.
- [static func | (Self, Self.Scalar) -> Self](./op%28_,_%29-3e53o.md)
- [static func | (Self.Scalar, Self) -> Self](./op%28_,_%29-3mmse.md)
- [static func % (Self, Self) -> Self](./op%28_,_%29-3mrhw.md)
- [static func ^ (Self, Self) -> Self](./op%28_,_%29-3rknz.md)
- [static func / (Self.Scalar, Self) -> Self](./op%28_,_%29-4b85p.md)
- [static func ^ (Self, Self.Scalar) -> Self](./op%28_,_%29-4p1dd.md)
- [static func / (Self, Self) -> Self](./op%28_,_%29-53v87.md)
- [static func | (Self, Self) -> Self](./op%28_,_%29-5axk6.md)
- [static func / (Self, Self) -> Self](./op%28_,_%29-5bfge.md)
- [static func / (Self, Self.Scalar) -> Self](./op%28_,_%29-5tz1l.md)
- [static func ^ (Self.Scalar, Self) -> Self](./op%28_,_%29-6f021.md)
- [static func % (Self.Scalar, Self) -> Self](./op%28_,_%29-7xkx0.md)
- [static func / (Self.Scalar, Self) -> Self](./op%28_,_%29-8y8tm.md)
- [static func % (Self, Self.Scalar) -> Self](./op%28_,_%29-9p4bu.md)
- [static func / (Self, Self.Scalar) -> Self](./op%28_,_%29-f4mg.md)
- [static func %= (inout Self, Self)](./opeq%28_,_%29-1d41k.md)
- [static func /= (inout Self, Self.Scalar)](./opeq%28_,_%29-2haal.md)
- [static func |= (inout Self, Self)](./opeq%28_,_%29-2nqna.md)
- [static func /= (inout Self, Self)](./opeq%28_,_%29-2opf0.md)
- [static func /= (inout Self, Self)](./opeq%28_,_%29-2z9yb.md)
- [static func ^= (inout Self, Self.Scalar)](./opeq%28_,_%29-3rd8x.md)
- [static func /= (inout Self, Self.Scalar)](./opeq%28_,_%29-6hdyq.md)
- [static func %= (inout Self, Self.Scalar)](./opeq%28_,_%29-98nne.md)
- [static func ^= (inout Self, Self)](./opeq%28_,_%29-9mati.md)
- [static func |= (inout Self, Self.Scalar)](./opeq%28_,_%29-r1oc.md)
- [static func ~ (Self) -> Self](./tilde%28_%29.md)
### Initializers
- [init<S>(S)](./init%28_%29-6l6bn.md)
  Creates a vector from the given sequence.
- [init(arrayLiteral: Self.Scalar...)](./init%28arrayliteral%29.md)
  Creates a vector from the specified elements.
- [init(from: any Decoder) throws](./init%28from%29.md)
  Creates a new vector by decoding scalars from the given decoder.
- [init(repeating: Self.Scalar)](./init%28repeating%29-1uy8k.md)
  A vector with the specified scalar in all lanes.
### Instance Properties
- [var description: String](./description.md)
  A textual description of the vector.
- [var indices: Range<Int>](./indices.md)
  The valid indices for subscripting the vector.
- [var leadingZeroBitCount: Self](./leadingzerobitcount.md)
- [var nonzeroBitCount: Self](./nonzerobitcount.md)
- [var trailingZeroBitCount: Self](./trailingzerobitcount.md)
### Instance Methods
- [func addProduct(Self.Scalar, Self)](./addproduct%28_,_%29-2v9r3.md)
- [func addProduct(Self, Self)](./addproduct%28_,_%29-6gitz.md)
- [func addProduct(Self, Self.Scalar)](./addproduct%28_,_%29-94bac.md)
- [func addingProduct(Self, Self.Scalar) -> Self](./addingproduct%28_,_%29-8bwvm.md)
- [func addingProduct(Self.Scalar, Self) -> Self](./addingproduct%28_,_%29-99pn7.md)
- [func addingProduct(Self, Self) -> Self](./addingproduct%28_,_%29-ivsx.md)
- [func clamp(lowerBound: Self, upperBound: Self)](./clamp%28lowerbound,upperbound%29-ac6p.md)
- [func clamp(lowerBound: Self, upperBound: Self)](./clamp%28lowerbound,upperbound%29-wuiq.md)
- [func clamped(lowerBound: Self, upperBound: Self) -> Self](./clamped%28lowerbound,upperbound%29-3qdwo.md)
- [func clamped(lowerBound: Self, upperBound: Self) -> Self](./clamped%28lowerbound,upperbound%29-5ot5h.md)
- [func encode(to: any Encoder) throws](./encode%28to%29.md)
  Encodes the scalars of this vector into the given encoder in an unkeyed container.
- [func formSquareRoot()](./formsquareroot%28%29.md)
- [func hash(into: inout Hasher)](./hash%28into%29.md)
  Hashes the elements of the vector using the given hasher.
- [func max() -> Self.Scalar](./max%28%29-3n69z.md)
  The greatest scalar in the vector.
- [func max() -> Self.Scalar](./max%28%29-9irq5.md)
  The greatest element in the vector.
- [func min() -> Self.Scalar](./min%28%29-52hug.md)
  The least element in the vector.
- [func min() -> Self.Scalar](./min%28%29-9s02d.md)
  The least scalar in the vector.
- [func replace(with: Self, where: SIMDMask<Self.MaskStorage>)](./replace%28with,where%29-7685a.md)
  Replaces elements of this vector with elements of `other` in the lanes where `mask` is `true`.
- [func replace(with: Self.Scalar, where: SIMDMask<Self.MaskStorage>)](./replace%28with,where%29-99fgt.md)
  Replaces elements of this vector with `other` in the lanes where `mask` is `true`.
- [func replacing(with: Self, where: SIMDMask<Self.MaskStorage>) -> Self](./replacing%28with,where%29-3ecx2.md)
  Returns a copy of this vector, with elements replaced by elements of `other` in the lanes where `mask` is `true`.
- [func replacing(with: Self.Scalar, where: SIMDMask<Self.MaskStorage>) -> Self](./replacing%28with,where%29-xwqn.md)
  Returns a copy of this vector, with elements `other` in the lanes where `mask` is `true`.
- [func round(FloatingPointRoundingRule)](./round%28_%29.md)
- [func rounded(FloatingPointRoundingRule) -> Self](./rounded%28_%29.md)
  A vector formed by rounding each lane of the source vector to an integral value according to the specified rounding `rule`.
- [func squareRoot() -> Self](./squareroot%28%29.md)
- [func sum() -> Self.Scalar](./sum%28%29.md)
  The sum of the scalars in the vector.
- [func wrappedSum() -> Self.Scalar](./wrappedsum%28%29.md)
  Returns the sum of the scalars in the vector, computed with wrapping addition.
### Type Properties
- [static var one: Self](./one-1lpug.md)
  A vector with one in all lanes.
- [static var one: Self](./one-44mp3.md)
  A vector with one in all lanes.
- [static var zero: Self](./zero-2faik.md)
  A vector with zero in all lanes.
- [static var zero: Self](./zero-3vf97.md)
  A vector with zero in all lanes.
### Type Methods
- [static func random(in: ClosedRange<Self.Scalar>) -> Self](./random%28in%29-46u2s.md)
  Returns a vector with random values from within the specified range in all lanes.
- [static func random(in: Range<Self.Scalar>) -> Self](./random%28in%29-8do2i.md)
  Returns a vector with random values from within the specified range in all lanes.
- [static func random<T>(in: Range<Self.Scalar>, using: inout T) -> Self](./random%28in,using%29-7qbkk.md)
  Returns a vector with random values from within the specified range in all lanes, using the given generator as a source for randomness.
- [static func random<T>(in: ClosedRange<Self.Scalar>, using: inout T) -> Self](./random%28in,using%29-8863m.md)
  Returns a vector with random values from within the specified range in all lanes, using the given generator as a source for randomness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/simd64/simd-implementations)*
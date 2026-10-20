# SIMD

**Framework**: Swift  
**Kind**: protocol  
**Role**: Protocol

A SIMD vector of a fixed number of elements.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
protocol SIMD<Scalar> : CustomStringConvertible, Decodable, Encodable, ExpressibleByArrayLiteral, Hashable, SIMDStorage
```

## Topics

### Operators
- [static func & (Self, Self) -> Self](./simd/amp%28_,_%29-7euv2.md)
- [static func & (Self.Scalar, Self) -> Self](./simd/amp%28_,_%29-9iwe1.md)
- [static func & (Self, Self.Scalar) -> Self](./simd/amp%28_,_%29-hube.md)
- [static func &* (Self, Self) -> Self](./simd/ampstar%28_,_%29-6dnx3.md)
- [static func &* (Self.Scalar, Self) -> Self](./simd/ampstar%28_,_%29-6q9r4.md)
- [static func &* (Self, Self.Scalar) -> Self](./simd/ampstar%28_,_%29-96x3e.md)
- [static func &*= (inout Self, Self.Scalar)](./simd/ampstareq%28_,_%29-2nncu.md)
- [static func &*= (inout Self, Self)](./simd/ampstareq%28_,_%29-7upvw.md)
- [static func &+ (Self, Self.Scalar) -> Self](./simd/ampplus%28_,_%29-11ezq.md)
- [static func &+ (Self.Scalar, Self) -> Self](./simd/ampplus%28_,_%29-2dwe6.md)
- [static func &+ (Self, Self) -> Self](./simd/ampplus%28_,_%29-7atvo.md)
- [static func &+= (inout Self, Self.Scalar)](./simd/amppluseq%28_,_%29-4nb37.md)
- [static func &+= (inout Self, Self)](./simd/amppluseq%28_,_%29-6bl8h.md)
- [static func &- (Self, Self.Scalar) -> Self](./simd/ampminus%28_,_%29-18r5t.md)
- [static func &- (Self.Scalar, Self) -> Self](./simd/ampminus%28_,_%29-3k78n.md)
- [static func &- (Self, Self) -> Self](./simd/ampminus%28_,_%29-8sti5.md)
- [static func &-= (inout Self, Self.Scalar)](./simd/ampminuseq%28_,_%29-8wqjs.md)
- [static func &-= (inout Self, Self)](./simd/ampminuseq%28_,_%29-9uxv2.md)
- [static func &= (inout Self, Self.Scalar)](./simd/ampeq%28_,_%29-8ruc4.md)
- [static func &= (inout Self, Self)](./simd/ampeq%28_,_%29-9p2uz.md)
- [static func &>> (Self.Scalar, Self) -> Self](./simd/ampopop%28_,_%29-4zcvd.md)
- [static func &>> (Self, Self.Scalar) -> Self](./simd/ampopop%28_,_%29-5ccr.md)
- [static func &<< (Self.Scalar, Self) -> Self](./simd/ampopop%28_,_%29-5zfif.md)
- [static func &<< (Self, Self) -> Self](./simd/ampopop%28_,_%29-6vdh9.md)
- [static func &>> (Self, Self) -> Self](./simd/ampopop%28_,_%29-8f94f.md)
- [static func &<< (Self, Self.Scalar) -> Self](./simd/ampopop%28_,_%29-9p0g4.md)
- [static func &<<= (inout Self, Self)](./simd/ampopopeq%28_,_%29-2r7mx.md)
- [static func &>>= (inout Self, Self)](./simd/ampopopeq%28_,_%29-66i5n.md)
- [static func &>>= (inout Self, Self.Scalar)](./simd/ampopopeq%28_,_%29-8yrf.md)
- [static func &<<= (inout Self, Self.Scalar)](./simd/ampopopeq%28_,_%29-94hft.md)
- [static func * (Self, Self) -> Self](./simd/star%28_,_%29-33k6i.md)
- [static func * (Self.Scalar, Self) -> Self](./simd/star%28_,_%29-4fl9b.md)
- [static func * (Self, Self.Scalar) -> Self](./simd/star%28_,_%29-4wltm.md)
- [static func *= (inout Self, Self.Scalar)](./simd/stareq%28_,_%29-33czt.md)
- [static func *= (inout Self, Self)](./simd/stareq%28_,_%29-jal7.md)
- [static func + (Self, Self.Scalar) -> Self](./simd/plus%28_,_%29-48zcp.md)
- [static func + (Self, Self) -> Self](./simd/plus%28_,_%29-64jan.md)
- [static func + (Self.Scalar, Self) -> Self](./simd/plus%28_,_%29-68uuk.md)
- [static func += (inout Self, Self.Scalar)](./simd/pluseq%28_,_%29-14pp9.md)
- [static func += (inout Self, Self)](./simd/pluseq%28_,_%29-3jf1j.md)
- [static func += (inout Self, Self)](./simd/pluseq%28_,_%29-9f7e0.md)
- [static func - (Self) -> Self](./simd/minus%28_%29-7asi6.md)
- [static func - (Self) -> Self](./simd/minus%28_%29-9ukvl.md)
- [static func - (Self.Scalar, Self) -> Self](./simd/minus%28_,_%29-2ad59.md)
- [static func - (Self, Self.Scalar) -> Self](./simd/minus%28_,_%29-3lx2i.md)
- [static func - (Self, Self) -> Self](./simd/minus%28_,_%29-oego.md)
- [static func -= (inout Self, Self.Scalar)](./simd/minuseq%28_,_%29-4uwnp.md)
- [static func -= (inout Self, Self)](./simd/minuseq%28_,_%29-6dwmc.md)
- [static func -= (inout Self, Self)](./simd/minuseq%28_,_%29-6ejxe.md)
- [static func .!= (Self, Self) -> SIMDMask<Self.MaskStorage>](./simd/dotnoteq%28_,_%29-3m98p.md)
  A vector mask with the result of a pointwise inequality comparison.
- [static func .!= (Self, Self.Scalar) -> SIMDMask<Self.MaskStorage>](./simd/dotnoteq%28_,_%29-402ba.md)
  Returns a vector mask with the result of a pointwise inequality comparison.
- [static func .!= (Self.Scalar, Self) -> SIMDMask<Self.MaskStorage>](./simd/dotnoteq%28_,_%29-8undu.md)
  Returns a vector mask with the result of a pointwise inequality comparison.
- [static func .== (Self, Self) -> SIMDMask<Self.MaskStorage>](./simd/doteqeq%28_,_%29-1nb4h.md)
  A vector mask with the result of a pointwise equality comparison.
- [static func .== (Self, Self.Scalar) -> SIMDMask<Self.MaskStorage>](./simd/doteqeq%28_,_%29-5akc8.md)
  Returns a vector mask with the result of a pointwise equality comparison.
- [static func .== (Self.Scalar, Self) -> SIMDMask<Self.MaskStorage>](./simd/doteqeq%28_,_%29-8utr5.md)
  Returns a vector mask with the result of a pointwise equality comparison.
- [static func .> (Self, Self.Scalar) -> SIMDMask<Self.MaskStorage>](./simd/dotop%28_,_%29-2bb66.md)
  Returns a vector mask with the result of a pointwise greater than comparison.
- [static func .< (Self, Self) -> SIMDMask<Self.MaskStorage>](./simd/dotop%28_,_%29-2g6i2.md)
  Returns a vector mask with the result of a pointwise less than comparison.
- [static func .> (Self.Scalar, Self) -> SIMDMask<Self.MaskStorage>](./simd/dotop%28_,_%29-6kr63.md)
  Returns a vector mask with the result of a pointwise greater than comparison.
- [static func .> (Self, Self) -> SIMDMask<Self.MaskStorage>](./simd/dotop%28_,_%29-7ad36.md)
  Returns a vector mask with the result of a pointwise greater than comparison.
- [static func .< (Self.Scalar, Self) -> SIMDMask<Self.MaskStorage>](./simd/dotop%28_,_%29-8bwmo.md)
  Returns a vector mask with the result of a pointwise less than comparison.
- [static func .< (Self, Self.Scalar) -> SIMDMask<Self.MaskStorage>](./simd/dotop%28_,_%29-935pf.md)
  Returns a vector mask with the result of a pointwise less than comparison.
- [static func .>= (Self.Scalar, Self) -> SIMDMask<Self.MaskStorage>](./simd/dotopeq%28_,_%29-1grcf.md)
  Returns a vector mask with the result of a pointwise greater than or equal comparison.
- [static func .>= (Self, Self.Scalar) -> SIMDMask<Self.MaskStorage>](./simd/dotopeq%28_,_%29-4poyx.md)
  Returns a vector mask with the result of a pointwise greater than or equal comparison.
- [static func .<= (Self.Scalar, Self) -> SIMDMask<Self.MaskStorage>](./simd/dotopeq%28_,_%29-7ulie.md)
  Returns a vector mask with the result of a pointwise less than or equal comparison.
- [static func .<= (Self, Self.Scalar) -> SIMDMask<Self.MaskStorage>](./simd/dotopeq%28_,_%29-8vgvo.md)
  Returns a vector mask with the result of a pointwise less than or equal comparison.
- [static func .>= (Self, Self) -> SIMDMask<Self.MaskStorage>](./simd/dotopeq%28_,_%29-d7g2.md)
  Returns a vector mask with the result of a pointwise greater than or equal comparison.
- [static func .<= (Self, Self) -> SIMDMask<Self.MaskStorage>](./simd/dotopeq%28_,_%29-iulp.md)
  Returns a vector mask with the result of a pointwise less than or equal comparison.
- [static func % (Self.Scalar, Self) -> Self](./simd/op%28_,_%29-1qdv9.md)
- [static func / (Self.Scalar, Self) -> Self](./simd/op%28_,_%29-1rb4.md)
- [static func | (Self, Self.Scalar) -> Self](./simd/op%28_,_%29-225ln.md)
- [static func / (Self, Self.Scalar) -> Self](./simd/op%28_,_%29-2hi2t.md)
- [static func / (Self, Self.Scalar) -> Self](./simd/op%28_,_%29-2om3p.md)
- [static func | (Self, Self) -> Self](./simd/op%28_,_%29-3ge91.md)
- [static func % (Self, Self.Scalar) -> Self](./simd/op%28_,_%29-3scvv.md)
- [static func % (Self, Self) -> Self](./simd/op%28_,_%29-4djx9.md)
- [static func | (Self.Scalar, Self) -> Self](./simd/op%28_,_%29-5f3rz.md)
- [static func ^ (Self, Self) -> Self](./simd/op%28_,_%29-620ag.md)
- [static func ^ (Self, Self.Scalar) -> Self](./simd/op%28_,_%29-6ryjr.md)
- [static func / (Self, Self) -> Self](./simd/op%28_,_%29-6tba5.md)
- [static func ^ (Self.Scalar, Self) -> Self](./simd/op%28_,_%29-73syd.md)
- [static func / (Self.Scalar, Self) -> Self](./simd/op%28_,_%29-80bu5.md)
- [static func / (Self, Self) -> Self](./simd/op%28_,_%29-8gl48.md)
- [static func %= (inout Self, Self)](./simd/opeq%28_,_%29-17fvb.md)
- [static func |= (inout Self, Self)](./simd/opeq%28_,_%29-1olgw.md)
- [static func /= (inout Self, Self)](./simd/opeq%28_,_%29-1xum3.md)
- [static func /= (inout Self, Self)](./simd/opeq%28_,_%29-2i5w5.md)
- [static func ^= (inout Self, Self.Scalar)](./simd/opeq%28_,_%29-5qmfn.md)
- [static func |= (inout Self, Self.Scalar)](./simd/opeq%28_,_%29-7q26h.md)
- [static func /= (inout Self, Self.Scalar)](./simd/opeq%28_,_%29-9rh2.md)
- [static func ^= (inout Self, Self)](./simd/opeq%28_,_%29-9yqbl.md)
- [static func /= (inout Self, Self.Scalar)](./simd/opeq%28_,_%29-dtaz.md)
- [static func %= (inout Self, Self.Scalar)](./simd/opeq%28_,_%29-eq5q.md)
- [static func ~ (Self) -> Self](./simd/tilde%28_%29.md)
### Associated Types
- [associatedtype MaskStorage : SIMD](./simd/maskstorage.md)
  The mask type resulting from pointwise comparisons of this vector type.
### Initializers
- [init<S>(S)](./simd/init%28_%29-18uy8.md)
  Creates a vector from the given sequence.
- [init(Self.Scalar)](./simd/init%28_%29-4h623.md)
- [init(repeating: Self.Scalar)](./simd/init%28repeating%29.md)
  A vector with the specified scalar in all lanes.
### Instance Properties
- [var indices: Range<Int>](./simd/indices.md)
  The valid indices for subscripting the vector.
- [var leadingZeroBitCount: Self](./simd/leadingzerobitcount.md)
- [var nonzeroBitCount: Self](./simd/nonzerobitcount.md)
- [var trailingZeroBitCount: Self](./simd/trailingzerobitcount.md)
### Instance Methods
- [func addProduct(Self.Scalar, Self)](./simd/addproduct%28_,_%29-256j6.md)
- [func addProduct(Self, Self.Scalar)](./simd/addproduct%28_,_%29-3mvjt.md)
- [func addProduct(Self, Self)](./simd/addproduct%28_,_%29-i1fp.md)
- [func addingProduct(Self, Self.Scalar) -> Self](./simd/addingproduct%28_,_%29-4h4k3.md)
- [func addingProduct(Self.Scalar, Self) -> Self](./simd/addingproduct%28_,_%29-59qn8.md)
- [func addingProduct(Self, Self) -> Self](./simd/addingproduct%28_,_%29-kk15.md)
- [func clamp(lowerBound: Self, upperBound: Self)](./simd/clamp%28lowerbound,upperbound%29-3tdwm.md)
- [func clamp(lowerBound: Self, upperBound: Self)](./simd/clamp%28lowerbound,upperbound%29-yh51.md)
- [func clamped(lowerBound: Self, upperBound: Self) -> Self](./simd/clamped%28lowerbound,upperbound%29-4k4gy.md)
- [func clamped(lowerBound: Self, upperBound: Self) -> Self](./simd/clamped%28lowerbound,upperbound%29-9hl58.md)
- [func formSquareRoot()](./simd/formsquareroot%28%29.md)
- [func max() -> Self.Scalar](./simd/max%28%29-7j0po.md)
  The greatest scalar in the vector.
- [func max() -> Self.Scalar](./simd/max%28%29-l6ds.md)
  The greatest element in the vector.
- [func min() -> Self.Scalar](./simd/min%28%29-7pa71.md)
  The least scalar in the vector.
- [func min() -> Self.Scalar](./simd/min%28%29-9z12h.md)
  The least element in the vector.
- [func replace(with: Self.Scalar, where: SIMDMask<Self.MaskStorage>)](./simd/replace%28with,where%29-6if0p.md)
  Replaces elements of this vector with `other` in the lanes where `mask` is `true`.
- [func replace(with: Self, where: SIMDMask<Self.MaskStorage>)](./simd/replace%28with,where%29-91tn3.md)
  Replaces elements of this vector with elements of `other` in the lanes where `mask` is `true`.
- [func replacing(with: Self, where: SIMDMask<Self.MaskStorage>) -> Self](./simd/replacing%28with,where%29-1nga6.md)
  Returns a copy of this vector, with elements replaced by elements of `other` in the lanes where `mask` is `true`.
- [func replacing(with: Self.Scalar, where: SIMDMask<Self.MaskStorage>) -> Self](./simd/replacing%28with,where%29-8vzk.md)
  Returns a copy of this vector, with elements `other` in the lanes where `mask` is `true`.
- [func round(FloatingPointRoundingRule)](./simd/round%28_%29.md)
- [func rounded(FloatingPointRoundingRule) -> Self](./simd/rounded%28_%29.md)
  A vector formed by rounding each lane of the source vector to an integral value according to the specified rounding `rule`.
- [func squareRoot() -> Self](./simd/squareroot%28%29.md)
- [func sum() -> Self.Scalar](./simd/sum%28%29.md)
  The sum of the scalars in the vector.
- [func wrappedSum() -> Self.Scalar](./simd/wrappedsum%28%29.md)
  Returns the sum of the scalars in the vector, computed with wrapping addition.
### Type Properties
- [static var one: Self](./simd/one-428b1.md)
  A vector with one in all lanes.
- [static var one: Self](./simd/one-6bgr9.md)
  A vector with one in all lanes.
- [static var zero: Self](./simd/zero-6gnz.md)
  A vector with zero in all lanes.
- [static var zero: Self](./simd/zero-8n566.md)
  A vector with zero in all lanes.
### Type Methods
- [static func random(in: ClosedRange<Self.Scalar>) -> Self](./simd/random%28in%29-13ruo.md)
  Returns a vector with random values from within the specified range in all lanes.
- [static func random(in: Range<Self.Scalar>) -> Self](./simd/random%28in%29-3meec.md)
  Returns a vector with random values from within the specified range in all lanes.
- [static func random(in: ClosedRange<Self.Scalar>) -> Self](./simd/random%28in%29-4rat4.md)
  Returns a vector with random values from within the specified range in all lanes.
- [static func random(in: Range<Self.Scalar>) -> Self](./simd/random%28in%29-5ur5a.md)
  Returns a vector with random values from within the specified range in all lanes.
- [static func random<T>(in: ClosedRange<Self.Scalar>, using: inout T) -> Self](./simd/random%28in,using%29-5uz8w.md)
  Returns a vector with random values from within the specified range in all lanes, using the given generator as a source for randomness.
- [static func random<T>(in: Range<Self.Scalar>, using: inout T) -> Self](./simd/random%28in,using%29-86tab.md)
  Returns a vector with random values from within the specified range in all lanes, using the given generator as a source for randomness.
- [static func random<T>(in: Range<Self.Scalar>, using: inout T) -> Self](./simd/random%28in,using%29-8bcnv.md)
  Returns a vector with random values from within the specified range in all lanes, using the given generator as a source for randomness.
- [static func random<T>(in: ClosedRange<Self.Scalar>, using: inout T) -> Self](./simd/random%28in,using%29-8yt59.md)
  Returns a vector with random values from within the specified range in all lanes, using the given generator as a source for randomness.

## Relationships

### Inherits From
- [CustomStringConvertible](./customstringconvertible.md)
- [Decodable](./decodable.md)
- [Encodable](./encodable.md)
- [Equatable](./equatable.md)
- [ExpressibleByArrayLiteral](./expressiblebyarrayliteral.md)
- [Hashable](./hashable.md)
- [SIMDStorage](./simdstorage.md)
### Conforming Types
- [SIMD16](./simd16.md)
- [SIMD2](./simd2.md)
- [SIMD3](./simd3.md)
- [SIMD32](./simd32.md)
- [SIMD4](./simd4.md)
- [SIMD64](./simd64.md)
- [SIMD8](./simd8.md)
- [SIMDMask](./simdmask.md)

## See Also

### Supporting Types
- [protocol SIMDScalar](./simdscalar.md)
  A type that can be used as an element in a SIMD vector.
- [protocol SIMDStorage](./simdstorage.md)
  A type that can function as storage for a SIMD vector type.
- [struct SIMDMask](./simdmask.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/simd)*
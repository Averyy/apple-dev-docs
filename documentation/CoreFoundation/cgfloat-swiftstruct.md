# CGFloat

**Framework**: Core Foundation  
**Kind**: struct

The basic type for floating-point scalar values in Core Graphics and related frameworks.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS ?+
- watchOS 1.0+

## Declaration

```swift
@frozen
struct CGFloat
```

#### Overview

The size and precision of this type depend on the CPU architecture. When you build for a 64-bit CPU, the [`CGFloat`](https://developer.apple.comhttps://developer.apple.com/library/archive/releasenotes/Foundation/RN-FoundationOlderNotes/index.html#//apple_ref/doc/uid/TP40008080-TRANSLATED_CHAPTER_965-TRANSLATED_DEST_121) type is a 64-bit, IEEE double-precision floating point type, equivalent to the [`Double`](https://developer.apple.com/documentation/Swift/Double) type. When you build for a 32-bit CPU, the [`CGFloat`](https://developer.apple.comhttps://developer.apple.com/library/archive/releasenotes/Foundation/RN-FoundationOlderNotes/index.html#//apple_ref/doc/uid/TP40008080-TRANSLATED_CHAPTER_965-TRANSLATED_DEST_121) type is a 32-bit, IEEE single-precision floating point type, equivalent to the [`Float`](https://developer.apple.com/documentation/Swift/Float) type.

## Topics

### Initializers
- [init()](cgfloat-swift.struct/init.md)
  Create an instance initialized to zero.
- [init(CGFloat)](cgfloat-swift.struct/init(_:)-7dkuk.md)
  Create an instance initialized to `value`.
- [init(NSNumber)](cgfloat-swift.struct/init(_:)-99gmf.md)
  Creates a new value, rounded to the closest possible representation.
- [init(bitPattern: UInt)](cgfloat-swift.struct/init(bitpattern:).md)
- [init?(exactly: NSNumber)](cgfloat-swift.struct/init(exactly:).md)
- [init(nan: CGFloat.RawSignificand, signaling: Bool)](cgfloat-swift.struct/init(nan:signaling:).md)
- [init(truncating: NSNumber)](cgfloat-swift.struct/init(truncating:).md)
### Instance Properties
- [var bitPattern: UInt](cgfloat-swift.struct/bitpattern.md)
- [var native: CGFloat.NativeType](cgfloat-swift.struct/native.md)
  The native value.
### Type Aliases
- [typealias NativeType](cgfloat-swift.struct/nativetype.md)
  The native type used to store the `CGFloat`.
### Default Implementations
- [CustomReflectable Implementations](cgfloat-swift.struct/customreflectable-implementations.md)
- [CustomStringConvertible Implementations](cgfloat-swift.struct/customstringconvertible-implementations.md)
- [ExpressibleByFloatLiteral Implementations](cgfloat-swift.struct/expressiblebyfloatliteral-implementations.md)
- [ExpressibleByIntegerLiteral Implementations](cgfloat-swift.struct/expressiblebyintegerliteral-implementations.md)
- [Hashable Implementations](cgfloat-swift.struct/hashable-implementations.md)
- [Strideable Implementations](cgfloat-swift.struct/strideable-implementations.md)

## Relationships

### Conforms To
- [AdditiveArithmetic](../Swift/AdditiveArithmetic.md)
- [Animatable](../SwiftUI/Animatable.md)
- [BinaryFloatingPoint](../Swift/BinaryFloatingPoint.md)
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [CVarArg](../Swift/CVarArg.md)
- [Comparable](../Swift/Comparable.md)
- [Copyable](../Swift/Copyable.md)
- [CustomReflectable](../Swift/CustomReflectable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByFloatLiteral](../Swift/ExpressibleByFloatLiteral.md)
- [ExpressibleByIntegerLiteral](../Swift/ExpressibleByIntegerLiteral.md)
- [FloatingPoint](../Swift/FloatingPoint.md)
- [Hashable](../Swift/Hashable.md)
- [Numeric](../Swift/Numeric.md)
- [Sendable](../Swift/Sendable.md)
- [SignedNumeric](../Swift/SignedNumeric.md)
- [Strideable](../Swift/Strideable.md)
- [VectorArithmetic](../SwiftUI/VectorArithmetic.md)

## See Also

- [struct CGAffineTransform](cgaffinetransform.md)
- [struct CGAffineTransformComponents](cgaffinetransformcomponents.md)
- [struct CGPoint](cgpoint.md)
- [struct CGRect](cgrect.md)
- [struct CGSize](cgsize.md)
  A structure that contains width and height values.
- [struct CGVector](cgvector.md)
  A structure that contains a two-dimensional vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cgfloat-swift.struct)*
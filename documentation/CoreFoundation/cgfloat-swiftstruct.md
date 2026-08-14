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

The size and precision of this type depend on the CPU architecture. When you build for a 64-bit CPU, the [`CGFloat`](https://developer.apple.comhttps://developer.apple.com/library/archive/releasenotes/Foundation/RN-FoundationOlderNotes/index.html#//apple_ref/doc/uid/TP40008080-TRANSLATED_CHAPTER_965-TRANSLATED_DEST_121) type is a 64-bit, IEEE double-precision floating point type, equivalent to the [`Double`](https://developer.apple.com/documentation/swift/double) type. When you build for a 32-bit CPU, the [`CGFloat`](https://developer.apple.comhttps://developer.apple.com/library/archive/releasenotes/Foundation/RN-FoundationOlderNotes/index.html#//apple_ref/doc/uid/TP40008080-TRANSLATED_CHAPTER_965-TRANSLATED_DEST_121) type is a 32-bit, IEEE single-precision floating point type, equivalent to the [`Float`](https://developer.apple.com/documentation/swift/float) type.

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
- [AdditiveArithmetic](../swift/additivearithmetic.md)
- [Animatable](../swiftui/animatable.md)
- [BinaryFloatingPoint](../swift/binaryfloatingpoint.md)
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [CVAttachmentValueRepresentable](../corevideo/cvattachmentvaluerepresentable.md)
- [CVarArg](../swift/cvararg.md)
- [Comparable](../swift/comparable.md)
- [Copyable](../swift/copyable.md)
- [CustomReflectable](../swift/customreflectable.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [ExpressibleByFloatLiteral](../swift/expressiblebyfloatliteral.md)
- [ExpressibleByIntegerLiteral](../swift/expressiblebyintegerliteral.md)
- [FloatingPoint](../swift/floatingpoint.md)
- [Hashable](../swift/hashable.md)
- [Numeric](../swift/numeric.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SignedNumeric](../swift/signednumeric.md)
- [Strideable](../swift/strideable.md)
- [VectorArithmetic](../swiftui/vectorarithmetic.md)

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
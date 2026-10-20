# CGFloat

**Framework**: Core Foundation  
**Kind**: struct  
**Role**: Structure

The basic type for floating-point scalar values in Core Graphics and related frameworks.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS
- watchOS 1.0+

## Declaration

```swift
@frozen
struct CGFloat
```

#### Overview

The size and precision of this type depend on the CPU architecture. When you build for a 64-bit CPU, the [CGFloat](https://developer.apple.com/library/archive/releasenotes/Foundation/RN-FoundationOlderNotes/index.html#//apple_ref/doc/uid/TP40008080-TRANSLATED_CHAPTER_965-TRANSLATED_DEST_121) type is a 64-bit, IEEE double-precision floating point type, equivalent to the [`Double`](../Swift/double.md) type. When you build for a 32-bit CPU, the [CGFloat](https://developer.apple.com/library/archive/releasenotes/Foundation/RN-FoundationOlderNotes/index.html#//apple_ref/doc/uid/TP40008080-TRANSLATED_CHAPTER_965-TRANSLATED_DEST_121) type is a 32-bit, IEEE single-precision floating point type, equivalent to the [`Float`](../Swift/float.md) type.

## Topics

### Initializers
- [init()](./cgfloat-swift.struct/init%28%29.md)
  Create an instance initialized to zero.
- [init(CGFloat)](./cgfloat-swift.struct/init%28_%29-7dkuk.md)
  Create an instance initialized to `value`.
- [init(NSNumber)](./cgfloat-swift.struct/init%28_%29-99gmf.md)
  Creates a new value, rounded to the closest possible representation.
- [init(bitPattern: UInt)](./cgfloat-swift.struct/init%28bitpattern%29.md)
- [init?(exactly: NSNumber)](./cgfloat-swift.struct/init%28exactly%29.md)
- [init(nan: CGFloat.RawSignificand, signaling: Bool)](./cgfloat-swift.struct/init%28nan,signaling%29.md)
- [init(truncating: NSNumber)](./cgfloat-swift.struct/init%28truncating%29.md)
### Instance Properties
- [var bitPattern: UInt](./cgfloat-swift.struct/bitpattern.md)
- [var native: CGFloat.NativeType](./cgfloat-swift.struct/native.md)
  The native value.
### Type Aliases
- [typealias NativeType](./cgfloat-swift.struct/nativetype.md)
  The native type used to store the `CGFloat`.
### Default Implementations
- [CustomReflectable Implementations](./cgfloat-swift.struct/customreflectable-implementations.md)
- [CustomStringConvertible Implementations](./cgfloat-swift.struct/customstringconvertible-implementations.md)
- [ExpressibleByFloatLiteral Implementations](./cgfloat-swift.struct/expressiblebyfloatliteral-implementations.md)
- [ExpressibleByIntegerLiteral Implementations](./cgfloat-swift.struct/expressiblebyintegerliteral-implementations.md)
- [Hashable Implementations](./cgfloat-swift.struct/hashable-implementations.md)
- [Strideable Implementations](./cgfloat-swift.struct/strideable-implementations.md)

## Relationships

### Conforms To
- [AdditiveArithmetic](../Swift/additivearithmetic.md)
- [Animatable](../SwiftUI/animatable.md)
- [BinaryFloatingPoint](../Swift/binaryfloatingpoint.md)
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [CVAttachmentValueRepresentable](../CoreVideo/cvattachmentvaluerepresentable.md)
- [CVarArg](../Swift/cvararg.md)
- [Comparable](../Swift/comparable.md)
- [Copyable](../Swift/copyable.md)
- [CustomReflectable](../Swift/customreflectable.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [ExpressibleByFloatLiteral](../Swift/expressiblebyfloatliteral.md)
- [ExpressibleByIntegerLiteral](../Swift/expressiblebyintegerliteral.md)
- [FloatingPoint](../Swift/floatingpoint.md)
- [Hashable](../Swift/hashable.md)
- [Numeric](../Swift/numeric.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SignedNumeric](../Swift/signednumeric.md)
- [Strideable](../Swift/strideable.md)
- [VectorArithmetic](../SwiftUI/vectorarithmetic.md)

## See Also

### Structures
- [struct CGAffineTransform](./cgaffinetransform.md)
- [struct CGAffineTransformComponents](./cgaffinetransformcomponents.md)
- [struct CGPoint](./cgpoint.md)
- [struct CGRect](./cgrect.md)
- [struct CGSize](./cgsize.md)
  A structure that contains width and height values.
- [struct CGVector](./cgvector.md)
  A structure that contains a two-dimensional vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cgfloat-swift.struct)*
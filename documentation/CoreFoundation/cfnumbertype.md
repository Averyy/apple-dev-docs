# CFNumberType

**Framework**: Core Foundation  
**Kind**: enum

Flags used by CFNumber to indicate the data type of a value.

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
enum CFNumberType
```

#### Overview

The type specified in the call to [`CFNumberCreate(_:_:_:)`](cfnumbercreate(_:_:_:).md) is not necessarily preserved when creating a new CFNumber object. A CFNumber object uses whatever internal storage type the creation function deems appropriate. Use the [`CFNumberGetType(_:)`](cfnumbergettype(_:).md) function to find out what type the CFNumber object used to store your value.

## Topics

### Constants
- [CFNumberType.sInt8Type](cfnumbertype/sint8type.md)
  Eight-bit, signed integer. The `SInt8` data type is defined in `MacTypes.h`.
- [CFNumberType.sInt16Type](cfnumbertype/sint16type.md)
  Sixteen-bit, signed integer. The `SInt16` data type is defined in `MacTypes.h`.
- [CFNumberType.sInt32Type](cfnumbertype/sint32type.md)
  Thirty-two-bit, signed integer. The `SInt32` data type is defined in `MacTypes.h`.
- [CFNumberType.sInt64Type](cfnumbertype/sint64type.md)
  Sixty-four-bit, signed integer. The `SInt64` data type is defined in `MacTypes.h`.
- [CFNumberType.float32Type](cfnumbertype/float32type.md)
  Thirty-two-bit real. The `Float32` data type is defined in `MacTypes.h`.
- [CFNumberType.float64Type](cfnumbertype/float64type.md)
  Sixty-four-bit real. The `Float64` data type is defined in `MacTypes.h` and conforms to the 64-bit IEEE 754 standard.
- [CFNumberType.charType](cfnumbertype/chartype.md)
  Basic C `char` type.
- [CFNumberType.shortType](cfnumbertype/shorttype.md)
  Basic C `short` type.
- [CFNumberType.intType](cfnumbertype/inttype.md)
  Basic C `int` type.
- [CFNumberType.longType](cfnumbertype/longtype.md)
  Basic C `long` type.
- [CFNumberType.longLongType](cfnumbertype/longlongtype.md)
  Basic C `long long` type.
- [CFNumberType.floatType](cfnumbertype/floattype.md)
  Basic C `float` type.
- [CFNumberType.doubleType](cfnumbertype/doubletype.md)
  Basic C `double` type.
- [CFNumberType.cfIndexType](cfnumbertype/cfindextype.md)
  CFIndex value.
- [CFNumberType.nsIntegerType](cfnumbertype/nsintegertype.md)
  `NSInteger` value.
- [CFNumberType.cgFloatType](cfnumbertype/cgfloattype.md)
  `CGFloat` value.
- [static var maxType: CFNumberType](cfnumbertype/maxtype.md)
  Same as [`CFNumberType.cgFloatType`](cfnumbertype/cgfloattype.md).
### Initializers
- [init?(rawValue: CFIndex)](cfnumbertype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Predefined Values](predefined-values.md)
  CFNumber provides some predefined number values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfnumbertype)*
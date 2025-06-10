# NSNumber

**Framework**: Foundation  
**Kind**: class

An object wrapper for primitive scalar numeric values.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class NSNumber
```

## Mentions

- [Implementing Handoff in Your App](implementing-handoff-in-your-app.md)

#### Overview

`NSNumber` is a subclass of `NSValue` that offers a value as any C scalar (numeric) type. It defines a set of methods specifically for setting and accessing the value as a signed or unsigned `char`, `short int`, `int`, `long int`, `long long int`, `float`, or `double` or as a `BOOL`. (Note that number objects do not necessarily preserve the type they are created with.) It also defines a [`compare(_:)`](nsnumber/compare(_:).md) method to determine the ordering of two `NSNumber` objects.

`NSNumber` is “toll-free bridged” with its Core Foundation counterparts: [`CFNumber`](https://developer.apple.com/documentation/CoreFoundation/CFNumber) for integer and floating point values, and [`CFBoolean`](https://developer.apple.com/documentation/CoreFoundation/CFBoolean) for Boolean values. See [`Toll-Free Bridging`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/Toll-FreeBridgin/Toll-FreeBridgin.html#//apple_ref/doc/uid/TP40010810-CH2) for more information on toll-free bridging.

##### Value Conversions

`NSNumber` provides readonly properties that return the object’s stored value converted to a particular Boolean, integer, unsigned integer, or floating point C scalar type. Because numeric types have different storage capabilities, attempting to initialize with a value of one type and access the value of another type may produce an erroneous result—for example, initializing with a `double` value exceeding `FLT_MAX` and accessing its [`floatValue`](nsnumber/floatvalue.md), or initializing with an negative integer value and accessing its [`uintValue`](nsnumber/uintvalue.md). In some cases, attempting to initialize with a value of a type and access the value of another type may result in loss of precision—for example, initializing with a `double` value with many significant digits and accessing its [`floatValue`](nsnumber/floatvalue.md), or initializing with a large integer value and accessing its [`int8Value`](nsnumber/int8value.md).

An `NSNumber` object initialized with a value of a particular type accessing the converted value of a different  of type, such as `unsigned int` and `float`, will convert its stored value to that converted type in the following ways:

| `Value` | [`boolValue`](nsnumber/boolvalue.md) | [`intValue`](nsnumber/intvalue-95zzp.md) | [`uintValue`](nsnumber/uintvalue.md) | [`floatValue`](nsnumber/floatvalue.md) |
| --- | --- | --- | --- | --- |
| [`false`](https://developer.apple.com/documentation/swift/false) | [`false`](https://developer.apple.com/documentation/swift/false) | `0` | `0` | `0.0` |
| [`true`](https://developer.apple.com/documentation/swift/true) | [`true`](https://developer.apple.com/documentation/swift/true) | `1` | `1` | `1.0` |

| `Value` | [`boolValue`](nsnumber/boolvalue.md) | [`intValue`](nsnumber/intvalue-95zzp.md) | [`uintValue`](nsnumber/uintvalue.md) | [`floatValue`](nsnumber/floatvalue.md) |
| --- | --- | --- | --- | --- |
| `0` | [`false`](https://developer.apple.com/documentation/swift/false) | `0` | `0` | `0.0` |
| `1` | [`true`](https://developer.apple.com/documentation/swift/true) | `1` | `1` | `1.0` |
| `-1` | [`true`](https://developer.apple.com/documentation/swift/true) | `-1` |  | `-1.0` |

| `Value` | [`boolValue`](nsnumber/boolvalue.md) | [`intValue`](nsnumber/intvalue-95zzp.md) | [`uintValue`](nsnumber/uintvalue.md) | [`floatValue`](nsnumber/floatvalue.md) |
| --- | --- | --- | --- | --- |
| `0` | [`false`](https://developer.apple.com/documentation/swift/false) | `0` | `0` | `0.0` |
| `1` | [`true`](https://developer.apple.com/documentation/swift/true) | `1` | `1` | `1.0` |

| `Value` | [`boolValue`](nsnumber/boolvalue.md) | [`intValue`](nsnumber/intvalue-95zzp.md) | [`uintValue`](nsnumber/uintvalue.md) | [`floatValue`](nsnumber/floatvalue.md) |
| --- | --- | --- | --- | --- |
| `0.0` | [`false`](https://developer.apple.com/documentation/swift/false) | `0` | `0` | `0.0` |
| `1.0` | [`true`](https://developer.apple.com/documentation/swift/true) | `1` | `1` | `1.0` |
| `-1.0` | [`true`](https://developer.apple.com/documentation/swift/true) | `-1` |  | `-1.0` |

##### Subclassing Notes

As with any class cluster, subclasses of `NSNumber` must override the primitive methods of its superclass, `NSValue`. In addition, there are two requirements around the data type your subclass represents:

1. Your implementation of [`objCType`](nsvalue/objctype.md) must return one of “`c`”, “`C`”, “`s`”, “`S`”, “`i`”, “`I`”, “`l`”, “`L`”, “`q`”, “`Q`”, “`f`”, and “`d`”. This is required for the other methods of [`NSNumber`](nsnumber.md) to behave correctly.
2. Your subclass must override the accessor method that corresponds to the declared type—for example, if your implementation of [`objCType`](nsvalue/objctype.md) returns  “`i`”, you must override [`int32Value`](nsnumber/int32value.md).

## Topics

### Initializing an NSNumber Object
- [init(value: Bool)](nsnumber/init(value:)-1ojz2.md)
  Returns an `NSNumber` object initialized to contain a given value, treated as a `BOOL`.
- [init(value: CChar)](nsnumber/init(value:)-8krjs.md)
  Returns an `NSNumber` object initialized to contain a given value, treated as a signed `char`.
- [init(value: Double)](nsnumber/init(value:)-15chk.md)
  Returns an `NSNumber` object initialized to contain `value`, treated as a `double`.
- [init(value: Float)](nsnumber/init(value:)-2vlwk.md)
  Returns an `NSNumber` object initialized to contain a given value, treated as a `float`.
- [init(value: Int32)](nsnumber/init(value:)-7jvmg.md)
  Returns an `NSNumber` object initialized to contain a given value, treated as a signed `int`.
- [init(value: Int)](nsnumber/init(value:)-5jcjl.md)
  Returns an `NSNumber` object initialized to contain a given value, treated as an `NSInteger`.
- [init(value: Int64)](nsnumber/init(value:)-40ad0.md)
  Returns an `NSNumber` object initialized to contain `value`, treated as a signed `long long`.
- [init(value: Int16)](nsnumber/init(value:)-16drx.md)
  Returns an `NSNumber` object initialized to contain a given value, treated as a signed `short`.
- [init(value: UInt8)](nsnumber/init(value:)-8se67.md)
  Returns an `NSNumber` object initialized to contain a given value, treated as an `unsigned char`.
- [init(value: UInt32)](nsnumber/init(value:)-47coa.md)
  Returns an `NSNumber` object initialized to contain a given value, treated as an `unsigned int`.
- [init(value: UInt)](nsnumber/init(value:)-3l4ek.md)
  Returns an `NSNumber` object initialized to contain a given value, treated as an `NSUInteger`.
- [init(value: UInt64)](nsnumber/init(value:)-43lc7.md)
  Returns an `NSNumber` object initialized to contain a given value, treated as an `unsigned long long`.
- [init(value: UInt16)](nsnumber/init(value:)-87y9m.md)
  Returns an `NSNumber` object initialized to contain a given value, treated as an `unsigned short`.
### Accessing Numeric Values
- [var boolValue: Bool](nsnumber/boolvalue.md)
  The number object’s value expressed as a Boolean value.
- [var int8Value: CChar](nsnumber/int8value.md)
  The number object’s value expressed as a `char`.
- [var decimalValue: Decimal](nsnumber/decimalvalue.md)
  The number object’s value expressed as an [`Decimal`](decimal.md) structure.
- [var doubleValue: Double](nsnumber/doublevalue.md)
  The number object’s value expressed as a `double`, converted as necessary.
- [var floatValue: Float](nsnumber/floatvalue.md)
  The number object’s value expressed as a `float`, converted as necessary.
- [var int32Value: Int32](nsnumber/int32value.md)
  The number object’s value expressed as an `int`, converted as necessary.
- [var intValue: Int](nsnumber/intvalue-95zzp.md)
  The number object’s value expressed as an `NSInteger` object, converted as necessary.
- [var int64Value: Int64](nsnumber/int64value.md)
  The number object’s value expressed as a `long long`, converted as necessary.
- [var int16Value: Int16](nsnumber/int16value.md)
  The number object’s value expressed as a `short`, converted as necessary.
- [var uint8Value: UInt8](nsnumber/uint8value.md)
  The number object’s value expressed as an unsigned `char`, converted as necessary.
- [var uintValue: UInt](nsnumber/uintvalue.md)
  The number object’s value expressed as an `NSUInteger` object, converted as necessary.
- [var uint32Value: UInt32](nsnumber/uint32value.md)
  The number object’s value expressed as an unsigned `int`, converted as necessary.
- [var uint64Value: UInt64](nsnumber/uint64value.md)
  The number object’s value expressed as an unsigned `long long`, converted as necessary.
- [var uint16Value: UInt16](nsnumber/uint16value.md)
  The number object’s value expressed as an unsigned `short`, converted as necessary.
### Retrieving String Representations
- [func description(withLocale: Any?) -> String](nsnumber/description(withlocale:).md)
  Returns a string that represents the contents of the number object for a given locale.
- [var stringValue: String](nsnumber/stringvalue.md)
  The number object’s value expressed as a human-readable string.
### Comparing NSNumber Objects
- [func compare(NSNumber) -> ComparisonResult](nsnumber/compare(_:).md)
  Returns an `NSComparisonResult` value that indicates whether the number object’s value is greater than, equal to, or less than a given number.
- [func isEqual(to: NSNumber) -> Bool](nsnumber/isequal(to:).md)
  Returns a Boolean value that indicates whether the number object’s value and a given number are equal.
### Number Validation
- [func NSDecimalIsNotANumber(UnsafePointer<Decimal>) -> Bool](nsdecimalisnotanumber(_:).md)
  Returns a Boolean that indicates whether a given decimal contains a valid number.
### Initializers
- [init?(coder: NSCoder)](nsnumber/init(coder:).md)
### Default Implementations
- [ExpressibleByBooleanLiteral Implementations](nsnumber/expressiblebybooleanliteral-implementations.md)
- [ExpressibleByFloatLiteral Implementations](nsnumber/expressiblebyfloatliteral-implementations.md)
- [ExpressibleByIntegerLiteral Implementations](nsnumber/expressiblebyintegerliteral-implementations.md)

## Relationships

### Inherits From
- [NSValue](nsvalue.md)
### Inherited By
- [NSDecimalNumber](nsdecimalnumber.md)
### Conforms To
- [CKRecordValue](../CloudKit/CKRecordValue-c.protocol.md)
- [CKRecordValueProtocol](../CloudKit/CKRecordValueProtocol.md)
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByBooleanLiteral](../Swift/ExpressibleByBooleanLiteral.md)
- [ExpressibleByFloatLiteral](../Swift/ExpressibleByFloatLiteral.md)
- [ExpressibleByIntegerLiteral](../Swift/ExpressibleByIntegerLiteral.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](nscoding.md)
- [NSCopying](nscopying.md)
- [NSFetchRequestResult](../CoreData/NSFetchRequestResult.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](nssecurecoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnumber)*
# NSNumber

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

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

```objc
@interface NSNumber : NSValue
```

## Mentions

- [Implementing Handoff in Your App](./implementing-handoff-in-your-app.md)

#### Overview

`NSNumber` is a subclass of `NSValue` that offers a value as any C scalar (numeric) type. It defines a set of methods specifically for setting and accessing the value as a signed or unsigned `char`, `short int`, `int`, `long int`, `long long int`, `float`, or `double` or as a `BOOL`. (Note that number objects do not necessarily preserve the type they are created with.) It also defines a [`compare(_:)`](./nsnumber/compare%28_%29.md) method to determine the ordering of two `NSNumber` objects.

`NSNumber` is “toll-free bridged” with its Core Foundation counterparts: [`CFNumber`](../CoreFoundation/cfnumber.md) for integer and floating point values, and [`CFBoolean`](../CoreFoundation/cfboolean.md) for Boolean values. See [Toll-Free Bridging](https://developer.apple.com/library/archive/documentation/General/Conceptual/CocoaEncyclopedia/Toll-FreeBridgin/Toll-FreeBridgin.html#//apple_ref/doc/uid/TP40010810-CH2) for more information on toll-free bridging.

##### Value Conversions

`NSNumber` provides readonly properties that return the object’s stored value converted to a particular Boolean, integer, unsigned integer, or floating point C scalar type. Because numeric types have different storage capabilities, attempting to initialize with a value of one type and access the value of another type may produce an erroneous result—for example, initializing with a `double` value exceeding `FLT_MAX` and accessing its [`floatValue`](./nsnumber/floatvalue.md), or initializing with an negative integer value and accessing its [`uintValue`](./nsnumber/uintvalue.md). In some cases, attempting to initialize with a value of a type and access the value of another type may result in loss of precision—for example, initializing with a `double` value with many significant digits and accessing its [`floatValue`](./nsnumber/floatvalue.md), or initializing with a large integer value and accessing its [`int8Value`](./nsnumber/int8value.md).

An `NSNumber` object initialized with a value of a particular type accessing the converted value of a different *kind* of type, such as `unsigned int` and `float`, will convert its stored value to that converted type in the following ways:

| `Value` | [`boolValue`](./nsnumber/boolvalue.md) | [`intValue`](./nsnumber/intvalue-95zzp.md) | [`uintValue`](./nsnumber/uintvalue.md) | [`floatValue`](./nsnumber/floatvalue.md) |
| --- | --- | --- | --- | --- |
| [`false`](../Swift/false.md) | [`false`](../Swift/false.md) | `0` | `0` | `0.0` |
| [`true`](../Swift/true.md) | [`true`](../Swift/true.md) | `1` | `1` | `1.0` |

| `Value` | [`boolValue`](./nsnumber/boolvalue.md) | [`intValue`](./nsnumber/intvalue-95zzp.md) | [`uintValue`](./nsnumber/uintvalue.md) | [`floatValue`](./nsnumber/floatvalue.md) |
| --- | --- | --- | --- | --- |
| `0` | [`false`](../Swift/false.md) | `0` | `0` | `0.0` |
| `1` | [`true`](../Swift/true.md) | `1` | `1` | `1.0` |
| `-1` | [`true`](../Swift/true.md) | `-1` | *invalid, erroneous result* | `-1.0` |

| `Value` | [`boolValue`](./nsnumber/boolvalue.md) | [`intValue`](./nsnumber/intvalue-95zzp.md) | [`uintValue`](./nsnumber/uintvalue.md) | [`floatValue`](./nsnumber/floatvalue.md) |
| --- | --- | --- | --- | --- |
| `0` | [`false`](../Swift/false.md) | `0` | `0` | `0.0` |
| `1` | [`true`](../Swift/true.md) | `1` | `1` | `1.0` |

| `Value` | [`boolValue`](./nsnumber/boolvalue.md) | [`intValue`](./nsnumber/intvalue-95zzp.md) | [`uintValue`](./nsnumber/uintvalue.md) | [`floatValue`](./nsnumber/floatvalue.md) |
| --- | --- | --- | --- | --- |
| `0.0` | [`false`](../Swift/false.md) | `0` | `0` | `0.0` |
| `1.0` | [`true`](../Swift/true.md) | `1` | `1` | `1.0` |
| `-1.0` | [`true`](../Swift/true.md) | `-1` | *invalid, erroneous result* | `-1.0` |

##### Subclassing Notes

As with any class cluster, subclasses of `NSNumber` must override the primitive methods of its superclass, `NSValue`. In addition, there are two requirements around the data type your subclass represents:

1. Your implementation of [`objCType`](./nsvalue/objctype.md) must return one of “`c`”, “`C`”, “`s`”, “`S`”, “`i`”, “`I`”, “`l`”, “`L`”, “`q`”, “`Q`”, “`f`”, and “`d`”. This is required for the other methods of [`NSNumber`](./nsnumber.md) to behave correctly.
2. Your subclass must override the accessor method that corresponds to the declared type—for example, if your implementation of [`objCType`](./nsvalue/objctype.md) returns  “`i`”, you must override [`int32Value`](./nsnumber/int32value.md).

## Topics

### Initializing an NSNumber Object
- [init(value: Bool)](./nsnumber/init%28value%29-1ojz2.md)
  Returns an `NSNumber` object initialized to contain a given value, treated as a `BOOL`.
- [init(value: CChar)](./nsnumber/init%28value%29-8krjs.md)
  Returns an `NSNumber` object initialized to contain a given value, treated as a signed `char`.
- [init(value: Double)](./nsnumber/init%28value%29-15chk.md)
  Returns an `NSNumber` object initialized to contain `value`, treated as a `double`.
- [init(value: Float)](./nsnumber/init%28value%29-2vlwk.md)
  Returns an `NSNumber` object initialized to contain a given value, treated as a `float`.
- [init(value: Int32)](./nsnumber/init%28value%29-7jvmg.md)
  Returns an `NSNumber` object initialized to contain a given value, treated as a signed `int`.
- [init(value: Int)](./nsnumber/init%28value%29-5jcjl.md)
  Returns an `NSNumber` object initialized to contain a given value, treated as an `NSInteger`.
- [init(value: Int64)](./nsnumber/init%28value%29-40ad0.md)
  Returns an `NSNumber` object initialized to contain `value`, treated as a signed `long long`.
- [init(value: Int16)](./nsnumber/init%28value%29-16drx.md)
  Returns an `NSNumber` object initialized to contain a given value, treated as a signed `short`.
- [init(value: UInt8)](./nsnumber/init%28value%29-8se67.md)
  Returns an `NSNumber` object initialized to contain a given value, treated as an `unsigned char`.
- [init(value: UInt32)](./nsnumber/init%28value%29-47coa.md)
  Returns an `NSNumber` object initialized to contain a given value, treated as an `unsigned int`.
- [init(value: UInt)](./nsnumber/init%28value%29-3l4ek.md)
  Returns an `NSNumber` object initialized to contain a given value, treated as an `NSUInteger`.
- [init(value: UInt64)](./nsnumber/init%28value%29-43lc7.md)
  Returns an `NSNumber` object initialized to contain a given value, treated as an `unsigned long long`.
- [init(value: UInt16)](./nsnumber/init%28value%29-87y9m.md)
  Returns an `NSNumber` object initialized to contain a given value, treated as an `unsigned short`.
- [- initWithLong:](./nsnumber/initwithlong_.md)
  Returns an `NSNumber` object initialized to contain a given value, treated as a signed `long`.
- [- initWithUnsignedLong:](./nsnumber/initwithunsignedlong_.md)
  Returns an `NSNumber` object initialized to contain a given value, treated as an `unsigned long`.
### Accessing Numeric Values
- [var boolValue: Bool](./nsnumber/boolvalue.md)
  The number object’s value expressed as a Boolean value.
- [var int8Value: CChar](./nsnumber/int8value.md)
  The number object’s value expressed as a `char`.
- [var decimalValue: Decimal](./nsnumber/decimalvalue.md)
  The number object’s value expressed as an [`Decimal`](./decimal.md) structure.
- [var doubleValue: Double](./nsnumber/doublevalue.md)
  The number object’s value expressed as a `double`, converted as necessary.
- [var floatValue: Float](./nsnumber/floatvalue.md)
  The number object’s value expressed as a `float`, converted as necessary.
- [var int32Value: Int32](./nsnumber/int32value.md)
  The number object’s value expressed as an `int`, converted as necessary.
- [var intValue: Int](./nsnumber/intvalue-95zzp.md)
  The number object’s value expressed as an `NSInteger` object, converted as necessary.
- [var int64Value: Int64](./nsnumber/int64value.md)
  The number object’s value expressed as a `long long`, converted as necessary.
- [var int16Value: Int16](./nsnumber/int16value.md)
  The number object’s value expressed as a `short`, converted as necessary.
- [var uint8Value: UInt8](./nsnumber/uint8value.md)
  The number object’s value expressed as an unsigned `char`, converted as necessary.
- [var uintValue: UInt](./nsnumber/uintvalue.md)
  The number object’s value expressed as an `NSUInteger` object, converted as necessary.
- [var uint32Value: UInt32](./nsnumber/uint32value.md)
  The number object’s value expressed as an unsigned `int`, converted as necessary.
- [var uint64Value: UInt64](./nsnumber/uint64value.md)
  The number object’s value expressed as an unsigned `long long`, converted as necessary.
- [var uint16Value: UInt16](./nsnumber/uint16value.md)
  The number object’s value expressed as an unsigned `short`, converted as necessary.
- [longValue](./nsnumber/longvalue.md)
  The number object’s value expressed as a `long`, converted as necessary.
- [unsignedLongValue](./nsnumber/unsignedlongvalue.md)
  The number object’s value expressed as an unsigned `long`, converted as necessary.
### Retrieving String Representations
- [func description(withLocale: Any?) -> String](./nsnumber/description%28withlocale%29.md)
  Returns a string that represents the contents of the number object for a given locale.
- [var stringValue: String](./nsnumber/stringvalue.md)
  The number object’s value expressed as a human-readable string.
### Comparing NSNumber Objects
- [func compare(NSNumber) -> ComparisonResult](./nsnumber/compare%28_%29.md)
  Returns an `NSComparisonResult` value that indicates whether the number object’s value is greater than, equal to, or less than a given number.
- [func isEqual(to: NSNumber) -> Bool](./nsnumber/isequal%28to%29.md)
  Returns a Boolean value that indicates whether the number object’s value and a given number are equal.
### Number Validation
- [func NSDecimalIsNotANumber(UnsafePointer<Decimal>) -> Bool](./nsdecimalisnotanumber%28_%29.md)
  Returns a Boolean that indicates whether a given decimal contains a valid number.
### Initializers
- [init(bool: Bool)](./nsnumber/init%28bool%29.md)
- [init(char: CChar)](./nsnumber/init%28char%29.md)
- [init?(coder: NSCoder)](./nsnumber/init%28coder%29.md)
- [init(double: Double)](./nsnumber/init%28double%29.md)
- [init(float: Float)](./nsnumber/init%28float%29.md)
- [init(int: Int32)](./nsnumber/init%28int%29.md)
- [init(integer: Int)](./nsnumber/init%28integer%29.md)
- [init(longLong: Int64)](./nsnumber/init%28longlong%29.md)
- [init(short: Int16)](./nsnumber/init%28short%29.md)
- [init(unsignedChar: UInt8)](./nsnumber/init%28unsignedchar%29.md)
- [init(unsignedInt: UInt32)](./nsnumber/init%28unsignedint%29.md)
- [init(unsignedInteger: UInt)](./nsnumber/init%28unsignedinteger%29.md)
- [init(unsignedLongLong: UInt64)](./nsnumber/init%28unsignedlonglong%29.md)
- [init(unsignedShort: UInt16)](./nsnumber/init%28unsignedshort%29.md)
### Default Implementations
- [ExpressibleByBooleanLiteral Implementations](./nsnumber/expressiblebybooleanliteral-implementations.md)
- [ExpressibleByFloatLiteral Implementations](./nsnumber/expressiblebyfloatliteral-implementations.md)
- [ExpressibleByIntegerLiteral Implementations](./nsnumber/expressiblebyintegerliteral-implementations.md)
### Creating an NSNumber Object
- [+ numberWithBool:](./nsnumber/numberwithbool_.md)
  Creates and returns an `NSNumber` object containing a given value, treating it as a `BOOL`.
- [+ numberWithChar:](./nsnumber/numberwithchar_.md)
  Creates and returns an `NSNumber` object containing a given value, treating it as a signed `char`.
- [+ numberWithDouble:](./nsnumber/numberwithdouble_.md)
  Creates and returns an `NSNumber` object containing a given value, treating it as a `double`.
- [+ numberWithFloat:](./nsnumber/numberwithfloat_.md)
  Creates and returns an `NSNumber` object containing a given value, treating it as a `float`.
- [+ numberWithInt:](./nsnumber/numberwithint_.md)
  Creates and returns an `NSNumber` object containing a given value, treating it as a signed `int`.
- [+ numberWithInteger:](./nsnumber/numberwithinteger_.md)
  Creates and returns an `NSNumber` object containing a given value, treating it as an `NSInteger`.
- [+ numberWithLong:](./nsnumber/numberwithlong_.md)
  Creates and returns an `NSNumber` object containing a given value, treating it as a signed `long`.
- [+ numberWithLongLong:](./nsnumber/numberwithlonglong_.md)
  Creates and returns an `NSNumber` object containing a given value, treating it as a signed `long long`.
- [+ numberWithShort:](./nsnumber/numberwithshort_.md)
  Creates and returns an `NSNumber` object containing `value`, treating it as a signed `short`.
- [+ numberWithUnsignedChar:](./nsnumber/numberwithunsignedchar_.md)
  Creates and returns an `NSNumber` object containing a given value, treating it as an `unsigned char`.
- [+ numberWithUnsignedInt:](./nsnumber/numberwithunsignedint_.md)
  Creates and returns an `NSNumber` object containing a given value, treating it as an `unsigned int`.
- [+ numberWithUnsignedInteger:](./nsnumber/numberwithunsignedinteger_.md)
  Creates and returns an `NSNumber` object containing a given value, treating it as an `NSUInteger`.
- [+ numberWithUnsignedLong:](./nsnumber/numberwithunsignedlong_.md)
  Creates and returns an `NSNumber` object containing a given value, treating it as an `unsigned long`.
- [+ numberWithUnsignedLongLong:](./nsnumber/numberwithunsignedlonglong_.md)
  Creates and returns an `NSNumber` object containing a given value, treating it as an `unsigned long long`.
- [+ numberWithUnsignedShort:](./nsnumber/numberwithunsignedshort_.md)
  Creates and returns an `NSNumber` object containing a given value, treating it as an `unsigned short`.

## Relationships

### Inherits From
- [NSValue](./nsvalue.md)
### Inherited By
- [NSDecimalNumber](./nsdecimalnumber.md)
### Conforms To
- [CKRecordValue](../CloudKit/ckrecordvalue-c.protocol.md)
- [CKRecordValueProtocol](../CloudKit/ckrecordvalueprotocol.md)
- [CVarArg](../Swift/cvararg.md)
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [ExpressibleByBooleanLiteral](../Swift/expressiblebybooleanliteral.md)
- [ExpressibleByFloatLiteral](../Swift/expressiblebyfloatliteral.md)
- [ExpressibleByIntegerLiteral](../Swift/expressiblebyintegerliteral.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](./nscoding.md)
- [NSCopying](./nscopying.md)
- [NSFetchRequestResult](../CoreData/nsfetchrequestresult.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](./nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Numbers
- [NSInteger](../ObjectiveC/nsinteger.md)
  Describes an integer.
- [NSUInteger](../ObjectiveC/nsuinteger.md)
  Describes an unsigned integer.
- [NSDecimal](./decimal.md)
  A structure representing a base-10 number.
- [NSDecimalNumber](./nsdecimalnumber.md)
  An object for representing and performing arithmetic on base-10 numbers.
- [NSNumberFormatter](./numberformatter.md)
  A formatter that converts between numeric values and their textual representations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsnumber)*
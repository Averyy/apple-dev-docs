# ValueNotConvertibleToTypeError

**Framework**: CKTool JS  
**Kind**: class

The base class of errors related to type validation or coercion.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
interface ValueNotConvertibleToTypeError
```

#### Overview

Extends `ValidationError`.

## Topics

### Instance Properties
- [typeDescription](valuenotconvertibletotypeerror/typedescription.md)
  The name of the type that the value should have been.
- [value](valuenotconvertibletotypeerror/value.md)
  The value that failed validation.

## Relationships

### Inherits From
- [LengthNotNumericError](lengthnotnumericerror.md)
- [ValueNotArrayBufferError](valuenotarraybuffererror.md)
- [ValueNotArrayError](valuenotarrayerror.md)
- [ValueNotBase64StringError](valuenotbase64stringerror.md)
- [ValueNotBlobError](valuenotbloberror.md)
- [ValueNotBooleanError](valuenotbooleanerror.md)
- [ValueNotByteArrayError](valuenotbytearrayerror.md)
- [ValueNotByteError](valuenotbyteerror.md)
- [ValueNotDateError](valuenotdateerror.md)
- [ValueNotDateStringError](valuenotdatestringerror.md)
- [ValueNotDoubleError](valuenotdoubleerror.md)
- [ValueNotEnumValueError](valuenotenumvalueerror.md)
- [ValueNotFloatError](valuenotfloaterror.md)
- [ValueNotFunctionError](valuenotfunctionerror.md)
- [ValueNotInt32Error](valuenotint32error.md)
- [ValueNotInt64Error](valuenotint64error.md)
- [ValueNotJsonError](valuenotjsonerror.md)
- [ValueNotNumericError](valuenotnumericerror.md)
- [ValueNotStringError](valuenotstringerror.md)
- [ValueNotUuidError](valuenotuuiderror.md)
### Inherited By
- [ValidationError](validationerror.md)

## See Also

- [ValidationError](validationerror.md)
  The base class of errors emitted when validators fail validation.
- [ArrayError](arrayerror.md)
  An error an array validator emits when an array’s elements fail validation.
- [MaxValueNotNumericError](maxvaluenotnumericerror.md)
  An error a validator emits when the maximum value given isn’t numeric.
- [MinValueNotNumericError](minvaluenotnumericerror.md)
  An error a validator emits when the minimum value given isn’t numeric.
- [ValueIsRequiredError](valueisrequirederror.md)
  The error emitted when a value is required but a validator determines the value is not present.
- [ValueNotFunctionError](valuenotfunctionerror.md)
  An error a validator emits when a value isn’t a function.
- [ValueNotArrayBufferError](valuenotarraybuffererror.md)
  An error a validator emits when a value isn’t an `ArrayBuffer`.
- [ValueNotArrayError](valuenotarrayerror.md)
  An error a validator emits when a value isn’t an array.
- [ValueNotBase64StringError](valuenotbase64stringerror.md)
  An error a validator emits when a value isn’t a `Base64` string or isn’t castable to that type.
- [ValueNotBlobError](valuenotbloberror.md)
  An error a validator emits when a value isn’t a `Blob`.
- [ValueNotBooleanError](valuenotbooleanerror.md)
  An error a validator emits when a value isn’t a Boolean or isn’t castable to that type.
- [ValueNotByteArrayError](valuenotbytearrayerror.md)
  An error a validator emits when a value isn’t a `ByteArray` or isn’t castable to that type.
- [ValueNotByteError](valuenotbyteerror.md)
  An error a validator emits when a value isn’t a `Byte` or isn’t castable to that type.
- [ValueNotDateError](valuenotdateerror.md)
  An error a validator emits when a value isn’t a `Date` or isn’t castable to that type.
- [ValueNotDateStringError](valuenotdatestringerror.md)
  An error a validator emits when a value isn’t a date string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/valuenotconvertibletotypeerror)*
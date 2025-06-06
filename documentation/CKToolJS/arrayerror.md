# ArrayError

**Framework**: CKTool JS  
**Kind**: class

An error an array validator emits when an array’s elements fail validation.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
interface ArrayError
```

#### Overview

Extends `ValidationError`. The indices of the elements that failed validation are in the `indices` member. The `errors` array has the errors that correspond to the elements identified by the `indices` member.

## Topics

### Instance Properties
- [array](arrayerror/array.md)
  The array that failed validation.
- [errors](arrayerror/errors.md)
  An array of errors that correspond to indexes.
- [indices](arrayerror/indices.md)
  An array of indexes of elements that failed validation in the array.

## Relationships

### Inherited By
- [ValidationError](validationerror.md)

## See Also

- [ValidationError](validationerror.md)
  The base class of errors emitted when validators fail validation.
- [MaxValueNotNumericError](maxvaluenotnumericerror.md)
  An error a validator emits when the maximum value given isn’t numeric.
- [MinValueNotNumericError](minvaluenotnumericerror.md)
  An error a validator emits when the minimum value given isn’t numeric.
- [ValueIsRequiredError](valueisrequirederror.md)
  The error emitted when a value is required but a validator determines the value is not present.
- [ValueNotConvertibleToTypeError](valuenotconvertibletotypeerror.md)
  The base class of errors related to type validation or coercion.
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

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/arrayerror)*
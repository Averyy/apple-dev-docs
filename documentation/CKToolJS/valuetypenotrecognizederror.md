# ValueTypeNotRecognizedError

**Framework**: CKTool JS  
**Kind**: class

An error that a deserializer emits when it fails to recognize the type of object to deserialize or process.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
interface ValueTypeNotRecognizedError
```

#### Overview

Extends `ValidationError`.

## Topics

### Instance Properties
- [discriminator](valuetypenotrecognizederror/discriminator.md)
  The object’s type identifier.
- [obj](valuetypenotrecognizederror/obj.md)
  The object that failed validation.

## Relationships

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/valuetypenotrecognizederror)*
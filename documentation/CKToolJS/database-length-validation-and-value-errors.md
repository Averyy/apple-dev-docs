# Database, Length, Validation, and Value Errors

**Framework**: CKTool JS

## Topics

### Database Errors
- [AuthenticationRequiredError](authenticationrequirederror.md)
  An object that represents an error that occurs when authentication information is missing for the current user.
- [CKDBBatchDeleteError](ckdbbatchdeleteerror.md)
  An object that represents an error that may occur when deleting a resource as part of a batch delete operation.
- [RequestError](requesterror.md)
  An object that represents a general error from the service.
### Length Errors
- [LengthError](lengtherror.md)
  The base class of length-related validation errors.
- [LengthGreaterThanMaxError](lengthgreaterthanmaxerror.md)
  An error a validator emits when the length property of the value given is greater than the allowed maximum.
- [LengthLessThanMinError](lengthlessthanminerror.md)
  An error a validator emits when the length property of the value given is less than the allowed minimum.
- [LengthNotNumericError](lengthnotnumericerror.md)
  An error a validator emits when the length property of a value isn’t numeric.
### Validation Errors
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
- [ValueNotDateStringError](valuenotdatestringerror.md)
  An error a validator emits when a value isn’t a date string.
- [ValueNotDoubleError](valuenotdoubleerror.md)
  An error a validator emits when a value isn’t a `Double` or isn’t castable to that type.
- [ValueNotEnumValueError](valuenotenumvalueerror.md)
  An error a validator emits when a value isn’t a valid enumeration value.
- [ValueNotFloatError](valuenotfloaterror.md)
  An error a validator emits when a value isn’t a `Float` or isn’t castable to that type.
- [ValueNotInt32Error](valuenotint32error.md)
  An error a validator emits when a value isn’t an `Int32` or isn’t castable to that type.
- [ValueNotInt64Error](valuenotint64error.md)
  An error a validator emits when a value isn’t an `Int64` or isn’t castable to that type.
- [ValueNotJsonError](valuenotjsonerror.md)
  An error a validator emits when a value isn’t JSON.
- [ValueNotNumericError](valuenotnumericerror.md)
  An error a validator emits when a value isn’t numeric.
- [ValueNotObjectError](valuenotobjecterror.md)
  An error a validator emits when a value isn’t an object.
- [ValueNotStringError](valuenotstringerror.md)
  An error a validator emits when a value isn’t a string.
- [ValueNotUuidError](valuenotuuiderror.md)
  An error a validator emits when a value isn’t a `Uuid` or isn’t castable to that type.
- [ValueTypeNotRecognizedError](valuetypenotrecognizederror.md)
  An error that a deserializer emits when it fails to recognize the type of object to deserialize or process.
### Value Range Errors
- [ValueRangeError](valuerangeerror.md)
  The base class of range-related validation errors.
- [ValueGreaterThanMaxNumberError](valuegreaterthanmaxnumbererror.md)
  An error a validator emits when a given value is greater than the allowed maximum.
- [ValueLessThanMinNumberError](valuelessthanminnumbererror.md)
  An error a validator emits when a given value is less than the allowed minimum.
- [ValueNotInNumberRangeError](valuenotinnumberrangeerror.md)
  An error a validator emits when a value can’t be represented by a JavaScript number due to being outside of the representable range.

## See Also

- [ErrorBase](errorbase.md)
  The base class of any error emitted by functions in the client library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/database-length-validation-and-value-errors)*
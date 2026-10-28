# LengthError

**Framework**: CKTool JS  
**Kind**: class  
**Role**: Class

The base class of length-related validation errors.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```
interface LengthError
```

## Overview

Extends `ValidationError`.

## Topics

### Instance Properties
- [value](./lengtherror/value.md)
  The length value that failed validation.

## Relationships

### Inherits From
- [LengthGreaterThanMaxError](./lengthgreaterthanmaxerror.md)
- [LengthLessThanMinError](./lengthlessthanminerror.md)
### Inherited By
- [ValidationError](./validationerror.md)

## See Also

### Length Errors
- [LengthGreaterThanMaxError](./lengthgreaterthanmaxerror.md)
  An error a validator emits when the length property of the value given is greater than the allowed maximum.
- [LengthLessThanMinError](./lengthlessthanminerror.md)
  An error a validator emits when the length property of the value given is less than the allowed minimum.
- [LengthNotNumericError](./lengthnotnumericerror.md)
  An error a validator emits when the length property of a value isn’t numeric.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/lengtherror)*
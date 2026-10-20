# ValueRangeError

**Framework**: CKTool JS  
**Kind**: class  
**Role**: Class

The base class of range-related validation errors.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```
interface ValueRangeError
```

#### Overview

Extends `ValidationError`.

## Topics

### Instance Properties
- [value](./valuerangeerror/value.md)
  The value that failed validation.

## Relationships

### Inherits From
- [ValueGreaterThanMaxNumberError](./valuegreaterthanmaxnumbererror.md)
- [ValueLessThanMinNumberError](./valuelessthanminnumbererror.md)
- [ValueNotInNumberRangeError](./valuenotinnumberrangeerror.md)
### Inherited By
- [ValidationError](./validationerror.md)

## See Also

### Value Range Errors
- [ValueGreaterThanMaxNumberError](./valuegreaterthanmaxnumbererror.md)
  An error a validator emits when a given value is greater than the allowed maximum.
- [ValueLessThanMinNumberError](./valuelessthanminnumbererror.md)
  An error a validator emits when a given value is less than the allowed minimum.
- [ValueNotInNumberRangeError](./valuenotinnumberrangeerror.md)
  An error a validator emits when a value can’t be represented by a JavaScript number due to being outside of the representable range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/valuerangeerror)*
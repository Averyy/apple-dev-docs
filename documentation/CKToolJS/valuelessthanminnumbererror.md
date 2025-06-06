# ValueLessThanMinNumberError

**Framework**: CKTool JS  
**Kind**: class

An error a validator emits when a given value is less than the allowed minimum.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
interface ValueLessThanMinNumberError
```

#### Overview

Extends `ValueRangeError`.

## Topics

### Instance Properties
- [minimum](valuelessthanminnumbererror/minimum.md)
  The minimum value (inclusive) for the tested length property.

## Relationships

### Inherited By
- [ValueRangeError](valuerangeerror.md)

## See Also

- [ValueRangeError](valuerangeerror.md)
  The base class of range-related validation errors.
- [ValueGreaterThanMaxNumberError](valuegreaterthanmaxnumbererror.md)
  An error a validator emits when a given value is greater than the allowed maximum.
- [ValueNotInNumberRangeError](valuenotinnumberrangeerror.md)
  An error a validator emits when a value can’t be represented by a JavaScript number due to being outside of the representable range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/valuelessthanminnumbererror)*
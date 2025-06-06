# ValueGreaterThanMaxNumberError

**Framework**: CKTool JS  
**Kind**: class

An error a validator emits when a given value is greater than the allowed maximum.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
interface ValueGreaterThanMaxNumberError
```

#### Overview

Extends `ValueRangeError`.

## Topics

### Instance Properties
- [maximum](valuegreaterthanmaxnumbererror/maximum.md)
  The maximum value (inclusive) for the tested length property.

## Relationships

### Inherited By
- [ValueRangeError](valuerangeerror.md)

## See Also

- [ValueRangeError](valuerangeerror.md)
  The base class of range-related validation errors.
- [ValueLessThanMinNumberError](valuelessthanminnumbererror.md)
  An error a validator emits when a given value is less than the allowed minimum.
- [ValueNotInNumberRangeError](valuenotinnumberrangeerror.md)
  An error a validator emits when a value can’t be represented by a JavaScript number due to being outside of the representable range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/valuegreaterthanmaxnumbererror)*
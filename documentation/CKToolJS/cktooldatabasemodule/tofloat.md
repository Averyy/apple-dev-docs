# toFloat

**Framework**: CKTool JS  
**Kind**: method

Converts a number or numeric string to a `Float`.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
static Float toFloat();
```

#### Return Value

If the value passes validation, this function returns a `Float`; otherwise it throws `ValueNotFloatError`. A value passes validation if it’s a number in the range of a single-precision 32-bit IEEE 754 floating-point value. `toFloat` can also accept a numeric string that represents a number that requires more precision than can be achieved with a JavaScript number.

#### Discussion

In TypeScript, `Float` is a branded `BigNumber` type. In JavaScript, it’s a `BigNumber`. `BigNumber` is from the bignumber.js package.

```javascript
import { toFloat } from "@apple/cktool.database";
```

## Parameters

- `value`: A numeric or numeric string to convert or validate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/cktooldatabasemodule/tofloat)*
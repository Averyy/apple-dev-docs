# toByte

**Framework**: CKTool JS  
**Kind**: method

Converts a numeric value to a `Byte`.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
static Byte toByte();
```

#### Return Value

If the value passes validation, this function returns a `Byte`; otherwise it throws `ValueNotByteError`. A numeric value passes validation if it’s an integer in the range 0 to 255, inclusive.

#### Discussion

In TypeScript, `Byte` is a branded number type. In JavaScript, it’s a number.

```javascript
import { toByte } from "@apple/cktool.database";
```

## Parameters

- `value`: A numeric value to convert or validate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/cktooldatabasemodule/tobyte)*
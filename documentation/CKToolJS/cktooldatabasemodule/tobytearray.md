# toByteArray

**Framework**: CKTool JS  
**Kind**: method

Converts a numeric array to a `ByteArray`.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
static ByteArray toByteArray();
```

#### Return Value

If the value passes validation, this function returns a `ByteArray`; otherwise it throws `ValueNotByteArrayError`. A numeric array passes validation if every element of the array is an integer in the range 0 to 255, inclusive.

#### Discussion

In TypeScript, `ByteArray` is a branded `Uint8Array` type. In JavaScript, it’s a `Uint8Array`.

```javascript
import { toByteArray } from "@apple/cktool.database";
```

## Parameters

- `value`: A numeric array to convert or validate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/cktooldatabasemodule/tobytearray)*
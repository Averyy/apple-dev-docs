# toInt32

**Framework**: CKTool JS  
**Kind**: method

Converts a number to an `Int32`.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
static Int32 toInt32();
```

#### Return Value

If the value passes validation, this function returns an `Int32`; otherwise it throws `ValueNotInt32Error`. A numeric value passes validation if it’s within signed 32-bit integer range.

#### Discussion

In TypeScript, `Int32` is a branded number type. In JavaScript, it’s a number.

```javascript
import { toInt32 } from "@apple/cktool.database";
```

## Parameters

- `value`: A number to convert or validate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/cktooldatabasemodule/toint32)*
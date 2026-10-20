# toNumber

**Framework**: CKTool JS  
**Kind**: method  
**Role**: Type Method

Converts a supported numeric type to a JavaScript number.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```
static number toNumber();
```

#### Discussion

If the value passed in isn’t a number, this function throws `ValueNotNumericError`. If the value is numeric but can’t be represented by a JavaScript number, it throws `ValueNotInNumberRangeError`.

```javascript
import { toNumber } from "@apple/cktool.database";
```

## Parameters

- `value`: A numeric value to convert or validate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/cktooldatabasemodule/tonumber)*
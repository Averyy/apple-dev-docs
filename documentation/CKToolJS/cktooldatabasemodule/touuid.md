# toUuid

**Framework**: CKTool JS  
**Kind**: method

Converts a string to a `Uuid`.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
static Uuid toUuid();
```

#### Return Value

If the value passes validation, this function returns a `Uuid`; otherwise it throws `ValueNotUuidError`. A string passes validation if it is a UUID string.

#### Discussion

In TypeScript, `Uuid` is a branded string type. In JavaScript, it’s a string.

```javascript
import { toUuid } from "@apple/cktool.database";
```

## Parameters

- `value`: A string to convert or validate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/cktooldatabasemodule/touuid)*
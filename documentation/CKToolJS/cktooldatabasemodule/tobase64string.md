# toBase64String

**Framework**: CKTool JS  
**Kind**: method

Converts a regular string to a `Base64String`.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
static Base64String toBase64String();
```

#### Return Value

If the value passes validation, this function returns a `Base64String`; otherwise it throws `ValueNotBase64StringError`. A string passes validation if it is a base 64 string.

#### Discussion

In TypeScript, `Base64String` is a branded string type. In JavaScript, it’s a string.

```javascript
import { toBase64String } from "@apple/cktool.database";
```

## Parameters

- `value`: A string value to convert or validate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/cktooldatabasemodule/tobase64string)*
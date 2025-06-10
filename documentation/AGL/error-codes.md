# Error Codes

**Framework**: AGL

Defines the error codes that can be returned by the [`aglGetError`](https://developer.apple.comhttps://developer.apple.com/library/archive/#id(F15037)) function.

#### Overview

Unlike many Carbon APIs, AGL functions don’t return result codes for specific error conditions. Instead, AGL functions that fail either return `GL_FALSE` or `NULL`. You can find out the specific nature of the error by calling the function [`aglGetError`](https://developer.apple.comhttps://developer.apple.com/library/archive/#id(F15037)), which returns the appropriate error code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/agl/error-codes)*
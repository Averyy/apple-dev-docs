# aglSetWindowRef

**Framework**: AGL  
**Kind**: func

Sets an AGL context to the specified window.

**Availability**:
- macOS 10.5+

## Declaration

```swift
extern GLboolean aglSetWindowRef(AGLContext ctx, WindowRef window);
```

#### Return Value

`true` if the window is successfully set; `false` otherwise.

## Parameters

- `ctx`: An AGL context.
- `window`: The window to set.

## See Also

- [aglGetWindowRef](aglgetwindowref.md)
  Retrieves the window associated with an AGL context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/agl/aglsetwindowref)*
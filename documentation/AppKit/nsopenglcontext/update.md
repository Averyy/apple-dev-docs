# update()

**Framework**: AppKit  
**Kind**: method

Updates the OpenGL context’s drawable object.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
func update()
```

#### Discussion

Call this method whenever the receiver’s drawable object changes size or location. A multithreaded application must synchronize all threads that access the same drawable object and call [`update()`](nsopenglcontext/update().md) for each thread’s context serially.

## See Also

- [var view: NSView?](nsopenglcontext/view.md)
  Returns the OpenGL context’s view.
- [func clearDrawable()](nsopenglcontext/cleardrawable.md)
  Disassociates the OpenGL context from its viewport.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglcontext/update())*
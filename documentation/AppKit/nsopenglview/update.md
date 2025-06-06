# update()

**Framework**: AppKit  
**Kind**: method

Called by Cocoa when the view’s window moves or when the view itself moves or is resized.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
func update()
```

#### Discussion

The default implementation simply calls the [`update()`](nsopenglcontext/update().md) method of [`NSOpenGLContext`](nsopenglcontext.md). You can override this method to perform additional update operations on the context or if you need to add locks for multithreaded access to multiple contexts.

## See Also

- [func reshape()](nsopenglview/reshape.md)
  Called by Cocoa when the view’s visible rectangle or bounds change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglview/update())*
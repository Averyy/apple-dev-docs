# reshape()

**Framework**: AppKit  
**Kind**: method

Called by Cocoa when the view’s visible rectangle or bounds change.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
func reshape()
```

#### Discussion

Cocoa typically calls this method during scrolling and resize operations but may call it in other situations when the view’s rectangles change. The default implementation does nothing. You can override this method if you need to adjust the viewport and display frustum.

## See Also

- [func update()](nsopenglview/update.md)
  Called by Cocoa when the view’s window moves or when the view itself moves or is resized.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglview/reshape())*
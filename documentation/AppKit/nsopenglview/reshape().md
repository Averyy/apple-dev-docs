# reshape()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Called by Cocoa when the view’s visible rectangle or bounds change.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

> **Deprecated**: Please use MTKView instead.

## Declaration

```swift
func reshape()
```

```objc
- (void) reshape;
```

#### Discussion

Cocoa typically calls this method during scrolling and resize operations but may call it in other situations when the view’s rectangles change. The default implementation does nothing. You can override this method if you need to adjust the viewport and display frustum.

## See Also

### Managing the Visible Region
- [func update()](./update%28%29.md)
  Called by Cocoa when the view’s window moves or when the view itself moves or is resized.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenglview/reshape())*
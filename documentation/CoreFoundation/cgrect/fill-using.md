# fill(using:)

**Framework**: Core Foundation  
**Kind**: method

Fills this rect in the current NSGraphicsContext in the context’s fill color. The compositing operation of the fill defaults to the context’s compositing operation, not necessarily using `.copy` like `NSRectFill()`.

**Availability**:
- macOS 10.9+
- Swift 4.0+

## Declaration

```swift
func fill(using operation: NSCompositingOperation = NSGraphicsContext.current?.compositingOperation ?? .sourceOver)
```

#### Discussion

> **Note**: There must be a set current NSGraphicsContext.

There must be a set current NSGraphicsContext.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cgrect/fill(using:))*
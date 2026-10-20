# flushGraphics()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Forces any buffered operations or data to be sent to the graphics context’s destination.

**Availability**:
- macOS

## Declaration

```swift
func flushGraphics()
```

```objc
- (void) flushGraphics;
```

#### Discussion

Graphics contexts use buffers to queue pending operations but for efficiency reasons may not always empty those buffers immediately. This method forces the buffers to be emptied.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgraphicscontext/flushgraphics())*
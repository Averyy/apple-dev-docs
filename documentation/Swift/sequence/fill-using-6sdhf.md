# fill(using:)

**Framework**: Swift  
**Kind**: method

Fills this list of rects in the current NSGraphicsContext with that rect’s associated gray component value in the DeviceGray color space. The compositing operation of the fill defaults to the context’s compositing operation, not necessarily using `.copy` like `NSRectFillListWithGrays()`.

**Availability**:
- macOS 10.9+
- Swift 4.0+

## Declaration

```swift
func fill(using operation: NSCompositingOperation = NSGraphicsContext.current?.compositingOperation ?? .sourceOver)
```

#### Discussion

> **Note**: There must be a set current NSGraphicsContext.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/sequence/fill(using:)-6sdhf)*
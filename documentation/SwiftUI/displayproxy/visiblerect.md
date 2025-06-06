# visibleRect

**Framework**: SwiftUI  
**Kind**: property

The portion of the display where it is safe to place windows.

**Availability**:
- macOS 15.0+

## Declaration

```swift
let visibleRect: CGRect
```

#### Discussion

On macOS, this area does not contain the space occupied by the dock and menu bar. Additionally, on Macs that include a camera housing in the bezel this rectangle does not include the bezel or visible areas to each side of the bezel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/displayproxy/visiblerect)*
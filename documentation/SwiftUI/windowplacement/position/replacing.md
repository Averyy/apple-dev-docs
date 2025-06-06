# replacing(_:)

**Framework**: SwiftUI  
**Kind**: method

Positions the window in the same spot as an existing window, hiding the old window in the process.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
static func replacing(_ relativeWindow: WindowProxy) -> WindowPlacement.Position
```

#### Discussion

This will position the new window in the same location as the specified existing window, and hide the old window. Closing the new window will then result in the original window being shown again.

## Parameters

- `relativeWindow`: The existing window that the new window   will replace.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/windowplacement/position/replacing(_:))*
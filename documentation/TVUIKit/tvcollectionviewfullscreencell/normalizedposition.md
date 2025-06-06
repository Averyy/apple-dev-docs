# normalizedPosition

**Framework**: TVUIKit  
**Kind**: property

The value that determines the current cell’s relative position on the screen.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
@MainActor
var normalizedPosition: CGFloat { get }
```

#### Discussion

A value of 0 indicates that the cell is positioned at the center of the collection view. A negative value indicates that the cell is positioned to the left of the center. A positive value indicates that the cell is positioned to the right of the center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvuikit/tvcollectionviewfullscreencell/normalizedposition)*
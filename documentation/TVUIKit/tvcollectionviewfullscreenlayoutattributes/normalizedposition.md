# normalizedPosition

**Framework**: TVUIKit  
**Kind**: property

A value that indicates the distance of the current cell from the collection view’s center cell.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
@MainActor
var normalizedPosition: CGFloat { get set }
```

#### Discussion

A negative value indicates that the cell is positioned to the left of the center cell in the collection view. A positive value indicates that the cell is positioned to the right of the center cell. A 0 value indicates the cell is in the neutral position, in the center of the collection view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvuikit/tvcollectionviewfullscreenlayoutattributes/normalizedposition)*
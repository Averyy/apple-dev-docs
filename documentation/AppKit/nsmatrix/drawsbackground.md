# drawsBackground

**Framework**: AppKit  
**Kind**: property

A Boolean that indicates whether the matrix draws its background.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var drawsBackground: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/swift/true), the matrix draws its background (the space between the cells).

## See Also

- [var backgroundColor: NSColor](nsmatrix/backgroundcolor.md)
  The background color of the matrix (the space between the cells).
- [var cellBackgroundColor: NSColor?](nsmatrix/cellbackgroundcolor.md)
  The background color of the matrix’s cells.
- [var drawsCellBackground: Bool](nsmatrix/drawscellbackground.md)
  A Boolean that indicates whether the matrix draws the background within each of its cells.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/drawsbackground)*
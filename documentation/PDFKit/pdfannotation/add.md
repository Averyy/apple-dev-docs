# add(_:)

**Framework**: PDFKit  
**Kind**: method

Adds a bezier path to the ink annotation.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func add(_ path: NSBezierPath)
```

## Parameters

- `path`: The bezier path to add, in annotation-space coordinates.

## See Also

- [var paths: [UIBezierPath]?](pdfannotation/paths.md)
  An array of bezier paths, in annotation-space coordinates, that compose the annotation.
- [func remove(UIBezierPath)](pdfannotation/remove(_:).md)
  Removes a bezier path from an ink annotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pdfkit/pdfannotation/add(_:))*
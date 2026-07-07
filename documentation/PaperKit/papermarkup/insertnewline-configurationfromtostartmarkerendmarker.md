# insertNewLine(configuration:from:to:startMarker:endMarker:)

**Framework**: PaperKit  
**Kind**: method

Add a line element on top of the paper.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
mutating func insertNewLine(configuration: ShapeConfiguration, from start: CGPoint, to end: CGPoint, startMarker lineStartMarker: Bool = false, endMarker lineEndMarker: Bool = false)
```

## Parameters

- `configuration`: The configuration of the line to insert.
- `start`: The start position of the line.
- `end`: The end position of the line.
- `lineStartMarker`: True if the start of the line has a marker / arrow.
- `lineEndMarker`: True if the end of the line has a marker / arrow.

## See Also

- [func insertNewShape(configuration: ShapeConfiguration, frame: CGRect, rotation: CGFloat)](papermarkup/insertnewshape(configuration:frame:rotation:).md)
  Add a new element on top of the paper.
- [func insertNewImage(CGImage, frame: CGRect, rotation: CGFloat)](papermarkup/insertnewimage(_:frame:rotation:).md)
  Add a new image on top of the paper.
- [func insertNewTextbox(attributedText: AttributedString, frame: CGRect, rotation: CGFloat)](papermarkup/insertnewtextbox(attributedtext:frame:rotation:)-53rs.md)
  Add a new text box on top of the paper.
- [func insertNewTextbox(attributedText: NSAttributedString, frame: CGRect, rotation: CGFloat)](papermarkup/insertnewtextbox(attributedtext:frame:rotation:)-67igk.md)
  Add a new text box on top of the paper.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/papermarkup/insertnewline(configuration:from:to:startmarker:endmarker:))*
# insertNewImage(_:frame:rotation:)

**Framework**: PaperKit  
**Kind**: method

Add a new image on top of the paper.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
mutating func insertNewImage(_ image: CGImage, frame: CGRect, rotation: CGFloat = 0)
```

## Parameters

- `image`: The image to add.
- `frame`: The frame to add the image at.
- `rotation`: The rotation in radians to add the element with.

## See Also

- [func insertNewShape(configuration: ShapeConfiguration, frame: CGRect, rotation: CGFloat)](papermarkup/insertnewshape(configuration:frame:rotation:).md)
  Add a new element on top of the paper.
- [func insertNewLine(configuration: ShapeConfiguration, from: CGPoint, to: CGPoint, startMarker: Bool, endMarker: Bool)](papermarkup/insertnewline(configuration:from:to:startmarker:endmarker:).md)
  Add a line element on top of the paper.
- [func insertNewTextbox(attributedText: AttributedString, frame: CGRect, rotation: CGFloat)](papermarkup/insertnewtextbox(attributedtext:frame:rotation:)-53rs.md)
  Add a new text box on top of the paper.
- [func insertNewTextbox(attributedText: NSAttributedString, frame: CGRect, rotation: CGFloat)](papermarkup/insertnewtextbox(attributedtext:frame:rotation:)-67igk.md)
  Add a new text box on top of the paper.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/papermarkup/insertnewimage(_:frame:rotation:))*
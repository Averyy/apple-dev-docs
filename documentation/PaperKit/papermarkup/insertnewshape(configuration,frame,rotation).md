# insertNewShape(configuration:frame:rotation:)

**Framework**: PaperKit  
**Kind**: method  
**Role**: Instance Method

Add a new element on top of the paper.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
mutating func insertNewShape(configuration: ShapeConfiguration, frame: CGRect, rotation: CGFloat = 0)
```

## Parameters

- `configuration`: The configuration of the shape to insert.
- `frame`: The frame to add the element at.
- `rotation`: The rotation in radians to add the element with.

## See Also

### Inserting elements
- [func insertNewImage(CGImage, frame: CGRect, rotation: CGFloat)](./insertnewimage%28_,frame,rotation%29.md)
  Add a new image on top of the paper.
- [func insertNewLine(configuration: ShapeConfiguration, from: CGPoint, to: CGPoint, startMarker: Bool, endMarker: Bool)](./insertnewline%28configuration,from,to,startmarker,endmarker%29.md)
  Add a line element on top of the paper.
- [func insertNewTextbox(attributedText: AttributedString, frame: CGRect, rotation: CGFloat)](./insertnewtextbox%28attributedtext,frame,rotation%29-53rs.md)
  Add a new text box on top of the paper.
- [func insertNewTextbox(attributedText: NSAttributedString, frame: CGRect, rotation: CGFloat)](./insertnewtextbox%28attributedtext,frame,rotation%29-67igk.md)
  Add a new text box on top of the paper.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/papermarkup/insertnewshape(configuration:frame:rotation:))*
# contentRect(forBounds:)

**Framework**: UIKit  
**Kind**: method

Returns the rectangle in which the receiver draws its entire content.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS 2.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func contentRect(forBounds bounds: CGRect) -> CGRect
```

#### Return Value

The rectangle in which the receiver draws its entire content.

#### Discussion

The content rectangle is the area needed to display the image and title including any padding and adjustments for alignment and other settings.

## Parameters

- `bounds`: The bounding rectangle for the receiver.

## See Also

- [var contentEdgeInsets: UIEdgeInsets](uibutton/contentedgeinsets.md)
  The inset or outset margins for the rectangle surrounding all of the button’s content.
- [func backgroundRect(forBounds: CGRect) -> CGRect](uibutton/backgroundrect(forbounds:).md)
  Returns the rectangle in which the receiver draws its background.
- [func titleRect(forContentRect: CGRect) -> CGRect](uibutton/titlerect(forcontentrect:).md)
  Returns the rectangle in which the receiver draws its title.
- [func imageRect(forContentRect: CGRect) -> CGRect](uibutton/imagerect(forcontentrect:).md)
  Returns the rectangle in which the receiver draws its image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/contentrect(forbounds:))*
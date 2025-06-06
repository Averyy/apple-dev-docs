# titleRect(forContentRect:)

**Framework**: UIKit  
**Kind**: method

Returns the rectangle in which the receiver draws its title.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS 2.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func titleRect(forContentRect contentRect: CGRect) -> CGRect
```

#### Return Value

The rectangle in which the receiver draws its title.

## Parameters

- `contentRect`: The content rectangle for the receiver.

## See Also

- [func backgroundRect(forBounds: CGRect) -> CGRect](uibutton/backgroundrect(forbounds:).md)
  Returns the rectangle in which the receiver draws its background.
- [func contentRect(forBounds: CGRect) -> CGRect](uibutton/contentrect(forbounds:).md)
  Returns the rectangle in which the receiver draws its entire content.
- [func imageRect(forContentRect: CGRect) -> CGRect](uibutton/imagerect(forcontentrect:).md)
  Returns the rectangle in which the receiver draws its image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/titlerect(forcontentrect:))*
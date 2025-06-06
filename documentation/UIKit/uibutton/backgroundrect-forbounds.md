# backgroundRect(forBounds:)

**Framework**: UIKit  
**Kind**: method

Returns the rectangle in which the receiver draws its background.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS 2.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func backgroundRect(forBounds bounds: CGRect) -> CGRect
```

#### Return Value

The bounds rectangle in which to draw any standard button content.

#### Discussion

The default implementation of this method returns the value in the `bounds` parameter. This rectangle represents the area in which the button draws its standard background content. Subclasses that provide custom background adornments can override this method and return a modified bounds rectangle to prevent the button from drawing over any custom content.

## Parameters

- `bounds`: The bounding rectangle of the receiver.

## See Also

- [func contentRect(forBounds: CGRect) -> CGRect](uibutton/contentrect(forbounds:).md)
  Returns the rectangle in which the receiver draws its entire content.
- [func titleRect(forContentRect: CGRect) -> CGRect](uibutton/titlerect(forcontentrect:).md)
  Returns the rectangle in which the receiver draws its title.
- [func imageRect(forContentRect: CGRect) -> CGRect](uibutton/imagerect(forcontentrect:).md)
  Returns the rectangle in which the receiver draws its image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/backgroundrect(forbounds:))*
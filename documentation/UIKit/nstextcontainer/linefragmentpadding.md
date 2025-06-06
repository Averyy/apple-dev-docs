# lineFragmentPadding

**Framework**: UIKit  
**Kind**: property

The value for the text inset within line fragment rectangles.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var lineFragmentPadding: CGFloat { get set }
```

#### Discussion

The padding appears at the beginning and end of the line fragment rectangles. The layout manager uses this value to determine the layout width. The default value of this property is `5.0`.

Line fragment padding is not designed to express text margins. Instead, you should use insets on your text view, adjust the paragraph margin attributes, or change the position of the text view within its superview.

## See Also

- [func lineFragmentRect(forProposedRect: CGRect, at: Int, writingDirection: NSWritingDirection, remaining: UnsafeMutablePointer<CGRect>?) -> CGRect](nstextcontainer/linefragmentrect(forproposedrect:at:writingdirection:remaining:).md)
  Returns the bounds of a line fragment rectangle inside the text container for the proposed rectangle.
- [var maximumNumberOfLines: Int](nstextcontainer/maximumnumberoflines.md)
  The maximum number of lines that the text container can store.
- [func lineFragmentRect(forProposedRect: CGRect, at: Int, writingDirection: NSWritingDirection, remaining: UnsafeMutablePointer<CGRect>?) -> CGRect](nstextcontainer/linefragmentrect(forproposedrect:at:writingdirection:remaining:).md)
  Returns the bounds of a line fragment rectangle inside the text container for the proposed rectangle.
- [var isSimpleRectangularTextContainer: Bool](nstextcontainer/issimplerectangulartextcontainer.md)
  A Boolean that indicates whether the text container’s region is a rectangle with no holes or gaps, and whose edges are parallel to the text view’s coordinate system axes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextcontainer/linefragmentpadding)*
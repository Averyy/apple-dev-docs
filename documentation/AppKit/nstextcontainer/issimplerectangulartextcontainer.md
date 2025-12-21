# isSimpleRectangularTextContainer

**Framework**: AppKit  
**Kind**: property

A Boolean that indicates whether the text container’s region is a rectangle with no holes or gaps, and whose edges are parallel to the text view’s coordinate system axes.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var isSimpleRectangularTextContainer: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) when the text container’s region is a rectangle with no holes or gaps and the edges are parallel to the text view’s coordinate system axes. The default value of this property is [`false`](https://developer.apple.com/documentation/Swift/false) when the [`exclusionPaths`](nstextcontainer/exclusionpaths.md) property contains one or more items, when the [`maximumNumberOfLines`](nstextcontainer/maximumnumberoflines.md) property is not zero, or when you override the [`lineFragmentRect(forProposedRect:at:writingDirection:remaining:)`](nstextcontainer/linefragmentrect(forproposedrect:at:writingdirection:remaining:).md) method. Otherwise, the default value is [`true`](https://developer.apple.com/documentation/Swift/true).

## See Also

- [var maximumNumberOfLines: Int](nstextcontainer/maximumnumberoflines.md)
  The maximum number of lines that the text container can store.
- [var lineFragmentPadding: CGFloat](nstextcontainer/linefragmentpadding.md)
  The value for the text inset within line fragment rectangles.
- [func lineFragmentRect(forProposedRect: CGRect, at: Int, writingDirection: NSWritingDirection, remaining: UnsafeMutablePointer<CGRect>?) -> CGRect](nstextcontainer/linefragmentrect(forproposedrect:at:writingdirection:remaining:).md)
  Returns the bounds of a line fragment rectangle inside the text container for the proposed rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextcontainer/issimplerectangulartextcontainer)*
# heightTracksTextView

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean that controls whether the text container adjusts the height of its bounding rectangle when its text view resizes.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var heightTracksTextView: Bool { get set }
```

```objc
@property BOOL heightTracksTextView;
```

#### Discussion

When the value of this property is [`true`](../../Swift/true.md), the text container adjusts its height when the height of its text view changes. The default value of this property is [`false`](../../Swift/false.md).

For more information, see [`NSTextContainer`](../nstextcontainer.md).

## See Also

### Defining the container shape
- [var size: CGSize](./size.md)
  The size of the text container’s bounding rectangle.
- [var exclusionPaths: [NSBezierPath]](./exclusionpaths.md)
  An array of path objects that represents the regions where text doesn’t display in the text container.
- [var lineBreakMode: NSLineBreakMode](./linebreakmode.md)
  The behavior of the last line inside the text container.
- [var widthTracksTextView: Bool](./widthtrackstextview.md)
  A Boolean that controls whether the text container adjusts the width of its bounding rectangle when its text view resizes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextcontainer/heighttrackstextview)*
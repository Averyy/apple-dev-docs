# widthTracksTextView

**Framework**: UIKit  
**Kind**: property

A Boolean that controls whether the text container adjusts the width of its bounding rectangle when its text view resizes.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var widthTracksTextView: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the text container adjusts its width when the width of its text view changes. The default value of this property is [`false`](https://developer.apple.com/documentation/Swift/false).

For more information about size tracking, see [`Text System Storage Layer Overview`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TextStorageLayer/TextStorageLayer.html#//apple_ref/doc/uid/10000087i).

## See Also

- [var containerSize: NSSize](../AppKit/NSTextContainer/containerSize.md)
  The size of the text container’s bounding rectangle.
- [var size: CGSize](nstextcontainer/size.md)
  The size of the text container’s bounding rectangle.
- [var exclusionPaths: [UIBezierPath]](nstextcontainer/exclusionpaths.md)
  An array of path objects that represents the regions where text doesn’t display in the text container.
- [var lineBreakMode: NSLineBreakMode](nstextcontainer/linebreakmode.md)
  The behavior of the last line inside the text container.
- [var heightTracksTextView: Bool](nstextcontainer/heighttrackstextview.md)
  A Boolean that controls whether the text container adjusts the height of its bounding rectangle when its text view resizes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextcontainer/widthtrackstextview)*
# widthTracksTextView

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic) BOOL widthTracksTextView;
```

#### Discussion

When the value of this property is [`true`](../../Swift/true.md), the text container adjusts its width when the width of its text view changes. The default value of this property is [`false`](../../Swift/false.md).

For more information about size tracking, see [Text System Storage Layer Overview](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/TextStorageLayer/TextStorageLayer.html#//apple_ref/doc/uid/10000087i).

## See Also

### Related Documentation
- [var containerSize: NSSize](../../AppKit/nstextcontainer/containersize.md)
  The size of the text container’s bounding rectangle.
### Defining the container shape
- [var size: CGSize](./size.md)
  The size of the text container’s bounding rectangle.
- [var exclusionPaths: [UIBezierPath]](./exclusionpaths.md)
  An array of path objects that represents the regions where text doesn’t display in the text container.
- [var lineBreakMode: NSLineBreakMode](./linebreakmode.md)
  The behavior of the last line inside the text container.
- [var heightTracksTextView: Bool](./heighttrackstextview.md)
  A Boolean that controls whether the text container adjusts the height of its bounding rectangle when its text view resizes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextcontainer/widthtrackstextview)*
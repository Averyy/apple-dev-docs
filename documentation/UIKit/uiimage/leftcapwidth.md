# leftCapWidth

**Framework**: UIKit  
**Kind**: property

The horizontal end-cap size.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var leftCapWidth: Int { get }
```

#### Discussion

End caps specify the portion of an image that should not be resized when an image is stretched. This technique is used to implement buttons and other resizable image-based interface elements. When a button with end caps is resized, the resizing occurs only in the middle of the button, in the region between the end caps. The end caps themselves keep their original size and appearance.

This property specifies the size of the left end cap. The middle (stretchable) portion is assumed to be 1 pixel wide. The right end cap is therefore computed by adding the size of the left end cap and the middle portion together and then subtracting that value from the width of the image:

```objc
rightCapWidth = image.size.width - (image.leftCapWidth + 1);
```

By default, this property is set to 0, which indicates that the image does not use end caps and the entire image is subject to stretching. To create a new image with a nonzero value for this property, use the [`stretchableImage(withLeftCapWidth:topCapHeight:)`](uiimage/stretchableimage(withleftcapwidth:topcapheight:).md) method.

## See Also

- [func stretchableImage(withLeftCapWidth: Int, topCapHeight: Int) -> UIImage](uiimage/stretchableimage(withleftcapwidth:topcapheight:).md)
  Creates and returns a new image object with the specified cap values.
- [var topCapHeight: Int](uiimage/topcapheight.md)
  The vertical end-cap size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/leftcapwidth)*
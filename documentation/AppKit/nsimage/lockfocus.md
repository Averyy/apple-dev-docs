# lockFocus()

**Framework**: AppKit  
**Kind**: method

Prepares the image to receive drawing commands.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func lockFocus()
```

#### Discussion

This method sets the current drawing context to the area of the offscreen window used to cache the receiver’s contents. Subsequent drawing commands are composited to this offscreen window. If the offscreen drawing area already has some content, any new drawing commands are composited with that content. This method does not modify the original image data directly.

When locking focus, this method chooses the best image representation object available and locks focus on that object. If the receiver has no image representations, this method creates one with the default depth and locks focus on it. For information on how the “best” representation is chosen, see the [`Images`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaDrawingGuide/Images/Images.html#//apple_ref/doc/uid/TP40003290-CH208) chapter of [`Cocoa Drawing Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaDrawingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40003290).

A successful [`lockFocus()`](nsimage/lockfocus().md) message must be balanced with a matching [`unlockFocus()`](nsimage/unlockfocus().md) message to the same `NSImage` object. These messages bracket the code that draws the image.

If [`lockFocus()`](nsimage/lockfocus().md) is unable to focus on the image, it raises an `NSImageCacheException`.

## See Also

- [var isValid: Bool](nsimage/isvalid.md)
  A Boolean value that indicates whether it is possible to draw an image representation.
- [var representations: [NSImageRep]](nsimage/representations.md)
  An array containing all of the image object’s image representations.
- [var prefersColorMatch: Bool](nsimage/preferscolormatch.md)
  A Boolean value that indicates whether the image prefers to choose image representations using color-matching or resolution-matching.
- [func lockFocusFlipped(Bool)](nsimage/lockfocusflipped(_:).md)
  Prepares the image to receive drawing commands using the specified flipped state.
- [func unlockFocus()](nsimage/unlockfocus.md)
  Removes the focus from the image.
- [convenience init(iconRef: IconRef)](nsimage/init(iconref:).md)
  Initializes the image object with a Carbon-style icon resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/lockfocus())*
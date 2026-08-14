# init(size:flipped:drawingHandler:)

**Framework**: AppKit  
**Kind**: init

Creates and returns an image object whose contents are drawn using the specified block.

**Availability**:
- macOS 10.8+

## Declaration

```swift
convenience init(size: NSSize, flipped drawingHandlerShouldBeCalledWithFlippedContext: Bool, drawingHandler: @escaping (NSRect) -> Bool)
```

#### Return Value

An initialized `NSImage` object.

#### Discussion

Use this method to generate an image that is correct at any resolution. This method creates an image object with a single [`NSCustomImageRep`](nscustomimagerep.md) object to manage drawing. The image representation uses the block in the `drawingHandler` parameter to do the actual drawing.

When you draw the image for the first time, the underlying image representation executes the `drawingHandler` block. The image object caches the results according to its usual caching policies; see the [`cacheMode`](nsimage/cachemode-swift.property.md) property. As long as the configuration of the destination graphics context does not change in a significant way, subsequent attempts to draw the image reuse the cached results whenever possible. If the pixel density or color space of the destination graphics context changes, though, the image representation throws away any caches and executes the block again to obtain a new version of the image. For example, if you drew the image on a standard resolution display but then draw it on a Retina display, AppKit executes the block again to obtain an image at the new resolution.

The most typical use for this method is to create an image based on vector-based content. In that case, your `drawingHandler` block would redraw its existing path objects when asked. If you draw a mixture of vectors and images, you need to do more work to ensure that your images are the appropriate resolution for the destination graphics context.

## Parameters

- `size`: The size of the image, measured in points.
- `drawingHandlerShouldBeCalledWithFlippedContext`: [`true`](https://developer.apple.com/documentation/swift/true) to apply a flip transformation to the graphics context before drawing or [`false`](https://developer.apple.com/documentation/swift/false) to draw using the default Cocoa coordinate system orientation.
- `drawingHandler`: A block that draws the contents of the image representation. The image representation copies the block and stores it for later use. It is not executed until you draw the image. Because the block is executed later, AppKit executes it on the same thread on which you draw the image itself, which can be any thread of your app. Therefore, the block must be safe to call from any thread. The block takes the following parameter: - **dstRect**: The destination rectangle in which to draw. The coordinates of this rectangle are specified in points. The block returns a Boolean that indicates whether it drew the image successfully. Return [`true`](https://developer.apple.com/documentation/swift/true) from your block if it successfully drew the contents or [`false`](https://developer.apple.com/documentation/swift/false) if it did not.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/init(size:flipped:drawinghandler:))*
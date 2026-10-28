# image(from:scale:)

**Framework**: PencilKit  
**Kind**: method  
**Role**: Instance Method

Returns an image object that contains the specified portion of the drawing.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, visionOS*

```swift
func image(from rect: CGRect, scale: CGFloat) -> UIImage
```

*macOS*

```swift
func image(from rect: CGRect, scale: CGFloat) -> NSImage
```

*iOS, iPadOS, Mac Catalyst, visionOS*

```objc
- (UIImage *) imageFromRect:(CGRect) rect scale:(CGFloat) scale;
```

*macOS*

```objc
- (NSImage *) imageFromRect:(CGRect) rect scale:(CGFloat) scale;
```

## Return Value

A new image object that contains the rendered content.

## Discussion

This method creates a new image and renders content from the canvas into that image at the specified scale factor.

## Parameters

- `rect`: The portion of the drawing that you want to capture. Specify a rectangle in the canvas’ coordinate system.
- `scale`: The scale factor at which to create the image. Specifying scale factors greater than `1.0` creates an image with more detail. For example, you might specify a scale factor of `2.0` or `3.0` when displaying the image on a Retina display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkdrawingreference/image(from:scale:))*
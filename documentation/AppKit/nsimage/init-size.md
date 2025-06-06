# init(size:)

**Framework**: AppKit  
**Kind**: init

Initializes and returns an image object with the specified dimensions.

**Availability**:
- macOS ?+

## Declaration

```swift
init(size: NSSize)
```

#### Return Value

An initialized `NSImage` object with no rendered content.

#### Discussion

This method does not add any image representations to the image object. It is permissible to initialize the image object by passing a size of `(0.0, 0.0)`; however, you must set the size to a non-zero value before using it or an exception will be raised.

After using this method to initialize an image object, you are expected to provide the image contents before trying to draw the image. You might lock focus on the image and draw to the image or you might explicitly add an image representation that you created.

## Parameters

- `size`: The size of the image, measured in points.

## See Also

- [var size: NSSize](nsimage/size.md)
  The size of the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/init(size:))*
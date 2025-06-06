# texture(with:options:)

**Framework**: Glkit  
**Kind**: method

Loads a 2D texture image from a Quartz image and creates a new texture from the data.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
class func texture(with cgImage: CGImage, options: [String : NSNumber]? = nil) throws -> GLKTextureInfo
```

#### Return Value

A texture info object that describes the loaded texture or `nil` if an error occurred.

#### Discussion

This class method loads the texture into the sharegroup attached to the current context for the thread this method is called on.

If the image was created using the CGBitmapImageContextCreate function, it must use one of the pixel formats described in the table below. CGImages loaded from files typically are already in one of these formats.

| Color Space | Pixel format and bitmap information constant |
| --- | --- |
| Null | 8 bpp, 8 bpc, [`CGImageAlphaInfo.alphaOnly`](https://developer.apple.com/documentation/CoreGraphics/CGImageAlphaInfo/alphaOnly) |
| Gray | 8 bpp, 8 bpc, [`CGImageAlphaInfo.none`](https://developer.apple.com/documentation/CoreGraphics/CGImageAlphaInfo/none) |
| Gray | 8 bpp, 8 bpc, [`CGImageAlphaInfo.alphaOnly`](https://developer.apple.com/documentation/CoreGraphics/CGImageAlphaInfo/alphaOnly) |
| RGB | 32 bpp, 8 bpc, [`CGImageAlphaInfo.noneSkipFirst`](https://developer.apple.com/documentation/CoreGraphics/CGImageAlphaInfo/noneSkipFirst) |
| RGB | 32 bpp, 8 bpc, [`CGImageAlphaInfo.premultipliedFirst`](https://developer.apple.com/documentation/CoreGraphics/CGImageAlphaInfo/premultipliedFirst) |

> **Note**:  In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `cgImage`: The Quartz image to be turned into a texture.
- `options`: A dictionary that describes any additional steps you want the texture loader to take when loading the texture. See  .

## See Also

- [func texture(with: CGImage, options: [String : NSNumber]?, queue: dispatch_queue_t?, completionHandler: GLKTextureLoaderCallback)](glktextureloader/texture(with:options:queue:completionhandler:).md)
  Asynchronously loads a 2D texture image from a Quartz image and creates a new texture from the data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glktextureloader/texture(with:options:))*
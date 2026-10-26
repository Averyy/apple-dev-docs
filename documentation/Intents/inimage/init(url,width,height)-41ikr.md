# init(url:width:height:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates an image object, of the specified size, from an image file in the local file system.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
convenience init?(url URL: URL, width: Double, height: Double)
```

```objc
+ (instancetype) imageWithURL:(NSURL *) URL width:(double) width height:(double) height;
```

#### Return Value

An image object that contains the local image file at the specified size, or `nil` if the system can’t load the image file or it doesn’t exist.

## Parameters

- `URL`: A URL to an image file on the local file system. The image can be in any format that the system supports.
- `width`: The required width, in points, of the image. If necessary, the system scales the image, horizontally, to match this value.
- `height`: The request height, in points, of the image. If necessary, the system scales the image, vertically, to match this value.

## See Also

### Creating an Image Object
- [convenience init(named: String)](./init%28named%29.md)
  Creates an image object from an image file in the extension’s bundle.
- [convenience init(UIImage: UIImage)](./init%28uiimage%29.md)
  Creates an image object from the specified UIKit image.
- [convenience init(CGImage: CGImage)](./init%28cgimage%29.md)
  Creates an image object from the specified Core Graphics image.
- [convenience init(imageData: Data)](./init%28imagedata%29.md)
  Creates an image object from the specified data.
- [convenience init?(url: URL)](./init%28url%29-8eo3q.md)
  Creates an image object from an image file in the local file system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inimage/init(url:width:height:)-41ikr)*
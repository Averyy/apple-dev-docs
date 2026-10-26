# init(UIImage:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates an image object from the specified UIKit image.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(UIImage image: UIImage)
```

```swift
convenience init(uiImage image: UIImage)
```

```objc
+ (instancetype) imageWithUIImage:(UIImage *) image;
```

#### Return Value

An image object that contains the specified UIKit image, or `nil` if that image is invalid.

## Parameters

- `image`: A UIKit image that contains the image data to use.

## See Also

### Creating an Image Object
- [convenience init(named: String)](./init%28named%29.md)
  Creates an image object from an image file in the extension’s bundle.
- [convenience init(CGImage: CGImage)](./init%28cgimage%29.md)
  Creates an image object from the specified Core Graphics image.
- [convenience init(imageData: Data)](./init%28imagedata%29.md)
  Creates an image object from the specified data.
- [convenience init?(url: URL)](./init%28url%29-8eo3q.md)
  Creates an image object from an image file in the local file system.
- [convenience init?(url: URL, width: Double, height: Double)](./init%28url,width,height%29-41ikr.md)
  Creates an image object, of the specified size, from an image file in the local file system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inimage/init(uiimage:))*
# init(url:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates an image object from an image file in the local file system.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
convenience init?(url URL: URL)
```

```objc
+ (instancetype) imageWithURL:(NSURL *) URL;
```

## Return Value

An image object that contains the local image file, or `nil` if the system can’t load the image file or it doesn’t exist.

## Parameters

- `URL`: A URL to an image file in the local file system. The image can be in any format that the system supports.

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
- [convenience init?(url: URL, width: Double, height: Double)](./init%28url,width,height%29-41ikr.md)
  Creates an image object, of the specified size, from an image file in the local file system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inimage/init(url:)-8eo3q)*
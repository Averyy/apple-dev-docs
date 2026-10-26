# init(imageData:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates an image object from the specified data.

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
convenience init(imageData: Data)
```

```objc
+ (instancetype) imageWithImageData:(NSData *) imageData;
```

#### Return Value

An image object that contains the specified image data, or `nil` if that image data is invalid.

## Parameters

- `imageData`: The data that contains the image, which you can create programmatically or load from an image file. The image can be in any format that the system supports.

## See Also

### Creating an Image Object
- [convenience init(named: String)](./init%28named%29.md)
  Creates an image object from an image file in the extension’s bundle.
- [convenience init(UIImage: UIImage)](./init%28uiimage%29.md)
  Creates an image object from the specified UIKit image.
- [convenience init(CGImage: CGImage)](./init%28cgimage%29.md)
  Creates an image object from the specified Core Graphics image.
- [convenience init?(url: URL)](./init%28url%29-8eo3q.md)
  Creates an image object from an image file in the local file system.
- [convenience init?(url: URL, width: Double, height: Double)](./init%28url,width,height%29-41ikr.md)
  Creates an image object, of the specified size, from an image file in the local file system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inimage/init(imagedata:))*
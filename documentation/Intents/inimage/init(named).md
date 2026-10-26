# init(named:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates an image object from an image file in the extension’s bundle.

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
convenience init(named name: String)
```

```objc
+ (instancetype) imageNamed:(NSString *) name;
```

#### Return Value

An image object that contains the bundled image file, or `nil` if the system can’t find an image with the specified filename.

## Parameters

- `name`: The filename of the image that the system loads from the extension’s bundle. You can omit the file’s extension for PNG images. For all other image file formats, you must include the extension.

## See Also

### Creating an Image Object
- [convenience init(UIImage: UIImage)](./init%28uiimage%29.md)
  Creates an image object from the specified UIKit image.
- [convenience init(CGImage: CGImage)](./init%28cgimage%29.md)
  Creates an image object from the specified Core Graphics image.
- [convenience init(imageData: Data)](./init%28imagedata%29.md)
  Creates an image object from the specified data.
- [convenience init?(url: URL)](./init%28url%29-8eo3q.md)
  Creates an image object from an image file in the local file system.
- [convenience init?(url: URL, width: Double, height: Double)](./init%28url,width,height%29-41ikr.md)
  Creates an image object, of the specified size, from an image file in the local file system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inimage/init(named:))*
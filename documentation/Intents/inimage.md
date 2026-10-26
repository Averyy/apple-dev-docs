# INImage

**Framework**: Intents  
**Kind**: class  
**Role**: Class

Image data inside an Intents extension or Intents UI extension.

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
class INImage
```

```objc
@interface INImage : NSObject
```

## Mentions

- [Displaying Shortcut Information in a Siri Watch Face Card](../SiriKit/displaying-shortcut-information-in-a-siri-watch-face-card.md)

#### Overview

[`INImage`](./inimage.md) is a wrapper for image data that you include in a response to an intent. When providing a response to an intent, you must specify any image parameters using instances of this class. [`INImage`](./inimage.md) supports the same formats as the underlying platform.

When confirming or handling an intent, you provide a response object with details about how your app handles that intent. When that response contains an image, use the [`imageSize(for:)`](./inimage/imagesize%28for%29.md) method to determine the required image size and then create an instance of this class with the corresponding image data.

## Topics

### Creating an Image Object
- [convenience init(named: String)](./inimage/init%28named%29.md)
  Creates an image object from an image file in the extension’s bundle.
- [convenience init(UIImage: UIImage)](./inimage/init%28uiimage%29.md)
  Creates an image object from the specified UIKit image.
- [convenience init(CGImage: CGImage)](./inimage/init%28cgimage%29.md)
  Creates an image object from the specified Core Graphics image.
- [convenience init(imageData: Data)](./inimage/init%28imagedata%29.md)
  Creates an image object from the specified data.
- [convenience init?(url: URL)](./inimage/init%28url%29-8eo3q.md)
  Creates an image object from an image file in the local file system.
- [convenience init?(url: URL, width: Double, height: Double)](./inimage/init%28url,width,height%29-41ikr.md)
  Creates an image object, of the specified size, from an image file in the local file system.
### Getting the Image
- [func fetchUIImage(completion: (UIImage?) -> Void)](./inimage/fetchuiimage%28completion%29.md)
  Fetches the image and provides it to the specified completion handler.
### Getting the Preferred Image Size
- [class func imageSize(for: INIntentResponse) -> CGSize](./inimage/imagesize%28for%29.md)
  Returns the preferred image size for the specified response object.
### Getting a System Symbol Image
- [class func systemImageNamed(String) -> Self](./inimage/systemimagenamed%28_%29.md)
  Returns an image object that contains the specified system symbol image.
### Initializers
- [convenience init(NSImage: NSImage)](./inimage/init%28nsimage%29.md)
- [convenience init?(URL: URL)](./inimage/init%28url%29-5po10.md)
- [convenience init?(URL: URL, width: Double, height: Double)](./inimage/init%28url,width,height%29-8snx6.md)
- [init?(coder: NSCoder)](./inimage/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inimage)*
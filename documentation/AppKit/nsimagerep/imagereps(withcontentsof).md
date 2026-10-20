# imageReps(withContentsOf:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Creates and returns an array of image representation objects initialized using the contents of the specified URL.

**Availability**:
- macOS

## Declaration

```swift
class func imageReps(withContentsOf url: URL) -> [NSImageRep]?
```

```objc
+ (NSArray<NSImageRep *> *) imageRepsWithContentsOfURL:(NSURL *) url;
```

#### Return Value

An array of image representation objects. The array contains one object for each image in the data at the specified URL.

#### Discussion

If sent to the `NSImageRep` class object, this method returns an array of objects (all newly allocated instances of a subclass of `NSImageRep`) that have been initialized with the contents of the specified URL. If sent to a subclass of `NSImageRep` that recognizes the data at the specified URL, it returns an array of objects (all instances of that subclass) that have been initialized with the contents of that URL.

This method returns `nil` in any of the following cases:

- The message is sent to the `NSImageRep` class object and there are no subclasses in the `NSImageRep` class registry that handle data in the specified URL.
- The message is sent to a subclass of `NSImageRep` and that subclass cannot handle data in the specified URL.
- The `NSImageRep` subclass is unable to initialize itself with the contents of the specified URL.

The `NSImageRep` subclass is initialized by creating an `NSData` object based on the contents of the specified URL and passing it to the `imageRepsWithData:` method.

## Parameters

- `url`: The URL pointing to the image data.

## See Also

### Creating Representations of Images
- [class func imageReps(withContentsOfFile: String) -> [NSImageRep]?](./imagereps%28withcontentsoffile%29.md)
  Creates and returns an array of image representation objects initialized using the contents of the specified file.
- [class func imageReps(with: NSPasteboard) -> [NSImageRep]?](./imagereps%28with%29.md)
  Creates and returns an array of image representation objects initialized using the contents of the pasteboard.
- [init?(contentsOfFile: String)](./init%28contentsoffile%29.md)
  Creates and returns an image representation object using the contents of the specified file.
- [init?(pasteboard: NSPasteboard)](./init%28pasteboard%29.md)
  Creates and returns an image representation object using the contents of the specified pasteboard.
- [init?(contentsOf: URL)](./init%28contentsof%29.md)
  Creates and returns an image representation object using the data at the specified URL.
- [init()](./init%28%29.md)
  Creates and returns an image representation object.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates and returns an image representation object from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimagerep/imagereps(withcontentsof:))*
# imageReps(with:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Creates and returns an array of image representation objects initialized using the contents of the pasteboard.

**Availability**:
- macOS

## Declaration

```swift
class func imageReps(with pasteboard: NSPasteboard) -> [NSImageRep]?
```

```objc
+ (NSArray<NSImageRep *> *) imageRepsWithPasteboard:(NSPasteboard *) pasteboard;
```

#### Return Value

An array of image representation objects. The array contains one object for each image in the specified pasteboard.

#### Discussion

If sent to the `NSImageRep` class object, this method returns an array of objects (all newly-allocated instances of a subclass of `NSImageRep`) that have been initialized with the data in the specified pasteboard. If sent to a subclass of `NSImageRep` that recognizes the pasteboard data, it returns an array of objects (all instances of that subclass) initialized with the pasteboard data.

This method returns `nil` in any of the following cases:

- The message is sent to the `NSImageRep` class object and there are no subclasses in the `NSImageRep` class registry that handle the pasteboard data.
- The message is sent to a subclass of `NSImageRep` and that subclass cannot handle the pasteboard data.
- The `NSImageRep` subclass is unable to initialize itself with the contents the pasteboard.

The `NSImageRep` subclass is initialized by creating an `NSData` object based on the data in `pasteboard` and passing it to the `imageRepsWithData:` method.

## Parameters

- `pasteboard`: The pasteboard containing the image data.

## See Also

### Related Documentation
- [class func imagePasteboardTypes() -> [NSPasteboard.PasteboardType]](./imagepasteboardtypes%28%29.md)
  Returns the pasteboard types supported by the image representation class or one of its subclasses.
### Creating Representations of Images
- [class func imageReps(withContentsOfFile: String) -> [NSImageRep]?](./imagereps%28withcontentsoffile%29.md)
  Creates and returns an array of image representation objects initialized using the contents of the specified file.
- [class func imageReps(withContentsOf: URL) -> [NSImageRep]?](./imagereps%28withcontentsof%29.md)
  Creates and returns an array of image representation objects initialized using the contents of the specified URL.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimagerep/imagereps(with:))*
# init(pasteboard:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates and returns an image representation object using the contents of the specified pasteboard.

**Availability**:
- macOS

## Declaration

```swift
init?(pasteboard: NSPasteboard)
```

```objc
+ (NSImageRep *) imageRepWithPasteboard:(NSPasteboard *) pasteboard;
```

#### Return Value

An initialized instance of an `NSImageRep` subclass, or `nil` if the image data could not be read.

#### Discussion

If sent to the `NSImageRep` class object, this method returns a newly allocated instance of a subclass of `NSImageRep` initialized with the data in the specified pasteboard. If sent to a subclass of `NSImageRep` that recognizes the data on the pasteboard, it returns an instance of that subclass initialized with that data.

This method returns `nil` in any of the following cases:

- The message is sent to the `NSImageRep` class object and there are no subclasses in the `NSImageRep` class registry that handle data of the type contained in the specified pasteboard.
- The message is sent to a subclass of `NSImageRep` and that subclass cannot handle data of the type contained in the specified pasteboard.
- The `NSImageRep` subclass is unable to initialize itself with the contents of the pasteboard.

The `NSImageRep` subclass is initialized by creating an `NSData` object based on the data the specified pasteboard and passing it to the `imageRepWithData:` method.

## Parameters

- `pasteboard`: The pasteboard containing the image data.

## See Also

### Related Documentation
- [class func imagePasteboardTypes() -> [NSPasteboard.PasteboardType]](./imagepasteboardtypes%28%29.md)
  Returns the pasteboard types supported by the image representation class or one of its subclasses.
### Creating Representations of Images
- [class func imageReps(withContentsOfFile: String) -> [NSImageRep]?](./imagereps%28withcontentsoffile%29.md)
  Creates and returns an array of image representation objects initialized using the contents of the specified file.
- [class func imageReps(with: NSPasteboard) -> [NSImageRep]?](./imagereps%28with%29.md)
  Creates and returns an array of image representation objects initialized using the contents of the pasteboard.
- [class func imageReps(withContentsOf: URL) -> [NSImageRep]?](./imagereps%28withcontentsof%29.md)
  Creates and returns an array of image representation objects initialized using the contents of the specified URL.
- [init?(contentsOfFile: String)](./init%28contentsoffile%29.md)
  Creates and returns an image representation object using the contents of the specified file.
- [init?(contentsOf: URL)](./init%28contentsof%29.md)
  Creates and returns an image representation object using the data at the specified URL.
- [init()](./init%28%29.md)
  Creates and returns an image representation object.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates and returns an image representation object from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimagerep/init(pasteboard:))*
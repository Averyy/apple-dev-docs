# init(pasteboard:)

**Framework**: AppKit  
**Kind**: init

Creates and returns an image representation object using the contents of the specified pasteboard.

**Availability**:
- macOS ?+

## Declaration

```swift
init?(pasteboard: NSPasteboard)
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

- [class func imagePasteboardTypes() -> [NSPasteboard.PasteboardType]](nsimagerep/imagepasteboardtypes.md)
  Returns the pasteboard types supported by the image representation class or one of its subclasses.
- [class func imageReps(withContentsOfFile: String) -> [NSImageRep]?](nsimagerep/imagereps(withcontentsoffile:).md)
  Creates and returns an array of image representation objects initialized using the contents of the specified file.
- [class func imageReps(with: NSPasteboard) -> [NSImageRep]?](nsimagerep/imagereps(with:).md)
  Creates and returns an array of image representation objects initialized using the contents of the pasteboard.
- [class func imageReps(withContentsOf: URL) -> [NSImageRep]?](nsimagerep/imagereps(withcontentsof:).md)
  Creates and returns an array of image representation objects initialized using the contents of the specified URL.
- [init?(contentsOfFile: String)](nsimagerep/init(contentsoffile:).md)
  Creates and returns an image representation object using the contents of the specified file.
- [init?(contentsOf: URL)](nsimagerep/init(contentsof:).md)
  Creates and returns an image representation object using the data at the specified URL.
- [init()](nsimagerep/init.md)
  Creates and returns an image representation object.
- [init?(coder: NSCoder)](nsimagerep/init(coder:).md)
  Creates and returns an image representation object from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimagerep/init(pasteboard:))*
# init(contentsOf:)

**Framework**: AppKit  
**Kind**: init

Creates and returns an image representation object using the data at the specified URL.

**Availability**:
- macOS ?+

## Declaration

```swift
init?(contentsOf url: URL)
```

#### Return Value

An initialized instance of an `NSImageRep` subclass, or `nil` if the image data could not be read.

#### Discussion

If sent to the `NSImageRep` class object, this method returns a newly allocated instance of a subclass of `NSImageRep` initialized with the contents of the specified URL. If sent to a subclass of `NSImageRep` that recognizes the data contained in the URL, it returns an instance of that subclass initialized with the data in the URL.

This method returns `nil` in any of the following cases:

- The message is sent to the `NSImageRep` class object and there are no subclasses in the `NSImageRep` class registry that handle the data contained in the specified URL.
- The message is sent to a subclass of `NSImageRep` and that subclass cannot handle the data contained in the specified URL.
- The `NSImageRep` subclass is unable to initialize itself with the contents of the specified URL.

The `NSImageRep` subclass is initialized by creating an `NSData` object based on the contents of the file, then passing it to the `imageRepWithData:` method.

## Parameters

- `url`: The URL pointing to the image data.

## See Also

- [class func imageReps(withContentsOfFile: String) -> [NSImageRep]?](nsimagerep/imagereps(withcontentsoffile:).md)
  Creates and returns an array of image representation objects initialized using the contents of the specified file.
- [class func imageReps(with: NSPasteboard) -> [NSImageRep]?](nsimagerep/imagereps(with:).md)
  Creates and returns an array of image representation objects initialized using the contents of the pasteboard.
- [class func imageReps(withContentsOf: URL) -> [NSImageRep]?](nsimagerep/imagereps(withcontentsof:).md)
  Creates and returns an array of image representation objects initialized using the contents of the specified URL.
- [init?(contentsOfFile: String)](nsimagerep/init(contentsoffile:).md)
  Creates and returns an image representation object using the contents of the specified file.
- [init?(pasteboard: NSPasteboard)](nsimagerep/init(pasteboard:).md)
  Creates and returns an image representation object using the contents of the specified pasteboard.
- [init()](nsimagerep/init.md)
  Creates and returns an image representation object.
- [init?(coder: NSCoder)](nsimagerep/init(coder:).md)
  Creates and returns an image representation object from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimagerep/init(contentsof:))*
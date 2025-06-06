# imageReps(withContentsOfFile:)

**Framework**: AppKit  
**Kind**: method

Creates and returns an array of image representation objects initialized using the contents of the specified file.

**Availability**:
- macOS ?+

## Declaration

```swift
class func imageReps(withContentsOfFile filename: String) -> [NSImageRep]?
```

#### Return Value

An array of image representation objects. The array contains one object for each image in the specified file.

#### Discussion

If sent to the `NSImageRep` class object, this method returns an array of objects (all newly allocated instances of a subclass of `NSImageRep`, chosen through the use of [`class(forFileType:)`](nsimagerep/class(forfiletype:).md)) that have been initialized with the contents of the file. If sent to a subclass of `NSImageRep` that recognizes the file type, this method returns an array of objects (all instances of that subclass) that have been initialized with the contents of the file.

This method returns `nil` in any of the following cases:

- The message is sent to the `NSImageRep` class object and there are no subclasses in the `NSImageRep` class registry that handle the data in the file.
- The message is sent to a subclass of `NSImageRep` and that subclass cannot handle the data in the file.
- The `NSImageRep` subclass is unable to initialize itself with the contents of `filename`.

The `NSImageRep` subclass is initialized by creating an `NSData` object based on the contents of the file and passing it to the `imageRepsWithData:` method of the subclass. By default, the files handled include those with the extensions “`tiff`”, “`gif`”, “`jpg`”, “`pict`”, “`pdf`”, and “`eps`”.

## Parameters

- `filename`: A full or relative pathname specifying the file to open. This string should include the filename extension.

## See Also

- [class func imageFileTypes() -> [String]](nsimagerep/imagefiletypes.md)
  Returns the file types supported by the image representation class or one of its subclasses.
- [Cocoa Drawing Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaDrawingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40003290)
- [class func imageReps(with: NSPasteboard) -> [NSImageRep]?](nsimagerep/imagereps(with:).md)
  Creates and returns an array of image representation objects initialized using the contents of the pasteboard.
- [class func imageReps(withContentsOf: URL) -> [NSImageRep]?](nsimagerep/imagereps(withcontentsof:).md)
  Creates and returns an array of image representation objects initialized using the contents of the specified URL.
- [init?(contentsOfFile: String)](nsimagerep/init(contentsoffile:).md)
  Creates and returns an image representation object using the contents of the specified file.
- [init?(pasteboard: NSPasteboard)](nsimagerep/init(pasteboard:).md)
  Creates and returns an image representation object using the contents of the specified pasteboard.
- [init?(contentsOf: URL)](nsimagerep/init(contentsof:).md)
  Creates and returns an image representation object using the data at the specified URL.
- [init()](nsimagerep/init.md)
  Creates and returns an image representation object.
- [init?(coder: NSCoder)](nsimagerep/init(coder:).md)
  Creates and returns an image representation object from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimagerep/imagereps(withcontentsoffile:))*
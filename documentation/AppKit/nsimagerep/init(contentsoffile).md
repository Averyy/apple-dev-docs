# init(contentsOfFile:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates and returns an image representation object using the contents of the specified file.

**Availability**:
- macOS

## Declaration

```swift
init?(contentsOfFile filename: String)
```

```objc
+ (NSImageRep *) imageRepWithContentsOfFile:(NSString *) filename;
```

## Return Value

An initialized instance of an `NSImageRep` subclass, or `nil` if the image data could not be read.

## Discussion

If sent to the `NSImageRep` class object, this method returns a newly allocated instance of a subclass of `NSImageRep` (chosen through the use of [`class(forFileType:)`](./class%28forfiletype%29.md)) initialized with the contents of the specified file. If sent to a subclass of `NSImageRep` that recognizes the type of data in the file, it returns an instance of that subclass initialized with the contents of the file.

This method returns `nil` in any of the following cases:

- The message is sent to the `NSImageRep` class object and there are no subclasses in the `NSImageRep` class registry that handle the type of data in the specified file.
- The message is sent to a subclass of `NSImageRep` and that subclass cannot handle the type of data in the specified file.
- The `NSImageRep` subclass is unable to initialize itself with the contents of the specified file.

The `NSImageRep` subclass is initialized by creating an `NSData` object based on the contents of the file and passing it to the `imageRepWithData:` method. By default, the files handled include those with the extensions “`tiff`”, “`gif`”, “`jpg`”, “`pict`”, “`pdf`”, and “`eps`”.

## Parameters

- `filename`: A full or relative pathname specifying the file to open. This string should include the filename extension.

## See Also

### Related Documentation
- [class func imageFileTypes() -> [String]](./imagefiletypes%28%29.md)
  Returns the file types supported by the image representation class or one of its subclasses.
### Creating Representations of Images
- [class func imageReps(withContentsOfFile: String) -> [NSImageRep]?](./imagereps%28withcontentsoffile%29.md)
  Creates and returns an array of image representation objects initialized using the contents of the specified file.
- [class func imageReps(with: NSPasteboard) -> [NSImageRep]?](./imagereps%28with%29.md)
  Creates and returns an array of image representation objects initialized using the contents of the pasteboard.
- [class func imageReps(withContentsOf: URL) -> [NSImageRep]?](./imagereps%28withcontentsof%29.md)
  Creates and returns an array of image representation objects initialized using the contents of the specified URL.
- [init?(pasteboard: NSPasteboard)](./init%28pasteboard%29.md)
  Creates and returns an image representation object using the contents of the specified pasteboard.
- [init?(contentsOf: URL)](./init%28contentsof%29.md)
  Creates and returns an image representation object using the data at the specified URL.
- [init()](./init%28%29.md)
  Creates and returns an image representation object.
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates and returns an image representation object from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimagerep/init(contentsoffile:))*
# imageUnfilteredFileTypes()

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Returns an array of strings identifying the file types supported directly by the registered image representation objects.

**Availability**:
- macOS 10.0+ - Deprecated in 10.10

> **Deprecated**: Use [`imageUnfilteredTypes`](./imageunfilteredtypes.md) instead.

## Declaration

```swift
class func imageUnfilteredFileTypes() -> [String]
```

```objc
+ (NSArray<NSString *> *) imageUnfilteredFileTypes;
```

#### Return Value

An array of `NSString` objects, each of which identifies a single supported file type. File types are identified by file extension and HFS file types.

#### Discussion

The returned list does not contain pasteboard types that are available only through a user-installed filter service.

## See Also

### Deprecated class methods
- [class func imageFileTypes() -> [String]](./imagefiletypes%28%29.md)
  Returns an array of strings identifying the image types supported by the registered image representation objects.
- [class func imagePasteboardTypes() -> [NSPasteboard.PasteboardType]](./imagepasteboardtypes%28%29.md)
  Returns an array of strings identifying the pasteboard types supported directly by the registered image representation objects.
- [class func imageUnfilteredPasteboardTypes() -> [NSPasteboard.PasteboardType]](./imageunfilteredpasteboardtypes%28%29.md)
  Returns an array of strings identifying the pasteboard types supported directly by the registered image representation objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/imageunfilteredfiletypes())*
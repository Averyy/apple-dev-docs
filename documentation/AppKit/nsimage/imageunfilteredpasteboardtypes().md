# imageUnfilteredPasteboardTypes()

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Returns an array of strings identifying the pasteboard types supported directly by the registered image representation objects.

**Availability**:
- macOS 10.0+ - Deprecated in 10.10

> **Deprecated**: Use +imageUnfilteredTypes instead

## Declaration

```swift
class func imageUnfilteredPasteboardTypes() -> [NSPasteboard.PasteboardType]
```

```objc
+ (NSArray<NSString *> *) imageUnfilteredPasteboardTypes;
```

#### Return Value

An array of `NSString` objects, each of which identifies a single supported pasteboard type.

#### Discussion

The returned list does not contain pasteboard types that are supported only through a user-installed filter service.

## See Also

### Deprecated class methods
- [class func imageFileTypes() -> [String]](./imagefiletypes%28%29.md)
  Returns an array of strings identifying the image types supported by the registered image representation objects.
- [class func imageUnfilteredFileTypes() -> [String]](./imageunfilteredfiletypes%28%29.md)
  Returns an array of strings identifying the file types supported directly by the registered image representation objects.
- [class func imagePasteboardTypes() -> [NSPasteboard.PasteboardType]](./imagepasteboardtypes%28%29.md)
  Returns an array of strings identifying the pasteboard types supported directly by the registered image representation objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/imageunfilteredpasteboardtypes())*
# imagePasteboardTypes()

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Returns the pasteboard types supported by the image representation class or one of its subclasses.

**Availability**:
- macOS 10.0+ - Deprecated in 10.10

> **Deprecated**: Use [`imageTypes`](./imagetypes.md) instead.

## Declaration

```swift
class func imagePasteboardTypes() -> [NSPasteboard.PasteboardType]
```

```objc
+ (NSArray<NSString *> *) imagePasteboardTypes;
```

#### Return Value

An array of `NSString` objects, each of which contains a supported pasteboard format.

#### Discussion

The list includes both those types returned by the [`imageUnfilteredPasteboardTypes()`](./imageunfilteredpasteboardtypes%28%29.md) class method plus those that can be converted to a supported type by a user-installed filter service. Don’t override this method when subclassing `NSImageRep`—it always returns a valid list for any subclass of `NSImageRep` that correctly overrides the [`imageUnfilteredPasteboardTypes()`](./imageunfilteredpasteboardtypes%28%29.md) method.

## See Also

### Deprecated methods
- [class func imageFileTypes() -> [String]](./imagefiletypes%28%29.md)
  Returns the file types supported by the image representation class or one of its subclasses.
- [class func imageUnfilteredFileTypes() -> [String]](./imageunfilteredfiletypes%28%29.md)
  Returns the list of file types supported directly by the image representation.
- [class func imageUnfilteredPasteboardTypes() -> [NSPasteboard.PasteboardType]](./imageunfilteredpasteboardtypes%28%29.md)
  Returns the list of pasteboard types supported directly by the image representation.
- [class func `class`(forFileType: String) -> AnyClass?](./class%28forfiletype%29.md)
  Returns the image representation subclass that handles data with the specified type.
- [class func `class`(forPasteboardType: NSPasteboard.PasteboardType) -> AnyClass?](./class%28forpasteboardtype%29.md)
  Returns the image representation subclass that handles data with the specified pasteboard type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimagerep/imagepasteboardtypes())*
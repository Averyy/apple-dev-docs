# imageUnfilteredFileTypes()

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Returns the list of file types supported directly by the image representation.

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

An array of `NSString` objects. This array is empty by default. Subclasses must override to return the list of file formats they support.

#### Discussion

The returned file types can include encoded HFS file types as well as filename extensions. When creating a subclass of `NSImageRep`, override this method to return a list of strings representing the supported file types. For example, the `NSBitmapImageRep` class implements code similar to the following for this method:

```objc
+ (NSArray *)imageUnfilteredFileTypes {
    static NSArray *types = nil;
 
    if (!types) types = [[NSArray alloc]
        initWithObjects:@"tiff", @"gif", @"jpg",  @"bmp", nil];
    return types;
}
```

If your subclass supports the types supported by its superclass, you must explicitly get the array of types from the superclass and put them in the array returned by this method.

## See Also

### Related Documentation
- [class func imageUnfilteredFileTypes() -> [String]](../nsimage/imageunfilteredfiletypes%28%29.md)
  Returns an array of strings identifying the file types supported directly by the registered image representation objects.
### Deprecated methods
- [class func imageFileTypes() -> [String]](./imagefiletypes%28%29.md)
  Returns the file types supported by the image representation class or one of its subclasses.
- [class func imagePasteboardTypes() -> [NSPasteboard.PasteboardType]](./imagepasteboardtypes%28%29.md)
  Returns the pasteboard types supported by the image representation class or one of its subclasses.
- [class func imageUnfilteredPasteboardTypes() -> [NSPasteboard.PasteboardType]](./imageunfilteredpasteboardtypes%28%29.md)
  Returns the list of pasteboard types supported directly by the image representation.
- [class func `class`(forFileType: String) -> AnyClass?](./class%28forfiletype%29.md)
  Returns the image representation subclass that handles data with the specified type.
- [class func `class`(forPasteboardType: NSPasteboard.PasteboardType) -> AnyClass?](./class%28forpasteboardtype%29.md)
  Returns the image representation subclass that handles data with the specified pasteboard type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimagerep/imageunfilteredfiletypes())*
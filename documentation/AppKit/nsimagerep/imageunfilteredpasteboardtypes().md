# imageUnfilteredPasteboardTypes()

**Framework**: AppKit  
**Kind**: method

Returns the list of pasteboard types supported directly by the image representation.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class func imageUnfilteredPasteboardTypes() -> [NSPasteboard.PasteboardType]
```

#### Return Value

An array of `NSString` objects. This array is empty by default. Subclasses must override to return the list of pasteboard formats they support.

#### Discussion

When creating a subclass of `NSImageRep`, override this method to return a list representing the supported pasteboard types. For example, the `NSBitmapImageRep` class implements code similar to the following for this method:

```objc
+ (NSArray *)imageUnfilteredPasteboardTypes {
    static NSArray *types = nil;
 
    if (!types) types = [[NSArray alloc] initWithObjects:NSTIFFPboardType,  nil];
    return types;
}
```

If your subclass supports the types supported by its superclass, you must explicitly get the list of types from the superclass and add them to the array returned by this method.

## See Also

- [class func imageUnfilteredPasteboardTypes() -> [NSPasteboard.PasteboardType]](nsimage/imageunfilteredpasteboardtypes.md)
  Returns an array of strings identifying the pasteboard types supported directly by the registered image representation objects.
- [class func imageFileTypes() -> [String]](nsimagerep/imagefiletypes.md)
  Returns the file types supported by the image representation class or one of its subclasses.
- [class func imagePasteboardTypes() -> [NSPasteboard.PasteboardType]](nsimagerep/imagepasteboardtypes.md)
  Returns the pasteboard types supported by the image representation class or one of its subclasses.
- [class func imageUnfilteredFileTypes() -> [String]](nsimagerep/imageunfilteredfiletypes.md)
  Returns the list of file types supported directly by the image representation.
- [class func `class`(forFileType: String) -> AnyClass?](nsimagerep/class(forfiletype:).md)
  Returns the image representation subclass that handles data with the specified type.
- [class func `class`(forPasteboardType: NSPasteboard.PasteboardType) -> AnyClass?](nsimagerep/class(forpasteboardtype:).md)
  Returns the image representation subclass that handles data with the specified pasteboard type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimagerep/imageunfilteredpasteboardtypes())*
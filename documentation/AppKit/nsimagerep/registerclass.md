# registerClass(_:)

**Framework**: AppKit  
**Kind**: method

Adds the specified class to the registry of available image representation subclasses.

**Availability**:
- macOS ?+

## Declaration

```swift
class func registerClass(_ imageRepClass: AnyClass)
```

#### Discussion

This method posts an [`registryDidChangeNotification`](nsimagerep/registrydidchangenotification.md), along with the receiving object, to the default notification center.

A good place to add image representation classes to the registry is in the `load` class method.

## Parameters

- `imageRepClass`: The   object for an   subclass.

## See Also

- [class func load()](../ObjectiveC/NSObject-swift.class/load.md)
  Invoked whenever a class or category is added to the Objective-C runtime; implement this method to perform class-specific behavior upon loading.
- [class func `class`(forType: String) -> AnyClass?](nsimagerep/class(fortype:).md)
  Returns the image representation subclass that handles image data for the specified UTI.
- [class func `class`(for: Data) -> AnyClass?](nsimagerep/class(for:).md)
  Returns the image representation subclass that handles the specified type of data.
- [class var registeredClasses: [AnyClass]](nsimagerep/registeredclasses.md)
  Returns an array containing the registered image representation classes.
- [class func unregisterClass(AnyClass)](nsimagerep/unregisterclass(_:).md)
  Removes the specified image representation subclass from the registry of available image representations.
- [class func `class`(forFileType: String) -> AnyClass?](nsimagerep/class(forfiletype:).md)
  Returns the image representation subclass that handles data with the specified type.
- [class func `class`(forPasteboardType: NSPasteboard.PasteboardType) -> AnyClass?](nsimagerep/class(forpasteboardtype:).md)
  Returns the image representation subclass that handles data with the specified pasteboard type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimagerep/registerclass(_:))*
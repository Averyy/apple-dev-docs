# registeredClasses

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Returns an array containing the registered image representation classes.

**Availability**:
- macOS

## Declaration

```swift
class var registeredClasses: [AnyClass] { get }
```

```objc
@property (class, copy, readonly) NSArray<Class> * registeredImageRepClasses;
```

## Return Value

An array of `Class` objects identifying the registered `NSImageRep` subclasses.

## See Also

### Managing Representation Subclasses of Images
- [class func `class`(forType: String) -> AnyClass?](./class%28fortype%29.md)
  Returns the image representation subclass that handles image data for the specified UTI.
- [class func `class`(for: Data) -> AnyClass?](./class%28for%29.md)
  Returns the image representation subclass that handles the specified type of data.
- [class func registerClass(AnyClass)](./registerclass%28_%29.md)
  Adds the specified class to the registry of available image representation subclasses.
- [class func unregisterClass(AnyClass)](./unregisterclass%28_%29.md)
  Removes the specified image representation subclass from the registry of available image representations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimagerep/registeredclasses)*
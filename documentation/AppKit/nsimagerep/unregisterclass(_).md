# unregisterClass(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Removes the specified image representation subclass from the registry of available image representations.

**Availability**:
- macOS

## Declaration

```swift
class func unregisterClass(_ imageRepClass: AnyClass)
```

```objc
+ (void) unregisterImageRepClass:(Class) imageRepClass;
```

## Discussion

This method posts the [`registryDidChangeNotification`](./registrydidchangenotification.md), along with the receiving object, to the default notification center.

## Parameters

- `imageRepClass`: The `Class` object for an `NSImageRep` subclass.

## See Also

### Managing Representation Subclasses of Images
- [class func `class`(forType: String) -> AnyClass?](./class%28fortype%29.md)
  Returns the image representation subclass that handles image data for the specified UTI.
- [class func `class`(for: Data) -> AnyClass?](./class%28for%29.md)
  Returns the image representation subclass that handles the specified type of data.
- [class var registeredClasses: [AnyClass]](./registeredclasses.md)
  Returns an array containing the registered image representation classes.
- [class func registerClass(AnyClass)](./registerclass%28_%29.md)
  Adds the specified class to the registry of available image representation subclasses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimagerep/unregisterclass(_:))*
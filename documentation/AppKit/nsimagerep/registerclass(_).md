# registerClass(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Adds the specified class to the registry of available image representation subclasses.

**Availability**:
- macOS

## Declaration

```swift
class func registerClass(_ imageRepClass: AnyClass)
```

```objc
+ (void) registerImageRepClass:(Class) imageRepClass;
```

## Discussion

This method posts an [`registryDidChangeNotification`](./registrydidchangenotification.md), along with the receiving object, to the default notification center.

A good place to add image representation classes to the registry is in the `load` class method.

## Parameters

- `imageRepClass`: The `Class` object for an `NSImageRep` subclass.

## See Also

### Related Documentation
- [class func load()](../../ObjectiveC/nsobject-swift.class/load%28%29.md)
  Invoked whenever a class or category is added to the Objective-C runtime; implement this method to perform class-specific behavior upon loading.
### Managing Representation Subclasses of Images
- [class func `class`(forType: String) -> AnyClass?](./class%28fortype%29.md)
  Returns the image representation subclass that handles image data for the specified UTI.
- [class func `class`(for: Data) -> AnyClass?](./class%28for%29.md)
  Returns the image representation subclass that handles the specified type of data.
- [class var registeredClasses: [AnyClass]](./registeredclasses.md)
  Returns an array containing the registered image representation classes.
- [class func unregisterClass(AnyClass)](./unregisterclass%28_%29.md)
  Removes the specified image representation subclass from the registry of available image representations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimagerep/registerclass(_:))*
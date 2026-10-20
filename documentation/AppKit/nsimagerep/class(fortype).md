# class(forType:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Returns the image representation subclass that handles image data for the specified UTI.

**Availability**:
- macOS 10.5+

## Declaration

```swift
class func `class`(forType type: String) -> AnyClass?
```

```objc
+ (Class) imageRepClassForType:(NSString *) type;
```

#### Return Value

A `Class` object for the image representation that can handle the UTI, or `nil` if no image representation could handle the data.

## Parameters

- `type`: The UTI string identifying the desired image type. Some sample image-related UTI strings include “`public.image`”, “`public.jpeg`”, and “`public.tiff`”. For a list of supported types, see `UTCoreTypes.h`.

## See Also

### Managing Representation Subclasses of Images
- [class func `class`(for: Data) -> AnyClass?](./class%28for%29.md)
  Returns the image representation subclass that handles the specified type of data.
- [class var registeredClasses: [AnyClass]](./registeredclasses.md)
  Returns an array containing the registered image representation classes.
- [class func registerClass(AnyClass)](./registerclass%28_%29.md)
  Adds the specified class to the registry of available image representation subclasses.
- [class func unregisterClass(AnyClass)](./unregisterclass%28_%29.md)
  Removes the specified image representation subclass from the registry of available image representations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimagerep/class(fortype:))*
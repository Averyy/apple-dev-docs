# class(for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Returns the image representation subclass that handles the specified type of data.

**Availability**:
- macOS

## Declaration

```swift
class func `class`(for data: Data) -> AnyClass?
```

```objc
+ (Class) imageRepClassForData:(NSData *) data;
```

#### Return Value

A `Class` object for the image representation that can handle the data, or `nil` if no image representation could handle the data.

## Parameters

- `data`: The image data.

## See Also

### Managing Representation Subclasses of Images
- [class func `class`(forType: String) -> AnyClass?](./class%28fortype%29.md)
  Returns the image representation subclass that handles image data for the specified UTI.
- [class var registeredClasses: [AnyClass]](./registeredclasses.md)
  Returns an array containing the registered image representation classes.
- [class func registerClass(AnyClass)](./registerclass%28_%29.md)
  Adds the specified class to the registry of available image representation subclasses.
- [class func unregisterClass(AnyClass)](./unregisterclass%28_%29.md)
  Removes the specified image representation subclass from the registry of available image representations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimagerep/class(for:))*
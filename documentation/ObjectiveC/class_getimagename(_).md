# class_getImageName(_:)

**Framework**: Objective-C Runtime  
**Kind**: func  
**Role**: Function

Returns the name of the dynamic library a class originated from.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func class_getImageName(_ cls: AnyClass?) -> UnsafePointer<CChar>?
```

```c
extern const char *class_getImageName(Class cls);
```

#### Return Value

A C string representing the name of the library containing the `cls` class.

## Parameters

- `cls`: The class you are inquiring about.

## See Also

### Working with Libraries
- [func objc_copyImageNames(UnsafeMutablePointer<UInt32>?) -> UnsafeMutablePointer<UnsafePointer<CChar>>](./objc_copyimagenames%28_%29.md)
  Returns the names of all the loaded Objective-C frameworks and dynamic libraries.
- [func objc_copyClassNamesForImage(UnsafePointer<CChar>, UnsafeMutablePointer<UInt32>?) -> UnsafeMutablePointer<UnsafePointer<CChar>>?](./objc_copyclassnamesforimage%28_,_%29.md)
  Returns the names of all the classes within a specified library or framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/class_getimagename(_:))*
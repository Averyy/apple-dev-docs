# objc_copyClassNamesForImage(_:_:)

**Framework**: Objective-C Runtime  
**Kind**: func

Returns the names of all the classes within a specified library or framework.

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
func objc_copyClassNamesForImage(_ image: UnsafePointer<CChar>, _ outCount: UnsafeMutablePointer<UInt32>?) -> UnsafeMutablePointer<UnsafePointer<CChar>>?
```

#### Return Value

An array of C strings representing all of the class names within the specified library or framework.

## Parameters

- `image`: The library or framework you are inquiring about.
- `outCount`: The number of class names in the returned array.

## See Also

- [func objc_copyImageNames(UnsafeMutablePointer<UInt32>?) -> UnsafeMutablePointer<UnsafePointer<CChar>>](objc_copyimagenames(_:).md)
  Returns the names of all the loaded Objective-C frameworks and dynamic libraries.
- [func class_getImageName(AnyClass?) -> UnsafePointer<CChar>?](class_getimagename(_:).md)
  Returns the name of the dynamic library a class originated from.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/objc_copyclassnamesforimage(_:_:))*
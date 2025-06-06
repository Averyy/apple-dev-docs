# objc_copyImageNames(_:)

**Framework**: Objective-C Runtime  
**Kind**: func

Returns the names of all the loaded Objective-C frameworks and dynamic libraries.

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
func objc_copyImageNames(_ outCount: UnsafeMutablePointer<UInt32>?) -> UnsafeMutablePointer<UnsafePointer<CChar>>
```

#### Return Value

An array of C strings representing the names of all the loaded Objective-C frameworks and dynamic libraries.

## Parameters

- `outCount`: The number of names in the returned array.

## See Also

- [func class_getImageName(AnyClass?) -> UnsafePointer<CChar>?](class_getimagename(_:).md)
  Returns the name of the dynamic library a class originated from.
- [func objc_copyClassNamesForImage(UnsafePointer<CChar>, UnsafeMutablePointer<UInt32>?) -> UnsafeMutablePointer<UnsafePointer<CChar>>?](objc_copyclassnamesforimage(_:_:).md)
  Returns the names of all the classes within a specified library or framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/objc_copyimagenames(_:))*
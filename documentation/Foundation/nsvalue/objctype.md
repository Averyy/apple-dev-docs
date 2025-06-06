# objCType

**Framework**: Foundation  
**Kind**: property

A C string containing the Objective-C type of the data contained in the value object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var objCType: UnsafePointer<CChar> { get }
```

#### Discussion

This property provides the same string produced by the `@encode()` compiler directive.

## See Also

- [init(bytes: UnsafeRawPointer, objCType: UnsafePointer<CChar>)](nsvalue/init(bytes:objctype:).md)
  Initializes a value object to contain the specified value, interpreted with the specified Objective-C type.
- [init(UnsafeRawPointer, withObjCType: UnsafePointer<CChar>)](nsvalue/init(_:withobjctype:).md)
  Creates a value object containing the specified value, interpreted with the specified Objective-C type.
- [func getValue(UnsafeMutableRawPointer)](nsvalue/getvalue(_:).md)
  Copies the value into the specified buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsvalue/objctype)*
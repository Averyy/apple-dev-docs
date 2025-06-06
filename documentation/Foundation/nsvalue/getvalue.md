# getValue(_:)

**Framework**: Foundation  
**Kind**: method

Copies the value into the specified buffer.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func getValue(_ value: UnsafeMutableRawPointer)
```

## Parameters

- `value`: A buffer into which to copy the value. The buffer must be large enough to hold the value.

## See Also

- [init(bytes: UnsafeRawPointer, objCType: UnsafePointer<CChar>)](nsvalue/init(bytes:objctype:).md)
  Initializes a value object to contain the specified value, interpreted with the specified Objective-C type.
- [init(UnsafeRawPointer, withObjCType: UnsafePointer<CChar>)](nsvalue/init(_:withobjctype:).md)
  Creates a value object containing the specified value, interpreted with the specified Objective-C type.
- [var objCType: UnsafePointer<CChar>](nsvalue/objctype.md)
  A C string containing the Objective-C type of the data contained in the value object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsvalue/getvalue(_:))*
# getValue(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Copies the value into the specified buffer.

**Availability**:
- iOS 2.0+ - Deprecated in 27.2
- iPadOS 2.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 10.0+ - Deprecated in 27.2
- tvOS 9.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 2.0+ - Deprecated in 27.2

## Declaration

```swift
func getValue(_ value: UnsafeMutableRawPointer)
```

```objc
- (void) getValue:(void *) value;
```

## Parameters

- `value`: A buffer into which to copy the value. The buffer must be large enough to hold the value.

## See Also

### Working with Raw Values
- [init(bytes: UnsafeRawPointer, objCType: UnsafePointer<CChar>)](./init%28bytes,objctype%29.md)
  Initializes a value object to contain the specified value, interpreted with the specified Objective-C type.
- [init(UnsafeRawPointer, withObjCType: UnsafePointer<CChar>)](./init%28_,withobjctype%29.md)
  Creates a value object containing the specified value, interpreted with the specified Objective-C type.
- [var objCType: UnsafePointer<CChar>](./objctype.md)
  A C string containing the Objective-C type of the data contained in the value object.
- [+ valueWithBytes:objCType:](./valuewithbytes_objctype_.md)
  Creates a value object containing the specified value, interpreted with the specified Objective-C type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsvalue/getvalue(_:))*
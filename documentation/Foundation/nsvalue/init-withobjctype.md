# init(_:withObjCType:)

**Framework**: Foundation  
**Kind**: init

Creates a value object containing the specified value, interpreted with the specified Objective-C type.

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
init(_ value: UnsafeRawPointer, withObjCType type: UnsafePointer<CChar>)
```

#### Return Value

A new value object that contains `value`, which is interpreted as being of the Objective-C type `type`.

#### Discussion

This method has the same effect as [`valueWithBytes:objCType:`](nsvalue/valuewithbytes:objctype:.md) and may be deprecated in a future release. You should use [`valueWithBytes:objCType:`](nsvalue/valuewithbytes:objctype:.md) instead.

## Parameters

- `value`: A pointer to data to be stored in the new value object.
- `type`: The Objective-C type of  , as provided by the   compiler directive. Do not hard-code this parameter as a C string.

## See Also

- [init(bytes: UnsafeRawPointer, objCType: UnsafePointer<CChar>)](nsvalue/init(bytes:objctype:).md)
  Initializes a value object to contain the specified value, interpreted with the specified Objective-C type.
- [func getValue(UnsafeMutableRawPointer)](nsvalue/getvalue(_:).md)
  Copies the value into the specified buffer.
- [var objCType: UnsafePointer<CChar>](nsvalue/objctype.md)
  A C string containing the Objective-C type of the data contained in the value object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsvalue/init(_:withobjctype:))*
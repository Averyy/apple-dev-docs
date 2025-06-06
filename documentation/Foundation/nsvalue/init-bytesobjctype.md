# init(bytes:objCType:)

**Framework**: Foundation  
**Kind**: init

Initializes a value object to contain the specified value, interpreted with the specified Objective-C type.

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
init(bytes value: UnsafeRawPointer, objCType type: UnsafePointer<CChar>)
```

#### Return Value

An initialized value object that contains `value`, which is interpreted as being of the Objective-C type `type`. The returned object might be different than the original receiver.

#### Discussion

See [`Number and Value Programming Topics`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NumbersandValues/NumbersandValues.html#//apple_ref/doc/uid/10000038i) for other considerations in creating a value object.

This is the designated initializer for the [`NSValue`](nsvalue.md) class.

## Parameters

- `value`: A pointer to data to be stored in the new value object.
- `type`: The Objective-C type of  , as provided by the   compiler directive. Do not hard-code this parameter as a C string.

## See Also

- [Number and Value Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NumbersandValues/NumbersandValues.html#//apple_ref/doc/uid/10000038i)
- [init(UnsafeRawPointer, withObjCType: UnsafePointer<CChar>)](nsvalue/init(_:withobjctype:).md)
  Creates a value object containing the specified value, interpreted with the specified Objective-C type.
- [func getValue(UnsafeMutableRawPointer)](nsvalue/getvalue(_:).md)
  Copies the value into the specified buffer.
- [var objCType: UnsafePointer<CChar>](nsvalue/objctype.md)
  A C string containing the Objective-C type of the data contained in the value object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsvalue/init(bytes:objctype:))*
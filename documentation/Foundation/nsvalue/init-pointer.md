# init(pointer:)

**Framework**: Foundation  
**Kind**: init

Creates a value object containing the specified pointer.

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
init(pointer: UnsafeRawPointer?)
```

#### Return Value

A new value object that contains `aPointer`.

#### Discussion

This method is equivalent to invoking [`init(_:withObjCType:)`](nsvalue/init(_:withobjctype:).md) in this manner:

```objc
NSValue *theValue = [NSValue value:&aPointer withObjCType:@encode(void *)];
```

This method does not copy the contents of `aPointer`, so you must not to free the memory at the pointer destination while the [`NSValue`](nsvalue.md) object exists. [`NSData`](nsdata.md) objects may be more suited for arbitrary pointers than [`NSValue`](nsvalue.md) objects.

## Parameters

- `pointer`: The value for the new object.

## See Also

- [init(nonretainedObject: Any?)](nsvalue/init(nonretainedobject:).md)
  Creates a value object containing the specified object.
- [var pointerValue: UnsafeMutableRawPointer?](nsvalue/pointervalue.md)
  Returns the value as an untyped pointer.
- [var nonretainedObjectValue: Any?](nsvalue/nonretainedobjectvalue.md)
  The value as a non-retained pointer to an object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsvalue/init(pointer:))*
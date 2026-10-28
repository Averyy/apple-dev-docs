# init(bytes:objCType:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

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

```objc
- (instancetype) initWithBytes:(const void *) value objCType:(const char *) type;
```

## Return Value

An initialized value object that contains `value`, which is interpreted as being of the Objective-C type `type`. The returned object might be different than the original receiver.

## Discussion

See [Number and Value Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NumbersandValues/NumbersandValues.html#//apple_ref/doc/uid/10000038i) for other considerations in creating a value object.

This is the designated initializer for the [`NSValue`](../nsvalue.md) class.

## Parameters

- `value`: A pointer to data to be stored in the new value object.
- `type`: The Objective-C type of `value`, as provided by the `@encode()` compiler directive. Do not hard-code this parameter as a C string.

## See Also

### Related Documentation
- [Number and Value Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NumbersandValues/NumbersandValues.html#//apple_ref/doc/uid/10000038i)
### Working with Raw Values
- [init(UnsafeRawPointer, withObjCType: UnsafePointer<CChar>)](./init%28_,withobjctype%29.md)
  Creates a value object containing the specified value, interpreted with the specified Objective-C type.
- [func getValue(UnsafeMutableRawPointer)](./getvalue%28_%29.md)
  Copies the value into the specified buffer.
- [var objCType: UnsafePointer<CChar>](./objctype.md)
  A C string containing the Objective-C type of the data contained in the value object.
- [+ valueWithBytes:objCType:](./valuewithbytes_objctype_.md)
  Creates a value object containing the specified value, interpreted with the specified Objective-C type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsvalue/init(bytes:objctype:))*
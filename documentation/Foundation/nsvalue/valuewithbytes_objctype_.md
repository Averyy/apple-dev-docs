# valueWithBytes:objCType:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

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

```objc
+ (NSValue *) valueWithBytes:(const void *) value objCType:(const char *) type;
```

## Return Value

A new value object that contains `value`, which is interpreted as being of the Objective-C type `type`.

## Discussion

See [Number and Value Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NumbersandValues/NumbersandValues.html#//apple_ref/doc/uid/10000038i) for other considerations in creating a value object and code examples.

## Parameters

- `value`: A pointer to data to be stored in the new value object.
- `type`: The Objective-C type of `value`, as provided by the `@encode()` compiler directive. Do not hard-code this parameter as a C string.

## See Also

### Working with Raw Values
- [init(bytes: UnsafeRawPointer, objCType: UnsafePointer<CChar>)](./init%28bytes,objctype%29.md)
  Initializes a value object to contain the specified value, interpreted with the specified Objective-C type.
- [init(UnsafeRawPointer, withObjCType: UnsafePointer<CChar>)](./init%28_,withobjctype%29.md)
  Creates a value object containing the specified value, interpreted with the specified Objective-C type.
- [func getValue(UnsafeMutableRawPointer)](./getvalue%28_%29.md)
  Copies the value into the specified buffer.
- [var objCType: UnsafePointer<CChar>](./objctype.md)
  A C string containing the Objective-C type of the data contained in the value object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsvalue/valuewithbytes:objctype:)*
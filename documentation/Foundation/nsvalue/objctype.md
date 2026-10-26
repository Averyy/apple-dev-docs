# objCType

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly) const char * objCType;
```

#### Discussion

This property provides the same string produced by the `@encode()` compiler directive.

## See Also

### Working with Raw Values
- [init(bytes: UnsafeRawPointer, objCType: UnsafePointer<CChar>)](./init%28bytes,objctype%29.md)
  Initializes a value object to contain the specified value, interpreted with the specified Objective-C type.
- [init(UnsafeRawPointer, withObjCType: UnsafePointer<CChar>)](./init%28_,withobjctype%29.md)
  Creates a value object containing the specified value, interpreted with the specified Objective-C type.
- [func getValue(UnsafeMutableRawPointer)](./getvalue%28_%29.md)
  Copies the value into the specified buffer.
- [+ valueWithBytes:objCType:](./valuewithbytes_objctype_.md)
  Creates a value object containing the specified value, interpreted with the specified Objective-C type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsvalue/objctype)*
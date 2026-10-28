# type

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The argument’s resource type.

**Availability**:
- iOS 8.0+ - Deprecated in 16.0
- iPadOS 8.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.11+ - Deprecated in 13.0
- tvOS - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
var type: MTLArgumentType { get }
```

```objc
@property (readonly) MTLArgumentType type;
```

## Discussion

This property indicates which type of resource is used (buffer, texture, sampler, or threadgroup memory) in the shading language code. For information on possible values, see [`MTLArgumentType`](../mtlargumenttype.md).

## See Also

### Describing the argument
- [var name: String](./name.md)
  The name of the argument.
- [var isActive: Bool](./isactive.md)
  A Boolean that indicates whether the compiled function uses the argument.
- [var index: Int](./index.md)
  The index in the argument table that corresponds to the function argument.
- [var access: MTLBindingAccess](./access.md)
  The argument’s read and/or write access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlargument/type)*
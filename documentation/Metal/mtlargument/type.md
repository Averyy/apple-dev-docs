# type

**Framework**: Metal  
**Kind**: property

The argument’s resource type.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var type: MTLArgumentType { get }
```

#### Discussion

This property indicates which type of resource is used (buffer, texture, sampler, or threadgroup memory) in the shading language code. For information on possible values, see [`MTLArgumentType`](mtlargumenttype.md).

## See Also

- [var name: String](mtlargument/name.md)
  The name of the argument.
- [var isActive: Bool](mtlargument/isactive.md)
  A Boolean that indicates whether the compiled function uses the argument.
- [var index: Int](mtlargument/index.md)
  The index in the argument table that corresponds to the function argument.
- [var access: MTLBindingAccess](mtlargument/access.md)
  The argument’s read and/or write access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlargument/type)*
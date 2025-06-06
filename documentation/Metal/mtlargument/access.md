# access

**Framework**: Metal  
**Kind**: property

The argument’s read and/or write access.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var access: MTLBindingAccess { get }
```

#### Discussion

This property indicates the type of access qualifiers (read-only, write-only, or read-write) used in the Metal shading language code. For information on possible values, see [`MTLArgumentAccess`](mtlargumentaccess.md).

## See Also

- [var name: String](mtlargument/name.md)
  The name of the argument.
- [var isActive: Bool](mtlargument/isactive.md)
  A Boolean that indicates whether the compiled function uses the argument.
- [var index: Int](mtlargument/index.md)
  The index in the argument table that corresponds to the function argument.
- [var type: MTLArgumentType](mtlargument/type.md)
  The argument’s resource type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlargument/access)*
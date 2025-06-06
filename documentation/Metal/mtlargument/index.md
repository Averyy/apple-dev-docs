# index

**Framework**: Metal  
**Kind**: property

The index in the argument table that corresponds to the function argument.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var index: Int { get }
```

#### Discussion

A command encoder ([`MTLComputeCommandEncoder`](mtlcomputecommandencoder.md) or [`MTLRenderCommandEncoder`](mtlrendercommandencoder.md)) specifies the index in the corresponding argument table. For example, an app can call the [`setTexture(_:index:)`](mtlcomputecommandencoder/settexture(_:index:).md) method of [`MTLComputeCommandEncoder`](mtlcomputecommandencoder.md) to specify an index in the texture argument table for a [`MTLTexture`](mtltexture.md) object that is used as an argument of a compute function.

## See Also

- [var name: String](mtlargument/name.md)
  The name of the argument.
- [var isActive: Bool](mtlargument/isactive.md)
  A Boolean that indicates whether the compiled function uses the argument.
- [var type: MTLArgumentType](mtlargument/type.md)
  The argument’s resource type.
- [var access: MTLBindingAccess](mtlargument/access.md)
  The argument’s read and/or write access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlargument/index)*
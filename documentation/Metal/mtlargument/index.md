# index

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The index in the argument table that corresponds to the function argument.

**Availability**:
- iOS 8.0+ - Deprecated in 16.0
- iPadOS 8.0+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.11+ - Deprecated in 13.0
- tvOS - Deprecated in 16.0
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
var index: Int { get }
```

```objc
@property (readonly) NSUInteger index;
```

## Discussion

A command encoder ([`MTLComputeCommandEncoder`](../mtlcomputecommandencoder.md) or [`MTLRenderCommandEncoder`](../mtlrendercommandencoder.md)) specifies the index in the corresponding argument table. For example, an app can call the [`setTexture(_:index:)`](../mtlcomputecommandencoder/settexture%28_,index%29.md) method of [`MTLComputeCommandEncoder`](../mtlcomputecommandencoder.md) to specify an index in the texture argument table for an [`MTLTexture`](../mtltexture.md) instance that is used as an argument of a compute function.

## See Also

### Describing the argument
- [var name: String](./name.md)
  The name of the argument.
- [var isActive: Bool](./isactive.md)
  A Boolean that indicates whether the compiled function uses the argument.
- [var type: MTLArgumentType](./type.md)
  The argument’s resource type.
- [var access: MTLBindingAccess](./access.md)
  The argument’s read and/or write access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlargument/index)*
# CFTreeContext

**Framework**: Core Foundation  
**Kind**: struct

Structure containing program-defined data and callbacks for a CFTree object.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct CFTreeContext
```

## Topics

### Initializers
- [init()](cftreecontext/init.md)
- [init(version: CFIndex, info: UnsafeMutableRawPointer!, retain: CFTreeRetainCallBack!, release: CFTreeReleaseCallBack!, copyDescription: CFTreeCopyDescriptionCallBack!)](cftreecontext/init(version:info:retain:release:copydescription:).md)
### Instance Properties
- [var copyDescription: CFTreeCopyDescriptionCallBack!](cftreecontext/copydescription.md)
  The callback used to provide a description of the `info` field.
- [var info: UnsafeMutableRawPointer!](cftreecontext/info.md)
  A C pointer to a program-defined block of data, referred to as the information pointer.
- [var release: CFTreeReleaseCallBack!](cftreecontext/release.md)
  The callback used to release a previously retained `info` field. If this parameter is not a pointer to a function of the correct prototype, the behavior is undefined. This value may be `NULL`.
- [var retain: CFTreeRetainCallBack!](cftreecontext/retain.md)
  The callback used to retain the `info` field. If this parameter is not a pointer to a function of the correct prototype, the behavior is undefined. This value may be `NULL`.
- [var version: CFIndex](cftreecontext/version.md)
  The version number of the structure type being passed in as a parameter to a CFTree creation function. This structure is version `0`.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cftreecontext)*
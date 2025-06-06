# GLKTextureLoaderCallback

**Framework**: GLKit  
**Kind**: typealias

Signature for the block executed after an asynchronous texture loading operation completes.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
typealias GLKTextureLoaderCallback = (GLKTextureInfo?, (any Error)?) -> Void
```

#### Discussion

The block parameters are defined as follows:

## See Also

- [Texture Loading Options](texture-loading-options.md)
  Keys to specify in a `textureOperations` dictionary.
- [Texture Error Handling](texture-error-handling.md)
  Strings used when handling error messages returned from a texture loading method.
- [GLKTextureLoaderError.Code](glktextureloadererror-swift.struct/code.md)
  Values to be returned when a texture loader encounters an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glktextureloadercallback)*
# texture(withContentsOf:options:)

**Framework**: GLKit  
**Kind**: method  
**Role**: Type Method

Loads a 2D texture image from a memory range and creates a new texture from the data.

**Availability**:
- iOS 5.0+ - Deprecated in 12.0
- iPadOS 5.0+ - Deprecated in 12.0
- macOS 10.8+ - Deprecated in 10.14
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
class func texture(withContentsOf data: Data, options: [String : NSNumber]? = nil) throws -> GLKTextureInfo
```

```objc
+ (GLKTextureInfo *) textureWithContentsOfData:(NSData *) data options:(NSDictionary<NSString *,NSNumber *> *) options error:(NSError **) outError;
```

#### Return Value

A texture info object that describes the loaded texture or `nil` if an error occurred.

#### Discussion

This class method loads the texture into the sharegroup attached to the current context for the thread this method is called on.

> **Handling Errors in Swift**:  In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `data`: The memory range to load as a texture.
- `options`: A dictionary that describes any additional steps you want the texture loader to take when loading the texture. See [Texture Loading Options](../texture-loading-options.md).

## See Also

### Creating Textures from In-Memory Representations
- [func texture(withContentsOf: Data, options: [String : NSNumber]?, queue: dispatch_queue_t?, completionHandler: (GLKTextureInfo?, (any Error)?) -> Void)](./texture%28withcontentsof,options,queue,completionhandler%29-6n0cf.md)
  Asynchronously loads a 2D texture image from a memory range and creates a new texture from the data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glktextureloader/texture(withcontentsof:options:)-2ljxb)*
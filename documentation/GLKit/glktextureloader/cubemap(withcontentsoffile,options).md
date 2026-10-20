# cubeMap(withContentsOfFile:options:)

**Framework**: GLKit  
**Kind**: method  
**Role**: Type Method

Loads a cube map texture image from a single file and creates a new texture from the data.

**Availability**:
- iOS 5.0+ - Deprecated in 12.0
- iPadOS 5.0+ - Deprecated in 12.0
- macOS 10.8+ - Deprecated in 10.14
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
class func cubeMap(withContentsOfFile path: String, options: [String : NSNumber]? = nil) throws -> GLKTextureInfo
```

```objc
+ (GLKTextureInfo *) cubeMapWithContentsOfFile:(NSString *) path options:(NSDictionary<NSString *,NSNumber *> *) options error:(NSError **) outError;
```

#### Return Value

A texture info object that describes the loaded texture or `nil` if an error occurred.

#### Discussion

The file is assumed to be a single image that includes the six faces of the cube map. The image’s height must be six times the width, and the images should be arranged in the following order from top to bottom: north, south, east, west, top, bottom. Alternatively, the image can have a width that is six times the height, and arranged from left to right, but this takes additional processing to load.

This class method loads the texture into the sharegroup attached to the current context for the thread this method is called on.

> **Handling Errors in Swift**:  In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `path`: A path to the file to load.
- `options`: A dictionary that describes any additional steps you want the texture loader to take when loading the texture. See [Texture Loading Options](../texture-loading-options.md).

## See Also

### Loading Cube Maps from Files
- [func cubeMap(withContentsOfFile: String, options: [String : NSNumber]?, queue: dispatch_queue_t?, completionHandler: (GLKTextureInfo?, (any Error)?) -> Void)](./cubemap%28withcontentsoffile,options,queue,completionhandler%29.md)
  Asynchronously loads a cube map texture image from a single file and creates a new texture from the data.
- [class func cubeMap(withContentsOfFiles: [Any], options: [String : NSNumber]?) throws -> GLKTextureInfo](./cubemap%28withcontentsoffiles,options%29.md)
  Loads a cube map texture image from a series of files and creates a new texture from the data.
- [func cubeMap(withContentsOfFiles: [Any], options: [String : NSNumber]?, queue: dispatch_queue_t?, completionHandler: (GLKTextureInfo?, (any Error)?) -> Void)](./cubemap%28withcontentsoffiles,options,queue,completionhandler%29.md)
  Asynchronously loads a cube map texture image from a series of files and creates a new texture from the data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glktextureloader/cubemap(withcontentsoffile:options:))*
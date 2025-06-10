# cubeMap(withContentsOfFile:options:)

**Framework**: GLKit  
**Kind**: method

Loads a cube map texture image from a single file and creates a new texture from the data.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
class func cubeMap(withContentsOfFile path: String, options: [String : NSNumber]? = nil) throws -> GLKTextureInfo
```

#### Return Value

A texture info object that describes the loaded texture or `nil` if an error occurred.

#### Discussion

The file is assumed to be a single image that includes the six faces of the cube map. The image’s height must be six times the width, and the images should be arranged in the following order from top to bottom: north, south, east, west, top, bottom. Alternatively, the image can have a width that is six times the height, and arranged from left to right, but this takes additional processing to load.

This class method loads the texture into the sharegroup attached to the current context for the thread this method is called on.

> **Note**:  In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `path`: A path to the file to load.
- `options`: A dictionary that describes any additional steps you want the texture loader to take when loading the texture. See  .

## See Also

- [func cubeMap(withContentsOfFile: String, options: [String : NSNumber]?, queue: dispatch_queue_t?, completionHandler: (GLKTextureInfo?, (any Error)?) -> Void)](glktextureloader/cubemap(withcontentsoffile:options:queue:completionhandler:).md)
  Asynchronously loads a cube map texture image from a single file and creates a new texture from the data.
- [class func cubeMap(withContentsOfFiles: [Any], options: [String : NSNumber]?) throws -> GLKTextureInfo](glktextureloader/cubemap(withcontentsoffiles:options:).md)
  Loads a cube map texture image from a series of files and creates a new texture from the data.
- [func cubeMap(withContentsOfFiles: [Any], options: [String : NSNumber]?, queue: dispatch_queue_t?, completionHandler: (GLKTextureInfo?, (any Error)?) -> Void)](glktextureloader/cubemap(withcontentsoffiles:options:queue:completionhandler:).md)
  Asynchronously loads a cube map texture image from a series of files and creates a new texture from the data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glktextureloader/cubemap(withcontentsoffile:options:))*
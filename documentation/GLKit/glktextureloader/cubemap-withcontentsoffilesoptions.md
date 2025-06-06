# cubeMap(withContentsOfFiles:options:)

**Framework**: GLKit  
**Kind**: method

Loads a cube map texture image from a series of files and creates a new texture from the data.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
class func cubeMap(withContentsOfFiles paths: [Any], options: [String : NSNumber]? = nil) throws -> GLKTextureInfo
```

#### Return Value

A texture info object that describes the loaded texture or `nil` if an error occurred.

#### Discussion

The array of file paths must include six entries for the six faces of the cube map. The URLs should be arranged in the following order: Right(+x), Left(-x), Top(+y), Bottom(-y), Front(+z), Back(-z). This coordinate system is left-handed if you think of yourself within the cube. The coordinate system is right-handed if you think of yourself outside of the cube.

This class method loads the texture into the sharegroup attached to the current context for the thread this method is called on.

> **Note**:  In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

 In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.

You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `paths`: An array of   or   objects that provide the paths to the six files that make up the cube map.
- `options`: A dictionary that describes any additional steps you want the texture loader to take when loading the texture. See  .

## Topics

### Related Documentation
- [func cubeMap(withContentsOf: URL, options: [String : NSNumber]?, queue: dispatch_queue_t?, completionHandler: GLKTextureLoaderCallback)](glktextureloader/cubemap(withcontentsof:options:queue:completionhandler:).md)
  Asynchronously loads a cube map texture image from a single URL and creates a new texture from the data.

## See Also

- [class func cubeMap(withContentsOfFile: String, options: [String : NSNumber]?) throws -> GLKTextureInfo](glktextureloader/cubemap(withcontentsoffile:options:).md)
  Loads a cube map texture image from a single file and creates a new texture from the data.
- [func cubeMap(withContentsOfFile: String, options: [String : NSNumber]?, queue: dispatch_queue_t?, completionHandler: GLKTextureLoaderCallback)](glktextureloader/cubemap(withcontentsoffile:options:queue:completionhandler:).md)
  Asynchronously loads a cube map texture image from a single file and creates a new texture from the data.
- [func cubeMap(withContentsOfFiles: [Any], options: [String : NSNumber]?, queue: dispatch_queue_t?, completionHandler: GLKTextureLoaderCallback)](glktextureloader/cubemap(withcontentsoffiles:options:queue:completionhandler:).md)
  Asynchronously loads a cube map texture image from a series of files and creates a new texture from the data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glktextureloader/cubemap(withcontentsoffiles:options:))*
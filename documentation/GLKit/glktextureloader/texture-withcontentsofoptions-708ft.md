# texture(withContentsOf:options:)

**Framework**: GLKit  
**Kind**: method

Loads a 2D texture image from a URL and creates a new texture from the data.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
class func texture(withContentsOf url: URL, options: [String : NSNumber]? = nil) throws -> GLKTextureInfo
```

#### Return Value

A texture info object that describes the loaded texture or `nil` if an error occurred.

#### Discussion

This class method loads the texture into the sharegroup attached to the current context for the thread this method is called on.

> **Note**:  In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

 In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.

You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `url`: A URL to the file to load.
- `options`: A dictionary that describes any additional steps you want the texture loader to take when loading the texture. See  .

## See Also

- [func texture(withContentsOf: URL, options: [String : NSNumber]?, queue: dispatch_queue_t?, completionHandler: GLKTextureLoaderCallback)](glktextureloader/texture(withcontentsof:options:queue:completionhandler:)-55187.md)
  Asynchronously loads a 2D texture image from a URL and creates a new texture from the data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glktextureloader/texture(withcontentsof:options:)-708ft)*
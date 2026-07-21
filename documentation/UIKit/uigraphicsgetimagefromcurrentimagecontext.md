# UIGraphicsGetImageFromCurrentImageContext()

**Framework**: UIKit  
**Kind**: func

Returns an image from the contents of the current bitmap-based graphics context.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func UIGraphicsGetImageFromCurrentImageContext() -> UIImage?
```

#### Return Value

A image object containing the contents of the current bitmap graphics context.

#### Discussion

You should call this function only when a bitmap-based graphics context is the current graphics context. If the current context is `nil` or was not created by a call to [`UIGraphicsBeginImageContext(_:)`](uigraphicsbeginimagecontext(_:).md), this function returns `nil`.

This function may be called from any thread of your app.

## See Also

- [func UIApplicationMain(Int32, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>!, String?, String?) -> Int32](uiapplicationmain(_:_:_:_:)-9jjn8.md)
  Creates the application object and the application delegate and sets up the event cycle.
- [func UIGraphicsBeginImageContext(CGSize)](uigraphicsbeginimagecontext(_:).md)
  Creates a bitmap-based graphics context and makes it the current context.
- [func UIGraphicsEndImageContext()](uigraphicsendimagecontext().md)
  Removes the current bitmap-based graphics context from the top of the stack.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicsgetimagefromcurrentimagecontext())*
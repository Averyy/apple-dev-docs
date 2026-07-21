# UIGraphicsEndImageContext()

**Framework**: UIKit  
**Kind**: func

Removes the current bitmap-based graphics context from the top of the stack.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func UIGraphicsEndImageContext()
```

#### Discussion

You use this function to clean up the drawing environment put in place by the [`UIGraphicsBeginImageContext(_:)`](uigraphicsbeginimagecontext(_:).md) function and to remove the corresponding bitmap-based graphics context from the top of the stack. If the current context was not created using the [`UIGraphicsBeginImageContext(_:)`](uigraphicsbeginimagecontext(_:).md) function, this function does nothing.

This function may be called from any thread of your app.

## See Also

- [func UIApplicationMain(Int32, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>!, String?, String?) -> Int32](uiapplicationmain(_:_:_:_:)-9jjn8.md)
  Creates the application object and the application delegate and sets up the event cycle.
- [func UIGraphicsBeginImageContext(CGSize)](uigraphicsbeginimagecontext(_:).md)
  Creates a bitmap-based graphics context and makes it the current context.
- [func UIGraphicsGetImageFromCurrentImageContext() -> UIImage?](uigraphicsgetimagefromcurrentimagecontext().md)
  Returns an image from the contents of the current bitmap-based graphics context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicsendimagecontext())*
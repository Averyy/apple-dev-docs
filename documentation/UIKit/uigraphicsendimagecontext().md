# UIGraphicsEndImageContext()

**Framework**: UIKit  
**Kind**: func  
**Role**: Function

Removes the current bitmap-based graphics context from the top of the stack.

**Availability**:
- iOS 2.0+ - Deprecated in 27.0
- iPadOS 2.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.2
- tvOS - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: Use [`UIGraphicsImageRenderer`](./uigraphicsimagerenderer.md) instead.

## Declaration

```swift
func UIGraphicsEndImageContext()
```

```c
extern void UIGraphicsEndImageContext();
```

## Discussion

You use this function to clean up the drawing environment put in place by the [`UIGraphicsBeginImageContext(_:)`](./uigraphicsbeginimagecontext%28_%29.md) function and to remove the corresponding bitmap-based graphics context from the top of the stack. If the current context was not created using the [`UIGraphicsBeginImageContext(_:)`](./uigraphicsbeginimagecontext%28_%29.md) function, this function does nothing.

This function may be called from any thread of your app.

## See Also

### Deprecated functions
- [func UIApplicationMain(Int32, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>!, String?, String?) -> Int32](./uiapplicationmain%28_,_,_,_%29-9jjn8.md)
  Creates the application object and the application delegate and sets up the event cycle.
- [func UIGraphicsBeginImageContext(CGSize)](./uigraphicsbeginimagecontext%28_%29.md)
  Creates a bitmap-based graphics context and makes it the current context.
- [func UIGraphicsGetImageFromCurrentImageContext() -> UIImage?](./uigraphicsgetimagefromcurrentimagecontext%28%29.md)
  Returns an image from the contents of the current bitmap-based graphics context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicsendimagecontext())*
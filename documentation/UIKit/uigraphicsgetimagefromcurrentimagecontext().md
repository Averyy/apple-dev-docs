# UIGraphicsGetImageFromCurrentImageContext()

**Framework**: UIKit  
**Kind**: func  
**Role**: Function

Returns an image from the contents of the current bitmap-based graphics context.

**Availability**:
- iOS 2.0+ - Deprecated in 27.0
- iPadOS 2.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.2
- tvOS - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: Use [`currentImage`](./uigraphicsimagerenderercontext/currentimage.md) instead.

## Declaration

```swift
func UIGraphicsGetImageFromCurrentImageContext() -> UIImage?
```

```c
extern UIImage *UIGraphicsGetImageFromCurrentImageContext();
```

#### Return Value

A image object containing the contents of the current bitmap graphics context.

#### Discussion

You should call this function only when a bitmap-based graphics context is the current graphics context. If the current context is `nil` or was not created by a call to [`UIGraphicsBeginImageContext(_:)`](./uigraphicsbeginimagecontext%28_%29.md), this function returns `nil`.

This function may be called from any thread of your app.

## See Also

### Deprecated functions
- [func UIApplicationMain(Int32, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>!, String?, String?) -> Int32](./uiapplicationmain%28_,_,_,_%29-9jjn8.md)
  Creates the application object and the application delegate and sets up the event cycle.
- [func UIGraphicsBeginImageContext(CGSize)](./uigraphicsbeginimagecontext%28_%29.md)
  Creates a bitmap-based graphics context and makes it the current context.
- [func UIGraphicsEndImageContext()](./uigraphicsendimagecontext%28%29.md)
  Removes the current bitmap-based graphics context from the top of the stack.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicsgetimagefromcurrentimagecontext())*
# UIGraphicsBeginImageContext(_:)

**Framework**: UIKit  
**Kind**: func  
**Role**: Function

Creates a bitmap-based graphics context and makes it the current context.

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
func UIGraphicsBeginImageContext(_ size: CGSize)
```

```c
extern void UIGraphicsBeginImageContext(CGSize size);
```

#### Discussion

This function is equivalent to calling the [`UIGraphicsBeginImageContextWithOptions(_:_:_:)`](./uigraphicsbeginimagecontextwithoptions%28_,_,_%29.md) function with the opaque parameter set to [`false`](../Swift/false.md) and a scale factor of `1.0`.

This function may be called from any thread of your app.

## Parameters

- `size`: The size of the new bitmap context. This represents the size of the image returned by the [`UIGraphicsGetImageFromCurrentImageContext()`](./uigraphicsgetimagefromcurrentimagecontext%28%29.md) function.

## See Also

### Deprecated functions
- [func UIApplicationMain(Int32, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>!, String?, String?) -> Int32](./uiapplicationmain%28_,_,_,_%29-9jjn8.md)
  Creates the application object and the application delegate and sets up the event cycle.
- [func UIGraphicsGetImageFromCurrentImageContext() -> UIImage?](./uigraphicsgetimagefromcurrentimagecontext%28%29.md)
  Returns an image from the contents of the current bitmap-based graphics context.
- [func UIGraphicsEndImageContext()](./uigraphicsendimagecontext%28%29.md)
  Removes the current bitmap-based graphics context from the top of the stack.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicsbeginimagecontext(_:))*
# UIGraphicsBeginImageContext(_:)

**Framework**: UIKit  
**Kind**: func

Creates a bitmap-based graphics context and makes it the current context.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func UIGraphicsBeginImageContext(_ size: CGSize)
```

#### Discussion

This function is equivalent to calling the [`UIGraphicsBeginImageContextWithOptions(_:_:_:)`](uigraphicsbeginimagecontextwithoptions(_:_:_:).md) function with the opaque parameter set to [`false`](https://developer.apple.com/documentation/swift/false) and a scale factor of `1.0`.

This function may be called from any thread of your app.

## Parameters

- `size`: The size of the new bitmap context. This represents the size of the image returned by the [`UIGraphicsGetImageFromCurrentImageContext()`](uigraphicsgetimagefromcurrentimagecontext().md) function.

## See Also

- [func UIApplicationMain(Int32, UnsafeMutablePointer<UnsafeMutablePointer<Int8>>!, String?, String?) -> Int32](uiapplicationmain(_:_:_:_:)-9jjn8.md)
  Creates the application object and the application delegate and sets up the event cycle.
- [func UIGraphicsGetImageFromCurrentImageContext() -> UIImage?](uigraphicsgetimagefromcurrentimagecontext().md)
  Returns an image from the contents of the current bitmap-based graphics context.
- [func UIGraphicsEndImageContext()](uigraphicsendimagecontext().md)
  Removes the current bitmap-based graphics context from the top of the stack.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicsbeginimagecontext(_:))*
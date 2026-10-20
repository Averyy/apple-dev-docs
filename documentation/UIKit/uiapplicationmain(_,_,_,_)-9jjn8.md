# UIApplicationMain(_:_:_:_:)

**Framework**: UIKit  
**Kind**: func  
**Role**: Function

Creates the application object and the application delegate and sets up the event cycle.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS
- Swift - Deprecated in 4.2

> **Deprecated**: Use [@main](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/attributes/#main) instead.

## Declaration

```swift
func UIApplicationMain(_ argc: Int32, _ argv: UnsafeMutablePointer<UnsafeMutablePointer<Int8>>!, _ principalClassName: String?, _ delegateClassName: String?) -> Int32
```

#### Return Value

Even though an integer return type is specified, this function never returns. When users exits an iOS app by pressing the Home button, the application moves to the background.

#### Discussion

This function instantiates the application object from the principal class and instantiates the delegate (if any) from the given class and sets the delegate for the application. It also sets up the main event loop, including the application’s run loop, and begins processing events. If the application’s `Info.plist` file specifies a main nib file to be loaded, by including the [`NSMainNibFile`](../BundleResources/information-property-list/nsmainnibfile.md) key and a valid nib file name for the value, this function loads that nib file.

Despite the declared return type, this function never returns.

## Parameters

- `argc`: The count of arguments in `argv`; this usually is the corresponding parameter to `main`.
- `argv`: A variable list of arguments; this usually is the corresponding parameter to `main`.
- `principalClassName`: The name of the [`UIApplication`](./uiapplication.md) class or subclass. If you specify `nil`, [`UIApplication`](./uiapplication.md) is assumed.
- `delegateClassName`: The name of the class from which the application delegate is instantiated. If `principalClassName` designates a subclass of [`UIApplication`](./uiapplication.md), you may designate the subclass as the delegate; the subclass instance receives the application-delegate messages. Specify `nil` if you load the delegate object from your application’s main nib file.

## See Also

### Deprecated functions
- [func UIGraphicsBeginImageContext(CGSize)](./uigraphicsbeginimagecontext%28_%29.md)
  Creates a bitmap-based graphics context and makes it the current context.
- [func UIGraphicsGetImageFromCurrentImageContext() -> UIImage?](./uigraphicsgetimagefromcurrentimagecontext%28%29.md)
  Returns an image from the contents of the current bitmap-based graphics context.
- [func UIGraphicsEndImageContext()](./uigraphicsendimagecontext%28%29.md)
  Removes the current bitmap-based graphics context from the top of the stack.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplicationmain(_:_:_:_:)-9jjn8)*
# shared

**Framework**: AppKit  
**Kind**: property

Returns the application instance, creating it if it doesn’t exist yet.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class var shared: NSApplication { get }
```

## Mentions

- [Passing control from one app to another with cooperative activation](passing-control-from-one-app-to-another-with-cooperative-activation.md)

#### Return Value

The shared application object.

#### Discussion

This method also makes a connection to the window server and completes other initialization. Your program should invoke this method as one of the first statements in `main()`; this invoking is done for you if you create your application with Xcode. To retrieve the `NSApplication` instance after it has been created, use the global variable [`NSApp`](nsapp.md) or invoke this method.

## See Also

- [Mac App Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/MOSXAppProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010543)
- [func run()](nsapplication/run.md)
  Starts the main event loop.
- [func terminate(Any?)](nsapplication/terminate(_:).md)
  Terminates the receiver.
- [var NSApp: NSApplication!](nsapp.md)
  The global variable for the shared app instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/shared)*
# shared

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Returns the application instance, creating it if it doesn’t exist yet.

**Availability**:
- macOS

## Declaration

```swift
class var shared: NSApplication { get }
```

```objc
@property (class, strong, readonly) NSApplication * sharedApplication;
```

## Mentions

- [Passing control from one app to another with cooperative activation](../passing-control-from-one-app-to-another-with-cooperative-activation.md)

## Return Value

The shared application object.

## Discussion

This method also makes a connection to the window server and completes other initialization. Your program should invoke this method as one of the first statements in `main()`; this invoking is done for you if you create your application with Xcode. To retrieve the `NSApplication` instance after it has been created, use the global variable [`NSApp`](../nsapp.md) or invoke this method.

## See Also

### Related Documentation
- [func run()](./run%28%29.md)
  Starts the main event loop.
- [func terminate(Any?)](./terminate%28_%29.md)
  Terminates the receiver.
### Getting the shared app object
- [var NSApp: NSApplication!](../nsapp.md)
  The global variable for the shared app instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/shared)*
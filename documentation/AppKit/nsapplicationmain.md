# NSApplicationMain(_:_:)

**Framework**: AppKit  
**Kind**: func

Called by the main function to create and run the application.

**Availability**:
- macOS 10.9+

## Declaration

```swift
func NSApplicationMain(_ argc: Int32, _ argv: UnsafeMutablePointer<UnsafeMutablePointer<CChar>?>) -> Int32
```

#### Return Value

This method never returns a result code. Instead, it calls the `exit` function to exit the application and terminate the process. If you want to determine why the application exited, you should look at the result code from the `exit` function instead.

#### Discussion

Creates the application, loads the main nib file from the application’s main bundle, and runs the application. You must call this function from the main thread of your application, and you typically call it only once from your application’s `main` function. Your `main` function is usually generated automatically by Xcode.

##### Special Considerations

`NSApplicationMain` itself ignores the `argc` and `argv` arguments. Instead, Cocoa gets its arguments indirectly through `_NSGetArgv`, `_NSGetArgc`, and `_NSGetEnviron` (see <crt_externs.h>).

## Parameters

- `argc`: The number of arguments in the   parameter.
- `argv`: An array of pointers containing the arguments passed to the application at startup.

## See Also

- [class NSApplication](nsapplication.md)
  An object that manages an app’s main event loop and resources used by all of that app’s objects.
- [class NSRunningApplication](nsrunningapplication.md)
  An object that can manipulate and provide information for a single instance of an app.
- [protocol NSApplicationDelegate](nsapplicationdelegate.md)
  A set of methods that manage your app’s life cycle and its interaction with common system services.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplicationmain(_:_:))*
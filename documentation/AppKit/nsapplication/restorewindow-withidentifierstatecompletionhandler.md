# restoreWindow(withIdentifier:state:completionHandler:)

**Framework**: AppKit  
**Kind**: method

Invoked to request that a window be restored.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func restoreWindow(withIdentifier identifier: NSUserInterfaceItemIdentifier, state: NSCoder, completionHandler: @escaping (NSWindow?, (any Error)?) -> Void) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the window was restored; otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

If the receiver knows how to restore the identified window, it should invoke the completion handler with the window, possibly creating it. It is acceptable to use a pre-existing window, though you should not pass the same window to more than one completion handler. If the receiver cannot restore the identified window (for example, the window referenced a document that has been deleted), it should invoke the completion handler with a nil window.

The receiver is app is passed the identifier of the window, which allows it to quickly check for known windows.  For example, you might give your preferences window an identifier of “preferences” in the nib, and then check for that identifier in your implementation.  The receiver is also passed the `NSCoder` instance containing the combined restorable state of the window, its delegate, the window controller, and any document.  The receiver may decode information previously stored in the coder to determine what window to restore.

> **Note**:  The app may invoke the completion handler before or after the method returns, and on any queue.  If you plan to invoke the completion handler after the method returns, you must copy the completion handler via the `copy` method. It is not necessary or recommended for implementations of this method to order restored windows onscreen (for example, the window may have been minimized, in which case it will not be ordered onscreen)

## Parameters

- `identifier`: The unique interface item identifier string that was previously associated with the window. Use this string to determine which window to create.
- `state`: A coder object containing the window state information. This coder object contains the combined restorable state of the window, which can include the state of the window, its delegate, window controller, and document object. You can use this state to determine which window to create.
- `completionHandler`: A Block object to execute with the results of creating the window. You must execute this block at some point but may do so after the method returns if needed. This block takes the following parameters:

## See Also

- [var isProtectedDataAvailable: Bool](nsapplication/isprotecteddataavailable.md)
- [func extendStateRestoration()](nsapplication/extendstaterestoration.md)
  Allows an app to extend its state restoration period.
- [func completeStateRestoration()](nsapplication/completestaterestoration.md)
  Completes the extended state restoration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/restorewindow(withidentifier:state:completionhandler:))*
# willPresentError(_:)

**Framework**: AppKit  
**Kind**: method

Called when the receiver is about to present an error.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func willPresentError(_ error: any Error) -> any Error
```

#### Return Value

The error that should actually be presented.

#### Discussion

The default implementation of this method merely returns the passed-in error. The returned error may simply be forwarded to the document controller.

You can override this method to customize the presentation of errors by examining the passed-in error and, for example, returning more specific information. When you override this method always check the `NSError` object’s domain and code to discriminate between errors whose presentation you want to customize and those you don’t. For errors you don’t want to customize, call the superclass implementation, passing the original error.

## Parameters

- `error`: The error object that is about to be presented to the user.

## See Also

- [func presentError(any Error, modalFor: NSWindow, delegate: Any?, didPresent: Selector?, contextInfo: UnsafeMutableRawPointer?)](nsdocument/presenterror(_:modalfor:delegate:didpresent:contextinfo:).md)
  Presents an error alert to the user as a modal panel.
- [func presentError(any Error) -> Bool](nsdocument/presenterror(_:).md)
  Presents an error alert to the user as a modal panel.
- [func willNotPresentError(any Error)](nsdocument/willnotpresenterror(_:).md)
  Confirms that the error object is not to be presented to the user and the error cannot be recovered from, so cleanup can be done.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/willpresenterror(_:))*
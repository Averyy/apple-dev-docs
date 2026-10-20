# willPresentError(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Called when the receiver is about to present an error.

**Availability**:
- macOS

## Declaration

```swift
func willPresentError(_ error: any Error) -> any Error
```

```objc
- (NSError *) willPresentError:(NSError *) error;
```

#### Return Value

The error that should actually be presented.

#### Discussion

The default implementation of this method merely returns the passed-in error. The returned error may simply be forwarded to the document controller.

You can override this method to customize the presentation of errors by examining the passed-in error and, for example, returning more specific information. When you override this method always check the `NSError` object’s domain and code to discriminate between errors whose presentation you want to customize and those you don’t. For errors you don’t want to customize, call the superclass implementation, passing the original error.

## Parameters

- `error`: The error object that is about to be presented to the user.

## See Also

### Displaying Errors to the User
- [func presentError(any Error, modalFor: NSWindow, delegate: Any?, didPresent: Selector?, contextInfo: UnsafeMutableRawPointer?)](./presenterror%28_,modalfor,delegate,didpresent,contextinfo%29.md)
  Presents an error alert to the user as a modal panel.
- [func presentError(any Error) -> Bool](./presenterror%28_%29.md)
  Presents an error alert to the user as a modal panel.
- [func willNotPresentError(any Error)](./willnotpresenterror%28_%29.md)
  Confirms that the error object is not to be presented to the user and the error cannot be recovered from, so cleanup can be done.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/willpresenterror(_:))*
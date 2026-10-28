# presentError(_:modalFor:delegate:didPresent:contextInfo:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Presents an error alert to the user as a modal panel.

**Availability**:
- macOS

## Declaration

```swift
func presentError(_ error: any Error, modalFor window: NSWindow, delegate: Any?, didPresent didPresentSelector: Selector?, contextInfo: UnsafeMutableRawPointer?)
```

```objc
- (void) presentError:(NSError *) error modalForWindow:(NSWindow *) window delegate:(id) delegate didPresentSelector:(SEL) didPresentSelector contextInfo:(void *) contextInfo;
```

## Discussion

When the user dismisses the alert and any recovery possible for the error and chosen by the user has been attempted, sends the message `didPresentSelector` to the specified `delegate`. The method selected by `didPresentSelector` must have the same signature as:

```objc
- (void)didPresentErrorWithRecovery:(BOOL)didRecover contextInfo:(void  *)contextInfo;
```

The default `NSDocumentController` implementation of this method is equivalent to that of `NSResponder` while treating the application object as the next responder and forwarding error presentation messages to it. (The default `NSDocument` implementation of this method treats the shared `NSDocumentController` instance as the next responder and forwards these messages to it.)

The default implementation of this method calls [`willPresentError(_:)`](./willpresenterror%28_%29.md) to give subclasses an opportunity to customize error presentation. You should not override this method but should instead override [`willPresentError(_:)`](./willpresenterror%28_%29.md).

## Parameters

- `error`: The error to present.
- `window`: The window to present the error.
- `delegate`: The object to receive the selector.
- `didPresentSelector`: The selector to send to the delegate.
- `contextInfo`: A pointer to user-supplied data.

## See Also

### Handling Errors
- [func presentError(any Error) -> Bool](./presenterror%28_%29.md)
  Presents an error alert to the user as a modal panel.
- [func willPresentError(any Error) -> any Error](./willpresenterror%28_%29.md)
  Indicates an error condition and provides the opportunity to return the same or a different error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/presenterror(_:modalfor:delegate:didpresent:contextinfo:))*
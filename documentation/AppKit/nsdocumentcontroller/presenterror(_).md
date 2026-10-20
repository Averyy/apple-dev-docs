# presentError(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Presents an error alert to the user as a modal panel.

**Availability**:
- macOS

## Declaration

```swift
func presentError(_ error: any Error) -> Bool
```

```objc
- (BOOL) presentError:(NSError *) error;
```

#### Return Value

Returns [`true`](../../Swift/true.md) if error recovery was done; otherwise, [`false`](../../Swift/false.md).

#### Discussion

This method does not return until the user dismisses the alert and, if the error has recovery options and a recovery delegate, the error’s recovery delegate is sent an `attemptRecoveryFromError:optionIndex:` message.

The default `NSDocumentController` implementation of this method is equivalent to that of `NSResponder` while treating the application object as the next responder and forwarding error presentation messages to it. (The default `NSDocument` implementation of this method treats the shared `NSDocumentController` instance as the next responder and forwards these messages to it.) The default implementations of several `NSDocumentController` methods call this method.

The default implementation of this method calls [`willPresentError(_:)`](./willpresenterror%28_%29.md) to give subclasses an opportunity to customize error presentation. You should not override this method but should instead override [`willPresentError(_:)`](./willpresenterror%28_%29.md).

## Parameters

- `error`: An object containing the error to present.

## See Also

### Handling Errors
- [func presentError(any Error, modalFor: NSWindow, delegate: Any?, didPresent: Selector?, contextInfo: UnsafeMutableRawPointer?)](./presenterror%28_,modalfor,delegate,didpresent,contextinfo%29.md)
  Presents an error alert to the user as a modal panel.
- [func willPresentError(any Error) -> any Error](./willpresenterror%28_%29.md)
  Indicates an error condition and provides the opportunity to return the same or a different error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/presenterror(_:))*
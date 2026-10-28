# willPresentError(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Indicates an error condition and provides the opportunity to return the same or a different error.

**Availability**:
- macOS

## Declaration

```swift
func willPresentError(_ error: any Error) -> any Error
```

```objc
- (NSError *) willPresentError:(NSError *) error;
```

## Discussion

The default implementation of this method merely returns the passed-in error. The returned error may simply be forwarded to the application object.

You can override this method to customize the presentation of errors by examining the passed-in error and, for example, returning more specific information. When you override this method always check the `NSError` object’s domain and code to discriminate between errors whose presentation you want to customize and those you don’t. For errors you don’t want to customize, call the superclass implementation, passing the original error.

## Parameters

- `error`: The error to present.

## See Also

### Handling Errors
- [func presentError(any Error) -> Bool](./presenterror%28_%29.md)
  Presents an error alert to the user as a modal panel.
- [func presentError(any Error, modalFor: NSWindow, delegate: Any?, didPresent: Selector?, contextInfo: UnsafeMutableRawPointer?)](./presenterror%28_,modalfor,delegate,didpresent,contextinfo%29.md)
  Presents an error alert to the user as a modal panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocumentcontroller/willpresenterror(_:))*
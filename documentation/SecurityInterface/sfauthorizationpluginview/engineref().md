# engineRef()

**Framework**: Security Interface  
**Kind**: method  
**Role**: Instance Method

Returns the authorization engine handle with which this instance was initialized.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func engineRef() -> AuthorizationEngineRef!
```

```objc
- (AuthorizationEngineRef) engineRef;
```

## Return Value

A handle of type [`AuthorizationEngineRef`](../../Security/authorizationengineref.md).

## Discussion

Use the authorization engine handle when you call the functions in the [`AuthorizationCallbacks`](../../Security/authorizationcallbacks.md) structure to set a result or a context value.

## See Also

### Getting Instance Information
- [func callbacks() -> UnsafePointer<AuthorizationCallbacks>!](./callbacks%28%29.md)
  Returns the authorization callbacks structure with which this instance was initialized.
- [func lastError() -> (any Error)!](./lasterror%28%29.md)
  Returns the last error that occurred during evaluation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfauthorizationpluginview/engineref())*
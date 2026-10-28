# callbacks()

**Framework**: Security Interface  
**Kind**: method  
**Role**: Instance Method

Returns the authorization callbacks structure with which this instance was initialized.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func callbacks() -> UnsafePointer<AuthorizationCallbacks>!
```

```objc
- (const AuthorizationCallbacks *) callbacks;
```

## Return Value

An object of type [`AuthorizationCallbacks`](../../Security/authorizationcallbacks.md).

## Discussion

Use the [`AuthorizationCallbacks`](../../Security/authorizationcallbacks.md) structure to get the function pointers to functions such as `SetResult` and `SetContextValue`.

## See Also

### Getting Instance Information
- [func engineRef() -> AuthorizationEngineRef!](./engineref%28%29.md)
  Returns the authorization engine handle with which this instance was initialized.
- [func lastError() -> (any Error)!](./lasterror%28%29.md)
  Returns the last error that occurred during evaluation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfauthorizationpluginview/callbacks())*
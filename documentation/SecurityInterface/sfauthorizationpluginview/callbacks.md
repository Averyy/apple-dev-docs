# callbacks()

**Framework**: Security Interface  
**Kind**: method

Returns the authorization callbacks structure with which this instance was initialized.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func callbacks() -> UnsafePointer<AuthorizationCallbacks>!
```

#### Return Value

An object of type [`AuthorizationCallbacks`](https://developer.apple.com/documentation/Security/AuthorizationCallbacks).

#### Discussion

Use the [`AuthorizationCallbacks`](https://developer.apple.com/documentation/Security/AuthorizationCallbacks) structure to get the function pointers to functions such as `SetResult` and `SetContextValue`.

## See Also

- [func engineRef() -> AuthorizationEngineRef!](sfauthorizationpluginview/engineref.md)
  Returns the authorization engine handle with which this instance was initialized.
- [func lastError() -> (any Error)!](sfauthorizationpluginview/lasterror.md)
  Returns the last error that occurred during evaluation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfauthorizationpluginview/callbacks())*
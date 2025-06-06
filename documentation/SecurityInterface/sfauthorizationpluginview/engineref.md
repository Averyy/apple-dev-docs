# engineRef()

**Framework**: Security Interface  
**Kind**: method

Returns the authorization engine handle with which this instance was initialized.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func engineRef() -> AuthorizationEngineRef!
```

#### Return Value

A handle of type [`AuthorizationEngineRef`](https://developer.apple.com/documentation/Security/AuthorizationEngineRef).

#### Discussion

Use the authorization engine handle when you call the functions in the [`AuthorizationCallbacks`](https://developer.apple.com/documentation/Security/AuthorizationCallbacks) structure to set a result or a context value.

## See Also

- [func callbacks() -> UnsafePointer<AuthorizationCallbacks>!](sfauthorizationpluginview/callbacks.md)
  Returns the authorization callbacks structure with which this instance was initialized.
- [func lastError() -> (any Error)!](sfauthorizationpluginview/lasterror.md)
  Returns the last error that occurred during evaluation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfauthorizationpluginview/engineref())*
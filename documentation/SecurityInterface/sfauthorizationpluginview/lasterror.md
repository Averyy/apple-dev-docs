# lastError()

**Framework**: Security Interface  
**Kind**: method

Returns the last error that occurred during evaluation.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func lastError() -> (any Error)!
```

#### Discussion

Your authorization plug-in should override this method and return the last error that occurred during evaluation or `nil` if no error occurred.

A downstream plug-in can set a context value using the `kAuthorizationContextFlagSticky` flag to make it available to the `SFAuthorizationPluginView` class in case of an error.

## See Also

- [func callbacks() -> UnsafePointer<AuthorizationCallbacks>!](sfauthorizationpluginview/callbacks.md)
  Returns the authorization callbacks structure with which this instance was initialized.
- [func engineRef() -> AuthorizationEngineRef!](sfauthorizationpluginview/engineref.md)
  Returns the authorization engine handle with which this instance was initialized.


---

*[View on Apple Developer](https://developer.apple.com/documentation/securityinterface/sfauthorizationpluginview/lasterror())*
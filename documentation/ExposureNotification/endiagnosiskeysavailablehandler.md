# ENDiagnosisKeysAvailableHandler

**Framework**: Exposure Notification  
**Kind**: typealias

The handler the system invokes after requesting diagnosis keys.

**Availability**:
- iOS 14.4+
- iPadOS 14.4+
- Mac Catalyst 14.4+

## Declaration

```swift
typealias ENDiagnosisKeysAvailableHandler = ([ENTemporaryExposureKey]) -> Void
```

## Parameters

- `keys`: An array of temporary exposure keys.

## See Also

- [func requestPreAuthorizedDiagnosisKeys(completionHandler: ENErrorHandler)](enmanager/requestpreauthorizeddiagnosiskeys(completionhandler:).md)
  Requests diagnosis keys after the user authorizes sharing them.
- [func preAuthorizeDiagnosisKeys(completionHandler: ENErrorHandler)](enmanager/preauthorizediagnosiskeys(completionhandler:).md)
  Allows users to authorize a one-time release of diagnosis keys within five days of the authorization.
- [var diagnosisKeysAvailableHandler: ENDiagnosisKeysAvailableHandler?](enmanager/diagnosiskeysavailablehandler.md)
  The handler that receives available diagnosis keys after a successful preauthorization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/endiagnosiskeysavailablehandler)*
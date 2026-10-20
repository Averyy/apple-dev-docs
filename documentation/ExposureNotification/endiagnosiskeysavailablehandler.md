# ENDiagnosisKeysAvailableHandler

**Framework**: Exposure Notification  
**Kind**: typealias  
**Role**: Type Alias

The handler the system invokes after requesting diagnosis keys.

**Availability**:
- iOS 14.4+ - Deprecated in 27.0
- iPadOS 14.4+ - Deprecated in 27.0
- Mac Catalyst 14.4+ - Deprecated in 27.0

> **Deprecated**: No longer supported.

## Declaration

```swift
typealias ENDiagnosisKeysAvailableHandler = ([ENTemporaryExposureKey]) -> Void
```

```c
typedef void (^)(NSArray<ENTemporaryExposureKey *> *) ENDiagnosisKeysAvailableHandler;
```

## Parameters

- `keys`: An array of temporary exposure keys.

## See Also

### Preauthorizing Exposure Keys
- [func requestPreAuthorizedDiagnosisKeys(completionHandler: ((any Error)?) -> Void)](./enmanager/requestpreauthorizeddiagnosiskeys%28completionhandler%29.md)
  Requests diagnosis keys after the user authorizes sharing them.
- [func preAuthorizeDiagnosisKeys(completionHandler: ((any Error)?) -> Void)](./enmanager/preauthorizediagnosiskeys%28completionhandler%29.md)
  Allows users to authorize a one-time release of diagnosis keys within five days of the authorization.
- [var diagnosisKeysAvailableHandler: ENDiagnosisKeysAvailableHandler?](./enmanager/diagnosiskeysavailablehandler.md)
  The handler that receives available diagnosis keys after a successful preauthorization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/endiagnosiskeysavailablehandler)*
# diagnosisKeysAvailableHandler

**Framework**: Exposure Notification  
**Kind**: property  
**Role**: Instance Property

The handler that receives available diagnosis keys after a successful preauthorization.

**Availability**:
- iOS 14.4+ - Deprecated in 27.0
- iPadOS 14.4+ - Deprecated in 27.0
- Mac Catalyst 14.4+ - Deprecated in 27.0

> **Deprecated**: No longer supported.

## Declaration

```swift
var diagnosisKeysAvailableHandler: ENDiagnosisKeysAvailableHandler? { get set }
```

```objc
@property (nonatomic, copy, readwrite, nullable) ENDiagnosisKeysAvailableHandler diagnosisKeysAvailableHandler;
```

## Discussion

Set this property before calling  [`requestPreAuthorizedDiagnosisKeys(completionHandler:)`](./requestpreauthorizeddiagnosiskeys%28completionhandler%29.md) to ensure [`ENManager`](../enmanager.md) can deliver the keys. Authorization expires after five days or the first time this method is called after authorization, whichever comes first.

## See Also

### Preauthorizing Exposure Keys
- [func requestPreAuthorizedDiagnosisKeys(completionHandler: ((any Error)?) -> Void)](./requestpreauthorizeddiagnosiskeys%28completionhandler%29.md)
  Requests diagnosis keys after the user authorizes sharing them.
- [func preAuthorizeDiagnosisKeys(completionHandler: ((any Error)?) -> Void)](./preauthorizediagnosiskeys%28completionhandler%29.md)
  Allows users to authorize a one-time release of diagnosis keys within five days of the authorization.
- [typealias ENDiagnosisKeysAvailableHandler](../endiagnosiskeysavailablehandler.md)
  The handler the system invokes after requesting diagnosis keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enmanager/diagnosiskeysavailablehandler)*
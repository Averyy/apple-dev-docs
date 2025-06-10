# diagnosisKeysAvailableHandler

**Framework**: Exposure Notification  
**Kind**: property

The handler that receives available diagnosis keys after a successful preauthorization.

**Availability**:
- iOS 14.4+
- iPadOS 14.4+
- Mac Catalyst 14.4+

## Declaration

```swift
var diagnosisKeysAvailableHandler: ENDiagnosisKeysAvailableHandler? { get set }
```

#### Discussion

Set this property before calling  [`requestPreAuthorizedDiagnosisKeys(completionHandler:)`](enmanager/requestpreauthorizeddiagnosiskeys(completionhandler:).md) to ensure [`ENManager`](enmanager.md) can deliver the keys. Authorization expires after five days or the first time this method is called after authorization, whichever comes first.

## See Also

- [func requestPreAuthorizedDiagnosisKeys(completionHandler: ((any Error)?) -> Void)](enmanager/requestpreauthorizeddiagnosiskeys(completionhandler:).md)
  Requests diagnosis keys after the user authorizes sharing them.
- [func preAuthorizeDiagnosisKeys(completionHandler: ((any Error)?) -> Void)](enmanager/preauthorizediagnosiskeys(completionhandler:).md)
  Allows users to authorize a one-time release of diagnosis keys within five days of the authorization.
- [typealias ENDiagnosisKeysAvailableHandler](endiagnosiskeysavailablehandler.md)
  The handler the system invokes after requesting diagnosis keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/exposurenotification/enmanager/diagnosiskeysavailablehandler)*